#!/bin/bash


# =================================================================================================================
# Usage:
# -----------------------------------------------------------------------------------------------------------------
usage() {
  cat <<-EOF
  A helper script to compare the secrets from 1password' vault for different environments.
  Usage: ./1pass_compare.sh [-h -d <subdomainName> -u <accountName>]
                             -k <secretKey>
                             -p <masterPassword>
                             -e <environments>
                             -v <vaultDetails>
                             -a <appName>

  OPTIONS:
  ========
    -h prints the usage for the script.
    -a Openshift application name, for example: auth-api-dev
    -d The subdomain name of the 1password account, default is registries.1password.ca.
    -u The account name of the 1password account, default is bcregistries.devops@gmail.com.
    -k The secret key of the 1password account.
    -p The master password of the 1password account.
    -e The environments of the vault, for example : "dev test"/"test prod".
    -v A list of vault and application name of the 1password account, for example:
       [
          {
              "vault": "shared",
              "application": [
                  "keycloak",
                  "email"
              ]
          },
          {
              "vault": "relationship",
              "application": [
                  "auth-api",
                  "notify-api",
                  "status-api"
              ]
          }
      ]

EOF
exit
}

# -----------------------------------------------------------------------------------------------------------------
# Initialization:
# -----------------------------------------------------------------------------------------------------------------
while getopts h:d:u:k:p:v:e: FLAG; do
  case $FLAG in
    h ) usage ;;
    d ) DOMAIN_NAME=$OPTARG ;;
    u ) USERNAME=$OPTARG ;;
    k ) SECRET_KEY=$OPTARG ;;
    p ) MASTER_PASSWORD=$OPTARG ;;
    v ) VAULT=$OPTARG ;;
    e ) ENVIRONMENTS=$OPTARG ;;
    \? ) #unrecognized option - show help
      echo -e \\n"Invalid script option: -${OPTARG}"\\n
      usage
      ;;
  esac
done

# Shift the parameters in case there any more to be used
shift $((OPTIND-1))
# echo Remaining arguments: $@

if [ -z "${DOMAIN_NAME}" ]; then
  DOMAIN_NAME=registries.1password.ca
fi

if [ -z "${USERNAME}" ]; then
  USERNAME=bcregistries.devops@gmail.com
fi

if [ -z "${SECRET_KEY}" ] || [ -z "${MASTER_PASSWORD}" ] || [ -z "${VAULT}" ]  ||  [ -z "${ENVIRONMENTS}" ]; then
  echo -e \\n"Missing parameters - secret key, master password, vault or environment"\\n
  usage
fi

envs=(${ENVIRONMENTS})
echo envs
if [[ ${#envs[@]} != 2 ]]; then
  echo -e \\n"Environments must be two values"\\n
  exit
fi

# Login to 1Password../s
# Assumes you have installed the OP CLI and performed the initial configuration
# For more details see https://support.1password.com/command-line-getting-started/
eval $(echo "${MASTER_PASSWORD}" | op signin ${DOMAIN_NAME} ${USERNAME} ${SECRET_KEY})

num=0
for env_name in "${envs[@]}"; do
  num=$((num+1))
  for vault_name in $(echo "${VAULT}" | jq -r '.[] | @base64' ); do
    _jq() {
      echo ${vault_name} | base64 --decode | jq -r ${1}
    }
    for application_name in $(echo "$(_jq '.application')" | jq -r '.[]| @base64' ); do
      _jq_app() {
        echo ${application_name} | base64 --decode
      }

      # My setup uses a 1Password type of 'Password' and stores all records within a
      # single section. The label is the key, and the value is the value.
      ev=`op get item --vault=$(_jq .vault) ${env_name}`

      # Convert to base64 for multi-line secrets.
      # The schema for the 1Password type uses t as the label, and v as the value.
      # Set secrets to env
      for row in $(echo ${ev} | jq -r -c '.details.sections[] | select(.title=='\"$(_jq_app)\"') | .fields[] | @base64'); do
        _envvars() {
          echo ${row} | base64 --decode | jq -r ${1}
        }
        echo $(_envvars '.t') >> t$num.txt
      done
    done
  done
done

if [[ -z $(comm -23 <(sort t1.txt) <(sort t2.txt)) ]]; then
  if [[ -z $(comm -23 <(sort t2.txt) <(sort t1.txt)) ]]; then
    echo ::set-env name=approval::true
    echo ::set-env name=message::The vault items in ${ENVIRONMENTS} are matched.
  else
    echo ::set-env name=approval::false
    echo ::set-env name=message::The vault items in ${ENVIRONMENTS} does not match. Please check it out in 1password.
  fi
else
  echo ::set-env name=approval::false
  echo ::set-env name=message::The vault items in ${ENVIRONMENTS} does not match. Please check it out in 1password.
fi

rm t*.txt

exit


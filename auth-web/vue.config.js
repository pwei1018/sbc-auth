var path = require('path')
const RemoveServiceWorkerPlugin = require('webpack-remove-serviceworker-plugin')
const webpack = require('webpack')
const fs = require('fs')
const packageJson = fs.readFileSync('./package.json')
const name = JSON.parse(packageJson).name
const appName = JSON.parse(packageJson).appName
const appVersion = JSON.parse(packageJson).version
const sbcName = JSON.parse(packageJson).sbcName
const sbcVersion = JSON.parse(packageJson).dependencies['sbc-common-components']
const aboutText1 = (appName && appVersion) ? `${appName} v${appVersion}` : ''
const aboutText2 = (sbcName && sbcVersion) ? `${sbcName} v${sbcVersion}` : ''

module.exports = {
  configureWebpack: {
    plugins: [
      // this is needed to remove existing service workers on users' systems
      // ref: https://www.npmjs.com/package/webpack-remove-serviceworker-plugin
      // ref: https://github.com/NekR/self-destroying-sw/tree/master/packages/webpack-remove-serviceworker-plugin
      new RemoveServiceWorkerPlugin({ filename: 'service-worker.js' }),
      new webpack.DefinePlugin({
        'process.env': {
          ABOUT_TEXT:
            (aboutText1 && aboutText2) ? `"${aboutText1}<br>${aboutText2}"`
              : aboutText1 ? `"${aboutText1}"`
                : aboutText2 ? `"${aboutText2}"`
                  : '',
          APP_NAME: `"${name}"`
        }
      })
    ],
    devtool: 'source-map',
    resolve: {
      alias: {
        'vue': path.resolve('./node_modules/vue'),
        '$assets': path.resolve('./src/assets/')
      }
    }
  },
  publicPath: process.env.VUE_APP_PATH,
  transpileDependencies: ['vuetify', 'vuex-persist'],
  devServer: {
    overlay: {
      warnings: true,
      errors: true
    }
  },
  pwa: {
    name: 'Business Registry',
    themeColor: '#003366',
    msTileColor: '#fcba19',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    manifestOptions: {
      name: 'Business Registry',
      short_name: 'Business Registry',
      start_url: '/business/auth/',
      display: 'standalone',
      theme_color: '#003366',
      background_color: '#fcba19',
      scope: '.'
    },
    iconPaths: {
      favicon32: 'img/icons/favicon-32x32.png',
      favicon16: 'img/icons/favicon-16x16.png',
      appleTouchIcon: 'img/icons/apple-touch-icon-152x152.png',
      maskIcon: 'img/icons/safari-pinned-tab.svg',
      msTileImage: 'img/icons/msapplication-icon-144x144.png'
    },
    workboxPluginMode: 'InjectManifest',
    workboxOptions: {
      // swSrc is required in InjectManifest mode.
      swSrc: 'src/service-worker.js',
      // skip precaching json files such as configs
      exclude: [/\.json$/]
    }
  }
}

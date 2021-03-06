"""business_type_and_size

Revision ID: 08e1d49dfa1a
Revises: 9b04140db7d3
Create Date: 2021-06-08 12:04:16.210558

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '08e1d49dfa1a'
down_revision = '9b04140db7d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bus_size = op.create_table('business_size_codes',
                               sa.Column('code', sa.String(length=15), nullable=False),
                               sa.Column('description', sa.String(length=100), nullable=True),
                               sa.Column('default', sa.Boolean(), nullable=True),
                               sa.PrimaryKeyConstraint('code')
                               )
    bus_type = op.create_table('business_type_codes',
                               sa.Column('code', sa.String(length=15), nullable=False),
                               sa.Column('description', sa.String(length=100), nullable=True),
                               sa.Column('default', sa.Boolean(), nullable=True),
                               sa.PrimaryKeyConstraint('code')
                               )

    op.bulk_insert(
        bus_size,
        [
            {
                "code": "0-1",
                "description": "1 Employee",
                "default": True
            },
            {
                "code": "2-5",
                "description": "2-5 Employees",
                "default": False
            },
            {
                "code": "6-10",
                "description": "6-10 Employees",
                "default": False
            },
            {
                "code": "11-20",
                "description": "11-20 Employees",
                "default": False
            },
            {
                "code": "21-30",
                "description": "21-30 Employees",
                "default": False
            },
            {
                "code": "30",
                "description": "More than 30 Employees",
                "default": False
            }
        ]
    )

    op.bulk_insert(
        bus_type,
        [
            {
                "code": "BIZ",
                "description": "GENERAL BUSINESS",
                "default": False
            },
            {
                "code": "BIZAC",
                "description": "ACCOUNTING FIRM",
                "default": False
            },
            {
                "code": "BIZEL",
                "description": "ELECTRICAL CONTRACTOR",
                "default": False
            },
            {
                "code": "BIZGA",
                "description": "GAS CONTRACTOR",
                "default": False
            },
            {
                "code": "BIZGE",
                "description": "GAS & ELECTRICAL CONTRACTOR",
                "default": False
            },
            {
                "code": "BSPLY",
                "description": "BUILDING SUPPLIES",
                "default": False
            },
            {
                "code": "CAR",
                "description": "AUTOMOBILE DEALER",
                "default": False
            },
            {
                "code": "CAREQ",
                "description": "RV'S, HEAVY TRUCK & EQUIPMENT DEALER",
                "default": False
            },
            {
                "code": "CON",
                "description": "CONSULTING FIRMS",
                "default": False
            },
            {
                "code": "EDUC",
                "description": "SCHOOLS, COLLEGES, OR UNIVERSITIES",
                "default": False
            },
            {
                "code": "EXPLR",
                "description": "GAS, PETROLEUM AND MINERAL EXPLORATION",
                "default": False
            },
            {
                "code": "FINBA",
                "description": "BANK",
                "default": False
            },
            {
                "code": "FINCO",
                "description": "FINANCING COMPANY",
                "default": False
            },
            {
                "code": "FINCU",
                "description": "CREDIT UNION",
                "default": False
            },
            {
                "code": "FINIC",
                "description": "INVESTMENT COMPANY",
                "default": False
            },
            {
                "code": "FINLE",
                "description": "LEASING COMPANY",
                "default": False
            },
            {
                "code": "FINTR",
                "description": "TRUST COMPANY",
                "default": False
            },
            {
                "code": "FIRNA",
                "description": "FIRST NATION INDIAN BAND",
                "default": False
            },
            {
                "code": "FOR",
                "description": "FORESTRY",
                "default": False
            },
            {
                "code": "GOVA",
                "description": "GOVERNMENT AGENCY OR AUTHORITY",
                "default": False
            },
            {
                "code": "GOVAA",
                "description": "BCA",
                "default": False
            },
            {
                "code": "GOVCC",
                "description": "CROWN CORPORATION",
                "default": False
            },
            {
                "code": "GOVD",
                "description": "DISTRICT GOVERNMENT",
                "default": False
            },
            {
                "code": "GOVF",
                "description": "FEDERAL GOVERNMENT",
                "default": False
            },
            {
                "code": "GOVGA",
                "description": "GOVERNMENT AGENTS BRANCH",
                "default": False
            },
            {
                "code": "GOVL",
                "description": "MUNICIPALITY",
                "default": False
            },
            {
                "code": "GOVLT",
                "description": "LTSA",
                "default": False
            },
            {
                "code": "GOVM",
                "description": "BC GOVERNMENT MINISTRY",
                "default": False
            },
            {
                "code": "GOVOP",
                "description": "OTHER PROVINCIAL GOVT. MINISTRY",
                "default": False
            },
            {
                "code": "GOVP",
                "description": "RCMP OR LAW ENFORCEMENT",
                "default": False
            },
            {
                "code": "GOVR",
                "description": "REGISTRIES WHO PARTICIPATE IN BCOL",
                "default": False
            },
            {
                "code": "GOVSR",
                "description": "GOVERNMENT SELF REGULATORY",
                "default": False
            },
            {
                "code": "HLTH",
                "description": "REGIONAL HEALTH UNITS",
                "default": False
            },
            {
                "code": "INSUR",
                "description": "INSURANCE AGENCIES",
                "default": False
            },
            {
                "code": "INTRN",
                "description": "INTERNAL BCOL ACCOUNT",
                "default": False
            },
            {
                "code": "LAW",
                "description": "LAW FIRM",
                "default": False
            },
            {
                "code": "LAWNP",
                "description": "NOTARY PUBLICS",
                "default": False
            },
            {
                "code": "LDB",
                "description": "LIQUOR DISTRIBUTION",
                "default": False
            },
            {
                "code": "LDBC",
                "description": "LAND DATA BC",
                "default": False
            },
            {
                "code": "MAR",
                "description": "MARINE",
                "default": False
            },
            {
                "code": "OTHCC",
                "description": "CHAMBER OF COMMERCE",
                "default": False
            },
            {
                "code": "OTHCR",
                "description": "CREDIT REPORTING, PI, SKIP TRACERS",
                "default": False
            },
            {
                "code": "OTHER",
                "description": "OTHER",
                "default": False
            },
            {
                "code": "OTHNE",
                "description": "NEWS MEDIA",
                "default": False
            },
            {
                "code": "OTHUN",
                "description": "UNION",
                "default": False
            },
            {
                "code": "PILOT",
                "description": "HRV",
                "default": False
            },
            {
                "code": "REAL",
                "description": "REALTOR",
                "default": False
            },
            {
                "code": "REALA",
                "description": "APPRAISER",
                "default": False
            },
            {
                "code": "REALB",
                "description": "REAL ESTATE BOARD",
                "default": False
            },
            {
                "code": "RESRC",
                "description": "RESEARCH & DEVELOPMENT",
                "default": False
            },
            {
                "code": "SES",
                "description": "MUNICIPAL AFFAIRS",
                "default": False
            },
            {
                "code": "SURV",
                "description": "BC LAND SURVEYOR",
                "default": False
            },
            {
                "code": "TSC",
                "description": "TITLE SEARCH COMPANY",
                "default": False
            }
        ]
    )
    op.add_column('orgs', sa.Column('is_business_account', sa.Boolean(), nullable=True))
    op.add_column('orgs', sa.Column('business_size', sa.String(length=15), nullable=True))
    op.add_column('orgs', sa.Column('business_type', sa.String(length=15), nullable=True))
    op.create_foreign_key('orgs_business_type_fkey', 'orgs', 'business_type_codes', ['business_type'],
                          ['code'], ondelete='SET NULL')
    op.create_foreign_key('orgs_business_size_fkey', 'orgs', 'business_size_codes', ['business_size'],
                          ['code'], ondelete='SET NULL')
    op.add_column('orgs_version', sa.Column('is_business_account', sa.Boolean(), autoincrement=False, nullable=True))
    op.add_column('orgs_version',
                  sa.Column('business_size', sa.String(length=15), autoincrement=False, nullable=True))
    op.add_column('orgs_version',
                  sa.Column('business_type', sa.String(length=15), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orgs_version', 'business_type')
    op.drop_column('orgs_version', 'business_size')
    op.drop_column('orgs_version', 'is_business_account')
    op.drop_constraint('orgs_business_size_fkey', 'orgs', type_='foreignkey')
    op.drop_constraint('orgs_business_type_fkey', 'orgs', type_='foreignkey')
    op.drop_column('orgs', 'business_type')
    op.drop_column('orgs', 'business_size')
    op.drop_column('orgs', 'is_business_account')
    op.drop_table('business_type_codes')
    op.drop_table('business_size_codes')
    # ### end Alembic commands ###

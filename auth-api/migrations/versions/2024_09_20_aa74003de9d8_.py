"""empty message

Revision ID: aa74003de9d8
Revises: 69f7b110a98c
Create Date: 2024-09-20 11:19:42.551199

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "aa74003de9d8"
down_revision = "69f7b110a98c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "affidavits_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("document_id", sa.String(length=60), autoincrement=False, nullable=True),
        sa.Column("issuer", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("status_code", sa.String(length=15), autoincrement=False, nullable=False),
        sa.Column("decision_made_by", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("decision_made_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("user_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("affidavits_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_affidavits_history_document_id"), ["document_id"], unique=False)

    op.create_table(
        "orgs_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("uuid", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("type_code", sa.String(length=15), autoincrement=False, nullable=False),
        sa.Column("status_code", sa.String(length=30), autoincrement=False, nullable=False),
        sa.Column("name", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("branch_name", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("access_type", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("decision_made_by", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("decision_made_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("bcol_user_id", sa.String(length=20), autoincrement=False, nullable=True),
        sa.Column("bcol_account_id", sa.String(length=20), autoincrement=False, nullable=True),
        sa.Column("bcol_account_name", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("suspended_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("suspension_reason_code", sa.String(length=15), autoincrement=False, nullable=True),
        sa.Column("has_api_access", sa.Boolean(), autoincrement=False, nullable=True),
        sa.Column("business_type", sa.String(length=15), autoincrement=False, nullable=True),
        sa.Column("business_size", sa.String(length=15), autoincrement=False, nullable=True),
        sa.Column("is_business_account", sa.Boolean(), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["business_size"], ["business_size_codes.code"], name="orgs_business_size_fkey", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["business_type"], ["business_type_codes.code"], name="orgs_business_type_fkey", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["suspension_reason_code"],
            ["suspension_reason_codes.code"],
            name="orgs_suspension_reason_code_fkey",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["type_code"],
            ["org_types.code"],
        ),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("orgs_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_orgs_history_access_type"), ["access_type"], unique=False)
        batch_op.create_index(batch_op.f("ix_orgs_history_name"), ["name"], unique=False)

    op.create_table(
        "account_login_options_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("login_source", sa.String(length=20), autoincrement=False, nullable=False),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("is_active", sa.Boolean(), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["status_code"],
            ["affidavit_statuses.code"],
        ),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "affiliations_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("entity_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("certified_by_name", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("environment", sa.String(length=20), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["status_code"],
            ["affidavit_statuses.code"],
        ),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("affiliations_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_affiliations_history_entity_id"), ["entity_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_affiliations_history_environment"), ["environment"], unique=False)

    op.create_table(
        "contacts_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("street", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("street_additional", sa.String(length=250), autoincrement=False, nullable=True),
        sa.Column("city", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("region", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("country", sa.String(length=20), autoincrement=False, nullable=True),
        sa.Column("postal_code", sa.String(length=15), autoincrement=False, nullable=True),
        sa.Column("delivery_instructions", sa.String(length=4096), autoincrement=False, nullable=True),
        sa.Column("phone", sa.String(length=15), autoincrement=False, nullable=True),
        sa.Column("phone_extension", sa.String(length=10), autoincrement=False, nullable=True),
        sa.Column("email", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("entity_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("contacts_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_contacts_history_street"), ["street"], unique=False)

    op.create_table(
        "memberships_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("membership_type_code", sa.String(length=15), autoincrement=False, nullable=False),
        sa.Column("status", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["membership_type_code"],
            ["membership_types.code"],
        ),
        sa.ForeignKeyConstraint(
            ["status"],
            ["membership_status_codes.id"],
        ),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("memberships_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_memberships_history_org_id"), ["org_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_memberships_history_status"), ["status"], unique=False)
        batch_op.create_index(batch_op.f("ix_memberships_history_user_id"), ["user_id"], unique=False)

    op.create_table(
        "org_settings_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("setting", sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column("enabled", sa.Boolean(), autoincrement=False, nullable=False),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "product_subscriptions_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("product_code", sa.String(length=15), autoincrement=False, nullable=False),
        sa.Column("status_code", sa.String(length=30), autoincrement=False, nullable=False),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_code"],
            ["product_codes.code"],
        ),
        sa.ForeignKeyConstraint(
            ["status_code"],
            ["product_subscriptions_statuses.code"],
        ),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("product_subscriptions_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_product_subscriptions_history_org_id"), ["org_id"], unique=False)

    op.create_table(
        "contact_links_history",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("contact_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("entity_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("user_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("org_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("affidavit_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("modified", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("created_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("modified_by_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("version", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("changed", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", "version"),
        sqlite_autoincrement=True,
    )
    with op.batch_alter_table("contact_links_history", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_contact_links_history_contact_id"), ["contact_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_contact_links_history_entity_id"), ["entity_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_contact_links_history_org_id"), ["org_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_contact_links_history_user_id"), ["user_id"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("contact_links_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_contact_links_history_user_id"))
        batch_op.drop_index(batch_op.f("ix_contact_links_history_org_id"))
        batch_op.drop_index(batch_op.f("ix_contact_links_history_entity_id"))
        batch_op.drop_index(batch_op.f("ix_contact_links_history_contact_id"))

    op.drop_table("contact_links_history")
    with op.batch_alter_table("product_subscriptions_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_product_subscriptions_history_org_id"))

    op.drop_table("product_subscriptions_history")
    op.drop_table("org_settings_history")
    with op.batch_alter_table("memberships_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_memberships_history_user_id"))
        batch_op.drop_index(batch_op.f("ix_memberships_history_status"))
        batch_op.drop_index(batch_op.f("ix_memberships_history_org_id"))

    op.drop_table("memberships_history")
    with op.batch_alter_table("contacts_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_contacts_history_street"))

    op.drop_table("contacts_history")
    with op.batch_alter_table("affiliations_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_affiliations_history_environment"))
        batch_op.drop_index(batch_op.f("ix_affiliations_history_entity_id"))

    op.drop_table("affiliations_history")
    op.drop_table("account_login_options_history")
    with op.batch_alter_table("orgs_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_orgs_history_name"))
        batch_op.drop_index(batch_op.f("ix_orgs_history_access_type"))

    op.drop_table("orgs_history")
    with op.batch_alter_table("affidavits_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_affidavits_history_document_id"))

    op.drop_table("affidavits_history")
    # ### end Alembic commands ###

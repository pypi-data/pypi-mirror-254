# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Shared RDM.
#
# invenio_override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for sharedRDM theme."""

from invenio_i18n import gettext as _

INVENIO_OVERRIDE_BASE_TEMPLATE = "invenio_override/base.html"
"""Default base template"""

INVENIO_OVERRIDE_ACCOUNT_BASE = "invenio_override/accounts/accounts_base.html"
"""Default account base template"""

INVENIO_OVERRIDE_ICON = "images/icon_use.png"
"""Icon used in login page"""

INVENIO_OVERRIDE_CONTACT_FORM = False
"""Enable/Disable Contact form."""

INVENIO_OVERRIDE_PRODUCTION = False
"""Production environment.

    Can also be set as an environment variable in a .env file. Then the name
    has to be 'INVENIO_OVERRIDE_PRODUCTION'.
"""

OVERRIDE_ROUTES = {
    "index": "/",
    "comingsoon": "/comingsoon",
}

INVENIO_OVERRIDE_LOGO = "images/TUG.png"
"""override logo"""

# TODO: fix it
INVENIO_OVERRIDE_FAVICON = "favicon.ico"
"""override favicon"""

INVENIO_OVERRIDE_SHIBBOLETH = False
"""Set True if SAML is configured"""

# Invenio-theme
# ============
# See https://invenio-theme.readthedocs.io/en/latest/configuration.html
#

THEME_SEARCHBAR = False
"""Enable or disable the header search bar."""

THEME_HEADER_TEMPLATE = "invenio_override/header.html"
"""header template"""

THEME_FRONTPAGE = False
"""Use default frontpage."""

THEME_HEADER_LOGIN_TEMPLATE = "invenio_override/accounts/header_login.html"
"""login page header"""

THEME_FOOTER_TEMPLATE = "invenio_override/footer.html"
"""footer template"""

THEME_FRONTPAGE_TITLE = _("Repository")
"""Frontpage title."""

THEME_SITENAME = _("Repository")
"""Site name."""

# Invenio-accounts
# ============
# See https://invenio-accounts.readthedocs.io/en/latest/configuration.html

# COVER_TEMPLATE = 'invenio_override/accounts/accounts_base.html'
"""Cover page template for login and sign up pages."""

SECURITY_LOGIN_USER_TEMPLATE = "invenio_override/accounts/login_user.html"
"""Login template"""

SECURITY_REGISTER_USER_TEMPLATE = "invenio_override/accounts/register_user.html"
"""Sigup template"""

# Invenio-app-rdm
# =============
# See https://invenio-app-rdm.readthedocs.io/en/latest/configuration.html
SEARCH_UI_HEADER_TEMPLATE = "invenio_override/header.html"
"""Search page's header template."""

DEPOSITS_HEADER_TEMPLATE = "invenio_override/header.html"
"""Deposits header page's template."""


# Invenio-rdm-records
# =============
# See https://invenio-rdm-records.readthedocs.io/en/latest/configuration.html
# Uncomment below to override records landingpage.
# from invenio_rdm_records.config import RECORDS_UI_ENDPOINTS
# RECORDS_UI_ENDPOINTS["recid"].update(
#     template="invenio_override/record_landing_page.html"
# )
"""override the default record landing page"""

# Invenio-search-ui
# =============
# See https://invenio-search-ui.readthedocs.io/en/latest/configuration.html
# SEARCH_UI_SEARCH_TEMPLATE = "invenio_override/search.html"
# """override the default search page"""


# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html
BABEL_DEFAULT_LOCALE = "en"
# Default time zone
BABEL_DEFAULT_TIMEZONE = "Europe/Vienna"
# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
I18N_LANGUAGES = [("de", _("German"))]

# Invenio-Mail
# ===========
# See https://invenio-mail.readthedocs.io/en/latest/configuration.html

MAIL_SERVER = "localhost"
"""Domain ip where mail server is running."""

SECURITY_EMAIL_SENDER = "info@example.com"
"""Email address used as sender of account registration emails."""
"""Domain name should match the domain used in web server."""

SECURITY_EMAIL_SUBJECT_REGISTER = _("Welcome to The Repository!")
"""Email subject for account registration emails."""

MAIL_SUPPRESS_SEND = True
"""Enable email sending by default.

Set this to False when sending actual emails.
"""

# Invenio-userprofiles
# ===========
# See https://invenio-userprofiles.readthedocs.io/en/latest/configuration.html

USERPROFILES_EXTEND_SECURITY_FORMS = True
"""Set True in order to register user_profile.

This also forces user to add username and fullname
when register.
"""

USERPROFILES_EMAIL_ENABLED = True
"""Exclude the user email in the profile form."""

USERPROFILES_READ_ONLY = True
"""Allow users to change profile info (name, email, etc...)."""

# Invenio-saml
# ===========
# See https://invenio-saml.readthedocs.io/en/latest/configuration.html

SSO_SAML_IDPS = {}
"""Configuration of IDPS. Actual values can be find in to invenio.cfg file"""

SSO_SAML_DEFAULT_BLUEPRINT_PREFIX = "/shibboleth"
"""Base URL for the extensions endpoint."""

SSO_SAML_DEFAULT_METADATA_ROUTE = "/metadata/<idp>"
"""URL route for the metadata request."""
"""This is also SP entityID https://domain/shibboleth/metadata/<idp>"""

SSO_SAML_DEFAULT_SSO_ROUTE = "/login/<idp>"
"""URL route for the SP login."""

SSO_SAML_DEFAULT_ACS_ROUTE = "/authorized/<idp>"
"""URL route to handle the IdP login request."""

SSO_SAML_DEFAULT_SLO_ROUTE = "/slo/<idp>"
"""URL route for the SP logout."""

SSO_SAML_DEFAULT_SLS_ROUTE = "/sls/<idp>"
"""URL route to handle the IdP logout request."""

# Invenio-accounts
# ===========
# See https://invenio-accounts.readthedocs.io/en/latest/configuration.html

ACCOUNTS_LOCAL_LOGIN_ENABLED = True
"""Allow local login."""

SECURITY_CHANGEABLE = False
"""Allow password change by users."""

SECURITY_RECOVERABLE = False
"""Allow password recovery by users."""

SECURITY_REGISTERABLE = True
""""Allow users to register.

With this variable set to "False" users will not be
able to register, or to navigate to /sigup page.
"""

SECURITY_CONFIRMABLE = False
"""Allow user to confirm their email address.

Instead user will get a welcome email.
"""

SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
"""Require users to confirm email before being able to login."""

# Flask-Security
# =============
# See https://pythonhosted.org/Flask-Security/configuration.html
SECURITY_EMAIL_PLAINTEXT = True
"""Render email content as plaintext."""

SECURITY_EMAIL_HTML = False
"""Render email content as HTML."""


ACCOUNTS = True
"""Tells if the templates should use the accounts module.

If False, you won't be able to login via the web UI.

Instead if you have a overriden template somewhere in your config.py:
like this:
SECURITY_LOGIN_USER_TEMPLATE = 'invenio_override/accounts/login.html'
then you can remove this condition from header_login.htm:
{%- if config.ACCOUNTS %}
to render your overriden login.html
"""

# Accounts
# ========
# Actual values can be find in to invenio.cfg file
#: Recaptcha public key (change to enable).
RECAPTCHA_PUBLIC_KEY = None
#: Recaptcha private key (change to enable).
RECAPTCHA_PRIVATE_KEY = None

# invenio-rdm-records
# =======
# See:
# https://invenio-rdm-records.readthedocs.io/en/latest/configuration.html
#
RDM_RECORDS_USER_FIXTURE_PASSWORDS = {"info@tugraz.at": None}
"""Overrides for the user fixtures' passwords.
The password set for a user fixture in this dictionary overrides the
password set in the ``users.yaml`` file. This can be used to set custom
passwords for the fixture users (of course, this has to be configured
before the fixtures are installed, e.g. by setting up the services).
If ``None`` or an empty string is configured in this dictionary, then the
password from ``users.yaml`` will be used. If that is also absent, a password
will be generated randomly.
"""

DATACITE_FORMAT = "{prefix}/{id}"
"""Customize the generated DOI string."""

DATACITE_DATACENTER_SYMBOL = ""
""""The OAI-PMH server's metadata format oai_datacite
that allows you to harvest record from InvenioRDM in DataCite XML needs
to be configured with your DataCite data center symbol.
This is only required if you want your records to be harvestable in DataCite XML format.
"""


SQLALCHEMY_ECHO = False
"""Enable to see all SQL queries."""

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": False,
    "pool_recycle": 3600,
    # set a more agressive timeout to ensure http requests don't wait for long
    "pool_timeout": 10,
}
"""SQLAlchemy engine options.

This is used to configure for instance the database connection pool.
Specifically for connection pooling the following options below are relevant.
Note, that the connection pool settings have to be aligned with:

1. your database server's max allowed connections settings, and
2. your application deployment (number of processes/threads)

**Disconnect handling**

Note, it's possible that a connection you get from the connection pool is no
longer open. This happens if e.g. the database server was restarted or the
server has a timeout that closes the connection. In these case you'll see an
error similar to::

    psycopg2.OperationalError: server closed the connection unexpectedly
        This probably means the server terminated abnormally
        before or while processing the request.

The errors can be avoided by using the ``pool_pre_ping`` option, which will
ensure the connection is open first by issuing a ``SELECT 1``. The pre-ping
feature however, comes with a performance penalty, and thus it may be better
to first try adjusting the ``pool_recyle`` to ensure connections are closed and
reopened regularly.

... code-block:: python

    SQLALCHEMY_ENGINE_OPTIONS = dict(
        # enable the connection pool “pre-ping” feature that tests connections
        # for liveness upon each checkout.
        pool_pre_ping=True,

        # the number of connections to allow in connection pool “overflow”,
        # that is connections that can be opened above and beyond the
        # pool_size setting
        max_overflow=10,

        # the number of connections to keep open inside the connection
        pool_size=5,

        # recycle connections after the given number of seconds has passed.
        pool_recycle=3600,

        # number of seconds to wait before giving up on getting a connection
        # from the pool
        pool_timeout=30,

    )

See https://docs.sqlalchemy.org/en/latest/core/engines.html.
"""

# Redis (cache)
# ========
# Cache or Redis configurations
RATELIMIT_AUTHENTICATED_USER = "25000 per hour;1000 per minute"
"""Increase defaults for authenticated users."""

RATELIMIT_GUEST_USER = "5000 per hour;500 per minute"
"""Increase defaults for guest users."""

SESSION_COOKIE_SAMESITE = "Strict"
"""Sets cookie with the samesite flag to 'Strict' by default."""

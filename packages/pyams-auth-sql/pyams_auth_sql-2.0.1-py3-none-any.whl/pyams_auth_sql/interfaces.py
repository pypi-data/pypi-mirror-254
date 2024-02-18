#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_auth_sql.interfaces module

"""

from zope.interface import Attribute, Interface
from zope.schema import Bool, Choice, TextLine

from pyams_alchemy.interfaces import ALCHEMY_ENGINES_VOCABULARY
from pyams_security.interfaces.plugin import IAuthenticationPlugin, IDirectorySearchPlugin

from pyams_auth_sql import _


class ISQLUserInfo(Interface):
    """SQL user information interface"""

    principal_id = Attribute("User principal ID")

    attributes = Attribute("User entry attributes")

    plugin = Attribute("SQL authentication plug-in")


SQL_AUTH_PLUGIN_LABEL = _("SQL authentication plug-in")


class ISQLAuthPlugin(IAuthenticationPlugin, IDirectorySearchPlugin):
    """SQL authentication plug-in interface"""

    sql_engine = Choice(title=_("SQL engine"),
                        description=_("SQLAlchemy engine used for database connection"),
                        vocabulary=ALCHEMY_ENGINES_VOCABULARY,
                        required=True)

    schema_name = TextLine(title=_("Schema name"),
                           description=_("Database schema name"),
                           required=False)

    table_name = TextLine(title=_("Table name"),
                          description=_("Users table name"),
                          required=True,
                          default='users')

    login_attribute = TextLine(title=_("Login field name"),
                               description=_("Field name used to store login information"),
                               required=True,
                               default='login')

    password_attribute = TextLine(title=_("Password field name"),
                                  description=_("Field name used to store encoded password"),
                                  required=True,
                                  default='password')

    title_format = TextLine(title=_("Title format"),
                            description=_("Principal's title format string"),
                            required=True,
                            default='{name}')

    search_attributes = TextLine(title=_("Search attributes"),
                                 description=_("Users will be searched against these attributes, "
                                               "which can be provided by separating them with "
                                               "commas; login attribute is automatically "
                                               "selected"),
                                 required=False,
                                 default='login,name')

    login_with_email = Bool(title=_("Allow login with email"),
                            description=_("If 'yes', users can log in using their email "
                                          "address or their base login"),
                            required=True,
                            default=False)

    mail_attribute = TextLine(title=_("Email field name"),
                              description=_("Field name used to store email address"),
                              required=True,
                              default='email')

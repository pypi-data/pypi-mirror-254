#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_auth_sql.plugin module

This module defines the main SQL authentication plug-in.
"""

import logging

from persistent import Persistent
from sqlalchemy import text
from zope.container.contained import Contained
from zope.interface import implementer
from zope.password.interfaces import IPasswordManager
from zope.schema.fieldproperty import FieldProperty

from pyams_alchemy.engine import get_user_session
from pyams_auth_sql.interfaces import ISQLAuthPlugin, ISQLUserInfo
from pyams_mail.interfaces import IPrincipalMailInfo
from pyams_security.interfaces.names import PRINCIPAL_ID_FORMATTER
from pyams_security.principal import PrincipalInfo
from pyams_utils.adapter import ContextAdapter, adapter_config
from pyams_utils.factory import factory_config
from pyams_utils.registry import get_utilities_for


__docformat__ = 'restructuredtext'


LOGGER = logging.getLogger('PyAMS (SQL auth)')


@implementer(ISQLUserInfo)
class SQLUserInfo:
    """SQL user information"""

    def __init__(self, principal_id, attributes, plugin=None):
        self.principal_id = principal_id
        self.attributes = attributes
        self.plugin = plugin


@adapter_config(required=ISQLUserInfo, provides=IPrincipalMailInfo)
class SQLUserMailInfoAdapter(ContextAdapter):
    """SQL user mail adapter"""

    def get_addresses(self):
        """Get mail address of given user"""
        user = self.context
        plugin = user.plugin
        mail = getattr(user.attributes, plugin.mail_attribute)
        if mail:
            return {(plugin.title_format.format(**user.attributes._mapping), mail)}
        return set()


@factory_config(ISQLAuthPlugin)
class SQLAuthPlugin(Persistent, Contained):
    """SQL authentication plug-in"""

    prefix = FieldProperty(ISQLAuthPlugin['prefix'])
    title = FieldProperty(ISQLAuthPlugin['title'])
    enabled = FieldProperty(ISQLAuthPlugin['enabled'])

    sql_engine = FieldProperty(ISQLAuthPlugin['sql_engine'])
    schema_name = FieldProperty(ISQLAuthPlugin['schema_name'])
    table_name = FieldProperty(ISQLAuthPlugin['table_name'])
    login_attribute = FieldProperty(ISQLAuthPlugin['login_attribute'])
    password_attribute = FieldProperty(ISQLAuthPlugin['password_attribute'])
    title_format = FieldProperty(ISQLAuthPlugin['title_format'])
    search_attributes = FieldProperty(ISQLAuthPlugin['search_attributes'])
    login_with_email = FieldProperty(ISQLAuthPlugin['login_with_email'])
    mail_attribute = FieldProperty(ISQLAuthPlugin['mail_attribute'])

    def check_password(self, entry, password):
        """Check encoded password with provided password"""
        encoded = getattr(entry, self.password_attribute)
        for _, manager in get_utilities_for(IPasswordManager):
            try:
                result = manager.checkPassword(encoded, password)
                if result:
                    return True
            except:  # pylint: disable=bare-except
                pass
        return None

    def authenticate(self, credentials, request):  # pylint: disable=unused-argument
        """Authenticate provided credentials"""
        if not self.enabled:
            return None
        attrs = credentials.attributes
        login = attrs.get('login').lower()
        password = attrs.get('password')
        engine = get_user_session(self.sql_engine)
        query = text(
            "select * from {}{} where lower({}) = :login {}".format(
                f'{self.schema_name}.' if self.schema_name else '',
                self.table_name,
                self.login_attribute,
                f'or lower({self.mail_attribute}) = :login' if self.login_with_email else ''
            ))
        for entry in engine.execute(query, params={'login': login}):
            if not getattr(entry, self.password_attribute):
                continue
            if self.check_password(entry, password):
                return PRINCIPAL_ID_FORMATTER.format(prefix=self.prefix,
                                                     login=getattr(entry, self.login_attribute))
        return None

    def get_principal(self, principal_id, info=True):
        """Get principal info matching given principal ID"""
        if not self.enabled:
            return None
        if not principal_id.startswith(self.prefix + ':'):
            return None
        prefix, login = principal_id.split(':', 1)  # pylint: disable=unused-variable
        engine = get_user_session(self.sql_engine)
        sql = text(
            "select * from {}{} where {} = :login".format(
                f'{self.schema_name}.' if self.schema_name else '',
                self.table_name,
                self.login_attribute,
            ))
        for entry in engine.execute(sql, params={'login': login}):
            principal_id = PRINCIPAL_ID_FORMATTER.format(prefix=self.prefix,
                                                         login=getattr(entry, self.login_attribute))
            if info:
                return PrincipalInfo(
                    id=principal_id,
                    title=self.title_format.format(**entry._mapping))
            return SQLUserInfo(principal_id, entry, self)
        return None

    def get_all_principals(self, principal_id):
        """Get all principals for given principal ID"""
        if not self.enabled:
            return set()
        if self.get_principal(principal_id) is not None:
            return {principal_id}
        return set()

    def find_principals(self, query, exact_match=False):
        """Get iterator of principals matching given query"""
        if not self.enabled:
            return
        if not query:
            return
        query = query.lower()
        if not exact_match:
            query = '%{}%'.format(query)
        engine = get_user_session(self.sql_engine)
        sql = text(
            "select * from {}{} where lower({}) like :query {}".format(
                f'{self.schema_name}.' if self.schema_name else '',
                self.table_name,
                self.login_attribute,
                f'or lower({self.mail_attribute}) like :query' if self.login_with_email else ''
            ))
        for entry in engine.execute(sql, params={'query': query}):
            yield PrincipalInfo(
                id=PRINCIPAL_ID_FORMATTER.format(prefix=self.prefix,
                                                 login=getattr(entry, self.login_attribute)),
                title=self.title_format.format(**entry._mapping))

    def get_search_results(self, data):
        """Search results getter"""
        query = data.get('query')
        if not query:
            return
        query = '%{}%'.format(query.lower())
        engine = get_user_session(self.sql_engine)
        sql = text(
            "select * from {}{} where lower({}) like :query {}".format(
                f'{self.schema_name}.' if self.schema_name else '',
                self.table_name,
                self.login_attribute,
                'or ' + ' or '.join((
                    f'lower({attr}) like :query'
                    for attr in self.search_attributes.split(',')
                )) if self.search_attributes else ''
            ))
        yield from engine.execute(sql, params={'query': query})

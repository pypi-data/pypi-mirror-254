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

"""PyAMS_auth_sql.zmi module

This module provides management interface components.
"""

from pyams_auth_sql.interfaces import ISQLAuthPlugin, SQL_AUTH_PLUGIN_LABEL
from pyams_form.ajax import ajax_form_config
from pyams_layer.interfaces import IPyAMSLayer
from pyams_pagelet.pagelet import pagelet_config
from pyams_security.interfaces import ISecurityManager
from pyams_security.interfaces.base import MANAGE_SECURITY_PERMISSION
from pyams_security_views.zmi import SecurityPluginsTable
from pyams_security_views.zmi.plugin import SecurityPluginAddForm, SecurityPluginAddMenu, \
    SecurityPluginPropertiesEditForm
from pyams_table.column import GetAttrColumn
from pyams_table.interfaces import IColumn, IValues
from pyams_utils.adapter import ContextRequestViewAdapter, adapter_config
from pyams_utils.registry import get_utility
from pyams_utils.url import absolute_url
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.interfaces import IAdminLayer
from pyams_zmi.interfaces.viewlet import IContextAddingsViewletManager
from pyams_zmi.search import SearchForm, SearchResultsView, SearchView
from pyams_zmi.table import I18nColumnMixin, Table


__docformat__ = 'restructuredtext'

from pyams_auth_sql import _  # pylint: disable=ungrouped-imports


@viewlet_config(name='add-sql-auth-plugin.menu',
                context=ISecurityManager, layer=IAdminLayer, view=SecurityPluginsTable,
                manager=IContextAddingsViewletManager, weight=50,
                permission=MANAGE_SECURITY_PERMISSION)
class SQLAuthPluginAddMenu(SecurityPluginAddMenu):
    """SQL authentication plug-in add menu"""

    label = _("Add SQL authentication plugin...")
    href = 'add-sql-auth-plugin.html'


@ajax_form_config(name='add-sql-auth-plugin.html',
                  context=ISecurityManager, layer=IPyAMSLayer,
                  permission=MANAGE_SECURITY_PERMISSION)
class SQLAuthPluginAddForm(SecurityPluginAddForm):
    """SQL authentication plug-in add form"""

    content_factory = ISQLAuthPlugin
    content_label = SQL_AUTH_PLUGIN_LABEL


@ajax_form_config(name='properties.html', context=ISQLAuthPlugin, layer=IPyAMSLayer)
class SQLAuthPluginPropertiesEditForm(SecurityPluginPropertiesEditForm):
    """SQL authentication plug-in properties edit form"""

    plugin_interface = ISQLAuthPlugin


#
# SQL authentication plug-in search view
#

class SQLAuthPluginSearchForm(SearchForm):  # pylint: disable=abstract-method
    """SQL authentication plug-in search form"""

    title = _("Users search form")

    @property
    def back_url(self):
        """Form back URL getter"""
        manager = get_utility(ISecurityManager)
        return absolute_url(manager, self.request, 'security-plugins.html')


@pagelet_config(name='search.html', context=ISQLAuthPlugin, layer=IPyAMSLayer,
                permission=MANAGE_SECURITY_PERMISSION)
class SQLAuthPluginSearchView(SearchView):
    """SQL authentication plug-in search view"""

    title = _("Users search form")
    search_form = SQLAuthPluginSearchForm


class SQLAuthPluginSearchResultsTable(Table):
    """SQL authentication plug-in search results table"""

    batch_size = 999


@adapter_config(required=(ISQLAuthPlugin, IAdminLayer, SQLAuthPluginSearchResultsTable),
                provides=IValues)
class SQLAuthPluginSearchResultsValues(ContextRequestViewAdapter):
    """SQL authentication plug-in search results values"""

    @property
    def values(self):
        """SQL authentication plug-in search table results getter"""
        yield from self.context.get_search_results({
            'query': self.request.params.get('form.widgets.query')
        })


@adapter_config(name='login',
                required=(ISQLAuthPlugin, IAdminLayer, SQLAuthPluginSearchResultsTable),
                provides=IColumn)
class SQLAuthPluginSearchLoginColumn(I18nColumnMixin, GetAttrColumn):
    """SQL authentication plug-in search login column"""

    i18n_header = _("Login")

    @property
    def attr_name(self):
        """Column attribute getter"""
        return self.context.login_attribute

    weight = 10


@adapter_config(name='name',
                required=(ISQLAuthPlugin, IAdminLayer, SQLAuthPluginSearchResultsTable),
                provides=IColumn)
class SQLAuthPluginSearchNameColumn(I18nColumnMixin, GetAttrColumn):
    """SQL authentication plug-in search name column"""

    i18n_header = _("Name")

    weight = 20

    def get_value(self, obj):
        """Column value getter"""
        return self.context.title_format.format(**obj)


@adapter_config(name='email',
                required=(ISQLAuthPlugin, IAdminLayer, SQLAuthPluginSearchResultsTable),
                provides=IColumn)
class SQLAuthPluginSearchEmailColumn(I18nColumnMixin, GetAttrColumn):
    """SQL authentication plug-in search email column"""

    i18n_header = _("Email")

    @property
    def attr_name(self):
        """Column attribute getter"""
        return self.context.mail_attribute

    weight = 30


@pagelet_config(name='search-results.html', context=ISQLAuthPlugin, layer=IPyAMSLayer,
                permission=MANAGE_SECURITY_PERMISSION, xhr=True)
class SQLAuthPluginSearchResultsView(SearchResultsView):
    """SQL authentication plug-in search results view"""

    table_label = _("Search results")
    table_class = SQLAuthPluginSearchResultsTable

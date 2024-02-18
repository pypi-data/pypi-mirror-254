================================
PyAMS SQL authentication package
================================

Introduction
------------

This extension package for PyAMS_security package provides authentication features using
an SQL database, using SQLAlchemy ORM and PyAMS_alchemy extension package.

    >>> import tempfile
    >>> tempdir = tempfile.mkdtemp()

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp(hook_zca=True)
    >>> config.registry.settings['zodbconn.uri'] = 'memory://'
    >>> config.registry.settings['pyams_alchemy.cleaner.timeout'] = 'off'

    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from cornice import includeme as include_cornice
    >>> include_cornice(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_site import includeme as include_site
    >>> include_site(config)
    >>> from pyams_security import includeme as include_security
    >>> include_security(config)
    >>> from pyams_skin import includeme as include_skin
    >>> include_skin(config)
    >>> from pyams_zmi import includeme as include_zmi
    >>> include_zmi(config)
    >>> from pyams_form import includeme as include_form
    >>> include_form(config)
    >>> from pyams_alchemy import includeme as include_alchemy
    >>> include_alchemy(config)
    >>> from pyams_auth_sql import includeme as include_auth_sql
    >>> include_auth_sql(config)

    >>> from pyams_site.generations import upgrade_site
    >>> request = DummyRequest()
    >>> app = upgrade_site(request)
    Upgrading PyAMS timezone to generation 1...
    Upgrading PyAMS security to generation 2...
    Upgrading PyAMS alchemy to generation 1...

    >>> dsn = 'sqlite:///{}/test.db?uri=true'.format(tempdir)

    >>> from pyams_alchemy.interfaces import IAlchemyEngineUtility
    >>> from pyams_alchemy.engine import AlchemyEngineUtility
    >>> engine = AlchemyEngineUtility(dsn=dsn, use_pool=False, twophase=False)
    >>> config.registry.registerUtility(engine, IAlchemyEngineUtility)

    >>> engine
    <pyams_alchemy.engine.AlchemyEngineUtility object at 0x...>

    >>> import transaction

    >>> from sqlalchemy.sql import text
    >>> from pyams_alchemy.engine import get_user_session
    >>> session = get_user_session("")
    >>> session
    <sqlalchemy.orm.session.Session object at 0x...>

    >>> _ = session.execute(text("drop table if exists USERS"))
    >>> _ = session.execute(text("create table USERS (login varchar(255) primary key, \
    ...                                               name varchar(255), \
    ...                                               password varchar(255), \
    ...                                               email varchar(255))"))

    >>> from zope.password.interfaces import IPasswordManager
    >>> passmngr = config.registry.getUtility(IPasswordManager, name='PBKDF2')
    >>> password = passmngr.encodePassword('This is my password')
    >>> password
    b'{PBKDF2}...'

    >>> from sqlalchemy import Column, Unicode
    >>> from pyams_alchemy import Base

    >>> class User(Base):
    ...     __tablename__ = 'USERS'
    ...     login = Column(Unicode, primary_key=True)
    ...     name = Column(Unicode)
    ...     password = Column(Unicode)
    ...     email = Column(Unicode)

    >>> from sqlalchemy import text

    >>> user = User(login='test', name='Test user', password=password.decode(), email='john.doe@example.com')
    >>> session.add(user)

    >>> user2 = User(login='login2', name='Test user 2', password=None)
    >>> session.add(user2)

    >>> transaction.commit()

    >>> list(session.execute(text("select count(*) from USERS")))
    [(2,)]


As our database is now containing a user record, we can try to authenticate using it:

    >>> from pyams_auth_sql.plugin import SQLAuthPlugin
    >>> plugin = SQLAuthPlugin()
    >>> plugin.prefix = 'sql'
    >>> plugin.sql_engine = ''
    >>> plugin.table_name = 'USERS'
    >>> plugin.login_attribute = 'login'
    >>> plugin.password_attribute = 'password'
    >>> plugin.search_attributes = 'login,name'
    >>> plugin.title_format = '{name}'
    >>> plugin.login_with_email = True
    >>> plugin.mail_attribute = 'email'
    >>> plugin.enabled = False

    >>> from pyams_security.credential import Credentials

At first, disabled plug-in can't be used for authentication of to find principals:

    >>> credentials = Credentials(prefix='http',
    ...                           id='sql:test',
    ...                           login='test',
    ...                           password='This is my password')
    >>> plugin.authenticate(credentials, request=None) is None
    True

    >>> plugin.get_principal('sql:test') is None
    True

    >>> plugin.get_all_principals('sql:test')
    set()

    >>> list(plugin.find_principals('user'))
    []

Let's now activate our plug-in and test it's features:

    >>> plugin.enabled = True

We can't authenticate using a bad password:

    >>> credentials = Credentials(prefix='http',
    ...                           id='sql:test',
    ...                           login='test',
    ...                           password='This is a bad password')
    >>> plugin.authenticate(credentials, request=None) is None
    True

We can't authenticate also for a principal on which no password is set:

    >>> credentials = Credentials(prefix='http',
    ...                           id='sql:login2',
    ...                           login='login2',
    ...                           password=None)
    >>> plugin.authenticate(credentials, request=None) is None
    True

A good login and password are required to authenticate:

    >>> credentials = Credentials(prefix='http',
    ...                           id='sql:test',
    ...                           login='test',
    ...                           password='This is my password')
    >>> plugin.authenticate(credentials, request=None)
    'sql:test'

As we activated login with email address, this should be OK:

    >>> credentials = Credentials(prefix='http',
    ...                           id='sql:test',
    ...                           login='john.doe@example.com',
    ...                           password='This is my password')
    >>> plugin.authenticate(credentials, request=None)
    'sql:test'

We can also try to get principals from IDs:

    >>> plugin.get_principal('unknown') is None
    True
    >>> plugin.get_principal('sql:unknown') is None
    True
    >>> principal = plugin.get_principal('sql:test')
    >>> principal
    <pyams_security.principal.PrincipalInfo object at 0x...>
    >>> principal.id
    'sql:test'
    >>> principal.title
    'Test user'

    >>> principal = plugin.get_principal('sql:test', False)
    >>> principal
    <pyams_auth_sql.plugin.SQLUserInfo object at 0x...>
    >>> principal.principal_id
    'sql:test'
    >>> principal.attributes
    ('test', 'Test user', '{PBKDF2}...', 'john.doe@example.com')

    >>> plugin.get_all_principals('unknown')
    set()
    >>> plugin.get_all_principals('sql:unknown')
    set()
    >>> plugin.get_all_principals('sql:test')
    {'sql:test'}


Principal mail info
-------------------

    >>> from pyams_mail.interfaces import IPrincipalMailInfo
    >>> mail_info = IPrincipalMailInfo(principal)
    >>> mail_info
    <pyams_auth_sql.plugin.SQLUserMailInfoAdapter object at 0x...>
    >>> mail_info.get_addresses()
    {('Test user', 'john.doe@example.com')}


Searching for principals
------------------------

The "find_principals" method is used by principals input widgets:

    >>> list(plugin.find_principals(''))
    []
    >>> list(plugin.find_principals('unknown'))
    []
    >>> principals = list(plugin.find_principals('test'))
    >>> principals
    [<pyams_security.principal.PrincipalInfo object at 0x...>]
    >>> principals[0].id
    'sql:test'

The "get_search_results" method is used by plugin management interface:

    >>> list(plugin.get_search_results({}))
    []
    >>> list(plugin.get_search_results({'query': 'unknown'}))
    []
    >>> principals = list(plugin.get_search_results({'query': 'user'}))
    >>> len(principals)
    2
    >>> sorted(principals)
    [('login2', 'Test user 2', None, None), ('test', 'Test user', '{PBKDF2}...', 'john.doe@example.com')]


Tests cleanup:

    >>> tearDown()

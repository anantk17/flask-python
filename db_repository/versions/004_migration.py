from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
    Column('name', String(length=60)),
    Column('branch', String(length=2)),
    Column('batch', String(length=2)),
    Column('bcode', String(length=10)),
    Column('sem', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['batch'].create()
    post_meta.tables['user'].columns['bcode'].create()
    post_meta.tables['user'].columns['branch'].create()
    post_meta.tables['user'].columns['name'].create()
    post_meta.tables['user'].columns['sem'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['batch'].drop()
    post_meta.tables['user'].columns['bcode'].drop()
    post_meta.tables['user'].columns['branch'].drop()
    post_meta.tables['user'].columns['name'].drop()
    post_meta.tables['user'].columns['sem'].drop()

#-*- coding: utf8 -*-

# webapi
#  /usr/bin/python /usr/bin/supervisord -c /home/python/conf/supervisord.conf
SUPERVISORCTL = '/usr/bin/python /usr/bin/supervisorctl'
SUPERVISOR_CONF_FILE = '/home/python/conf/supervisord.conf'
DEBUG = True
AUTH_KEY = 'oDerVOA0Dfh6qAk5J'
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 5000

DATABASES = {
    # MYSQL 数据库参数
    'mysql': {
        'edm_web': {
            'host': '202.103.191.7',
            'port': 3306,
            'user': 'edm_web',
            'passwd': 'XnLaT34LxaQViNB',
            'db': 'mm-ms',
        },
        'test': {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': 'XnLaT34LxaQViNB',
            'db': 'test',
        },
    },

    # PgSQL 数据库参数
    'postgresql': {
        'mail_relay': {
            'host': '127.0.0.1',
            'port': 5432,
            'user': 'postgres',
            'password': '123456',
            'dbname': 'mail_relay',
        },
    },

    # Mongo 配置
    'mongo': {
        'mongo': {
            'host': '127.0.0.1',
            'port': 27017,
            'user': 'sa',
            'pass': 'sa',
            'dbname': 'admin',
        },
    }
}

# redis 配置
REDIS_SET = {
    'host': '127.0.0.1',
    'port': 6379,
}

# Mongo 配置
MONGODB_SET = {
    'host': '127.0.0.1',
    'port': 27017,
    'user': 'sa',
    'pass': 'sa',
    'dbname': 'admin',
}

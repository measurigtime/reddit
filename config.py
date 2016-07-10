import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '250448028671566',
        'secret': '5174e8be613f65596dbf0f7ae01160e0'
    },
    'twitter': {
        'id': 'ghoozQUbTo6NN7CBbvqtCtuqk',
        'secret': 'gabiYlkM7DOa4Vgz61TUlUB0MWFCzmUBxzMWrmDrPDGLxR3RSm'
    }
}

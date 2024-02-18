import os
import viggocore

from viggocore.system import System
from flask_cors import CORS
from viggopayfac.resources import SYSADMIN_EXCLUSIVE_POLICIES, \
    SYSADMIN_RESOURCES, USER_RESOURCES
from viggopayfac.packages import packages


system = System('viggopayfac',
                packages,
                USER_RESOURCES,
                SYSADMIN_RESOURCES,
                SYSADMIN_EXCLUSIVE_POLICIES)


class SystemFlask(viggocore.SystemFlask):

    def __init__(self):
        super().__init__(system)

    def configure(self):
        origins_urls = os.environ.get('ORIGINS_URLS', '*')
        CORS(self, resources={r'/*': {'origins': origins_urls}})

        self.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        viggopayfac_database_uri = os.getenv('viggopayfac_DATABASE_URI', None)
        if viggopayfac_database_uri is None:
            raise Exception('viggopayfac_DATABASE_URI not defined in enviroment.')
        else:
            # URL os enviroment example for Postgres
            # export viggopayfac_DATABASE_URI=
            # mysql+pymysql://root:mysql@localhost:3306/viggopayfac
            self.config['SQLALCHEMY_DATABASE_URI'] = viggopayfac_database_uri

'''
Connect to SQL Databases.

Copyright (C) 2023 Nat Hawkins & Mike Chappelow

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3 of the License)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


# Imports
import os
import pyodbc
from plinko.configurations import configure_username
from plinko.zoltar import zoltar_ask


def plinko_sql(environment, database, server = None):
    '''
    Access and connect to SQL database in specified environment
    
    Parameters
    ----------
    environment: str
        SQL Environment to access, can be either DEV or PROD
    database: str
        Database within SQL to access
    server: str (optional)
        Custom server to use rather than default MS SQL Server locations
        
    Returns
    -------
    pyodbc.connect
        If connection can be established using pyodbc.connect(), a pyodbc.connect() object
        will be returned. This can be passed to pandas (e.g., pd.read_sql) or similar libraries
        for reading remote data. If a connection cannot be established, None will be returned
    '''
    # Check for configuration of environment variables
    if os.getenv("CONNECT_API_KEY") is None: configure_username()
    
    # Determine driver to use for connection
    available_drivers = pyodbc.drivers()
    
    # Default to freetds for full functionality, otherwise use SQLServer/SQL Server
    if 'freetds' in available_drivers:
        unsupported_service_accounts_present = False
        driver = 'freetds'
    else:
        unsupported_service_accounts_present = True
        if 'SQL Server' in available_drivers:
            driver = 'SQL Server'
        else:
            driver = 'SQLServer'
    
    # Specified custom server
    if server is not None:
        server_val = server
        
        # Custom server DEV
        if environment == "DEV":
            if "USAWSCWSQL5066" in server.upper():
                uid = zoltar_ask("USAWSCWSQL5066_DEV_userid")
                pwd = zoltar_ask("USAWSCWSQL5066_DEV_pwd")
                
        # Custom server PROD
        elif environment == "PROD":
            if database.upper() == "KG_ANALYTICS_APPS":
                if "USAWSCWSQL0066" in server.upper():
                    uid = zoltar_ask("Usawscwsql0066_KG_ANALYTICS_APPS_PROD_uid")
                    pwd = zoltar_ask("Usawscwsql0066_KG_ANALYTICS_APPS_PROD_pwd")
                else:
                    uid = zoltar_ask("Usawscwsql0066_KG_SAS_PROD_userid")
                    pwd = zoltar_ask("Usawscwsql0066_KG_SAS_PROD_pwd")
        
        # Cannot connect
        else:
            print("Unknown request, please contact Data Science team for support.")
            return None
    
    # Default server DEV
    elif environment == "DEV":
        server_val = zoltar_ask("MS_SQL_ANALYTICS_DEV_server")
        
        if database in ["KG_R_APPS", "KNA_FIN"]:
            if unsupported_service_accounts_present:
                print("Due to your available ODBC drivers, this service account cannot be utilized.")
                return None
            uid = zoltar_ask("KG_R_APPS_DEV_userid")
            pwd = zoltar_ask("KG_R_APPS_DEV_pwd")
            
        elif database in ["KG_SAS", "KG_SC", "KG_EXTERNAL", "KNA_ECC", "KG_SANDBOX", "KG_MEMSQL", "KG_VIEWS"]:
            uid = zoltar_ask("KG_SAS_DEV_userid")
            pwd = zoltar_ask("KG_SAS_DEV_pwd")
        
        elif database in ["KG_SAS_WRITE"]:
            database = "KG_SAS" 
            uid = zoltar_ask("KG_SAS_DEV_WRITE_uid")
            pwd = zoltar_ask("KG_SAS_DEV_WRITE_pwd")
        
        elif database in ["KG_ANALYTICS_APPS", "WKKC_K_ANALYTICS_APPS"]:
            uid = zoltar_ask("KG_ANALYTICS_APPS_DEV_userid")
            pwd = zoltar_ask("KG_ANALYTICS_APPS_DEV_pwd")
            
        else:
            uid = zoltar_ask("KG_SAS_DEV_userid")
            pwd = zoltar_ask("KG_SAS_DEV_pwd")
        
    # Default server PROD
    elif environment == "PROD":
        server_val = zoltar_ask("MS_SQL_ANALYTICS_PROD_server")
        
        if database in ["KG_R_APPS", "KNA_FIN"]:
            if unsupported_service_accounts_present:
                print("Due to your available ODBC drivers, this service account cannot be utilized.")
                return None
            uid = zoltar_ask("KG_R_APPS_PROD_userid")
            pwd = zoltar_ask("KG_R_APPS_PROD_pwd")
            
        elif database in ["KG_SAS", "KG_SC", "KG_EXTERNAL", "KNA_ECC", "KG_SANDBOX", "KG_MEMSQL", "KG_VIEWS"]:
            uid = zoltar_ask("KG_SAS_PROD_userid")
            pwd = zoltar_ask("KG_SAS_PROD_pwd")
            
        elif database in ["KG_SAS_WRITE"]:
            database = "KG_SAS" 
            uid = zoltar_ask("KG_SAS_PROD_WRITE_uid")
            pwd = zoltar_ask("KG_SAS_PROD_WRITE_pwd")
            
        elif database in ["KG_ANALYTICS_APPS", "WKKC_KG_ANALYTICS_APPS"]:
            uid = zoltar_ask("KG_ANALYTICS_APPS_PROD_userid")
            pwd = zoltar_ask("KG_ANALYTICS_APPS_PROD_pwd")
            
        else:
            uid = zoltar_ask("KG_SAS_PROD_userid")
            pwd = zoltar_ask("KG_SAS_PROD_pwd")
        
    # Cannot connect
    else:
        print("Could not establish connect with given parameters, please try again.")
        return None
        
    # Create connection
    cnxn = pyodbc.connect(f'Driver={{{driver}}};',
                          Server = server_val,
                          Database = database,
                          User = uid,
                          Password = pwd,
                          Encrypt = 'yes',
                          Trusted_Connection = 'no')
    return cnxn

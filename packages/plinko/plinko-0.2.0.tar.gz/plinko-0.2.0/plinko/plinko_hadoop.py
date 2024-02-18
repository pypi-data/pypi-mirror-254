'''
Connect to Hadoop Server.

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
from plinko.zoltar import zoltar_ask
from plinko.configurations import configure_username


def plinko_hadoop(environment, schema):
    '''
    Connect to Hadoop server using ODBC Hive driver
    
    Parameters
    ----------
    environment: str
        String denoting Hadoop server to connect to, can be either DEV or PROD
    schema: str
        Database/schema in Hadoop server to access
        
    Returns
    -------
    pyodbc.connect  
        If connection can be established using pyodbc.connect(), a pyodbc.connect() object
        will be returned. This can be passed to pandas (e.g., pd.read_sql) or similar libraries
        for reading remote data. If a connection cannot be established, None will be returned
    '''
    # Check for environment variable
    if os.getenv("CONNECT_API_KEY") is None: configure_username()
    
    # Check for Hive drivers
    if 'Hive' not in pyodbc.drivers():
        print("Your system currently lacks the necessary Hive driver for connecting to Hadoop.")
        return None
        
    # Get service account credentials
    username = zoltar_ask(f'{environment}_HADOOP_userid')
    password = zoltar_ask(f'{environment}_HADOOP_pwd')

    # Run kerboros authentication
    kerboros_status = os.system(f"kinit {username} <<< {password}")
    if kerboros_status != 0:
        print("Kerboros authentication failed.")
        return None

    # Get Hadoop server information
    host = zoltar_ask(f'{environment}_HADOOP_server')
    port = zoltar_ask(f'{environment}_HADOOP_port')
    
    # Identify SSl certificate location for environment
    if os.getenv("CONNECT_SERVER_TYPE") == "PROD":
        if os.getenv("CONNECT_SERVER") == "https://prod.positconnect.analytics.kellogg.com":
            ssl_cert = "/usr/rstudio_prod/serverpro/certs/hive_prod.pem"
        else:
            ssl_cert = "/usr/rstudio/serverpro/certs/hive_prod.pem"
    else:
        ssl_cert = "/usr/rstudio2/serverpro/certs/hive.pem"
    
    # Connect
    cnxn = pyodbc.connect("DRIVER={Hive};" +
                          f"HOST={host};PORT={port};DATABASE={schema};"+
                          "ZKNamespace=None;"+
                          "AuthMech=1;"+
                          "ServiceDiscoveryMode=0;"+
                          "HiveServerType=2;"+
                          "ThriftTransport=2;"+
                          "SSL=1;"+
                          f"ClientCert={ssl_cert};"+
                          "AllowSelfSignedServerCert=1;"+
                          "HttpPathPrefix=/cliservice",
                          autocommit = True)
    return cnxn
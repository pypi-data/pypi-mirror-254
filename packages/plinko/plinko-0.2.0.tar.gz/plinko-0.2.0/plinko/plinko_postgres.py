'''
Connect to Postgres Databases.

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


def plinko_postgres(environment, database, server = None):
    '''
    Connect to Postgres SQL Database

    Parameters
    ----------
    environment: str
        Postgres SQL environment to connect to
    database: str
        Specify database in environment to connect to
    server: str (optional)
        Specify server to use when connection to Postgres SQL. If None, server information is
        determined based on environment and database parameters

    Returns
    -------
    pyodbc.connect
        If connection can be established using pyodbc.connect(), a pyodbc.connect() object
        will be returned. This can be passed to pandas (e.g., pd.read_sql) or similar libraries
        for reading remote data. If a connection cannot be established, None will be returned
    '''
    # Check for environment variable configurations
    if os.getenv("CONNECT_API_KEY") is None: configure_username()

    # DEV
    if environment.upper() == "DEV":
        if server is None:
            server = zoltar_ask("POSTGRES_DEV_server")
        
        port = zoltar_ask("POSTGRES_DEV_port")
        uid  = zoltar_ask("POSTGRES_DEV_uid")
        pwd  = zoltar_ask("POSTGRES_DEV_pwd")

    # PROD
    elif environment.upper() == "PROD":
        print("PROD credentials are not currently supported")
        return None

    else:
        print("Please specify PROD or DEV as your environment.")
        return None

    # Establish connection
    cnxn = pyodbc.connect(Driver = 'postgresql',
                          Server = server,
                          Port = port,
                          Database = database,
                          UID = uid, 
                          PWD = pwd,
                          BoolAsChar = "",
                          timeout = 10)

    return cnxn
'''
Connect to Amazon Redshift Databases.

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


def plinko_redshift(environment, region = 'KNA',
                    database = None, server = None):
    '''
    Connect to AWS Redshift databases in Kortex

    Parameters
    ----------
    environment: str
        Kortex environment to connect to (DEV, PROD, QA)
    region: str
        Regional redshift instance to connect to. Can be 'kna', 'keu', 'kamea'
        Default 'kna'
    database: str (optional)
        Specify database to connect to in Kortex environment. If None, REDSHIFT_default_database
        information is pulled from zoltar
    server: str (optional)
        Specify custom server to connect to in Kortex environment. If None, server is determined
        based on environment

    Returns
    -------
    pyodbc.connect
        If connection can be established using pyodbc.connect(), a pyodbc.connect() object
        will be returned. This can be passed to pandas (e.g., pd.read_sql) or similar libraries
        for reading remote data. If a connection cannot be established, None will be returned
    '''
    # Check for environment variable configurations
    if os.getenv("CONNECT_API_KEY") is None: configure_username()

    # Correct user input for AMEA
    if region.lower() in ['kamea', 'kap']: region = 'AMEA'

    # Query relevant information from zoltar
    redshift_id = f'REDSHIFT_{region.upper()}_{environment.upper()}'
    server_id   = f'{redshift_id}_server'
    port_id     = f'{redshift_id}_port'
    uid_id      = f'{redshift_id}_uid'
    pwd_id      = f'{redshift_id}_pwd'

    # Define database if none passed
    if database is None:
        if region == 'AMEA':
            database = 'klg_nga_kamea'
        else:
            database = f'klg_nga_{region.lower()}'

    # Establish connection
    cnxn = pyodbc.connect(Driver = 'redshift',
                          servername = zoltar_ask(server_id),
                          database = database,
                          UID = zoltar_ask(uid_id),
                          PWD = zoltar_ask(pwd_id),
                          Port = zoltar_ask(port_id))

    return cnxn
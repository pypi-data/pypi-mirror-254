'''
Query the Deployed Connect API for all Available Zoltar Credentials.

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
import pandas as pd
from plinko.plinko_sql import plinko_sql
from plinko.configurations import configure_username
 
def zoltar_list():
    '''
    Get list of all available credentials in Zoltar API
    
    Parameters
    ----------
    None
    
    Returns
    -------
    pandas.data.frame
        pandas.data.frame object containing all available credentials in Zoltar API
    '''
    # Check for environment variables
    if os.getenv("CONNECT_USER_LOCKED") is None: configure_username()
    
    # Check if user is locked
    if os.getenv("CONNECT_USER_LOCKED") == "True" or os.getenv("CONNECT_USER_LOCKED") is None:
        return None
        
    # TODO: Add more robust user role checking and user-level permissions
    # for restricting super access to credentials
        
    # Connect to credentials table in SQL
    cnxn = plinko_sql("PROD", "KG_R_APPS")
    
    # Check to see if access can be established
    if cnxn is None:
        return None
        
    # Return credentials
    return pd.read_sql("SELECT * FROM dbo.zoltar_list", cnxn)
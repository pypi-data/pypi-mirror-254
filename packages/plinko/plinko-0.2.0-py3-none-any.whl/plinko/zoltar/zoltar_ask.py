'''
Query the Deployed Connect API for Zoltar Credential.

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
from plinko.configurations import configure_username
from plinko.configurations import configure_environment

def zoltar_ask(wish):
    '''
    Query Zoltar API for secure credential by passing "Wish" to connect_server
    
    Parameters
    ----------
    wish : str
        String identifier to query Zoltar API with
        
    Returns
    -------
    str
        Result from Zoltar API query
    '''
    # Check for environment configuration
    if os.getenv("CONNECT_API_KEY") is None: configure_username()

    # Check for connect server configuration
    if os.getenv("CONNECT_SERVER") is None: configure_environment()
    
    # Query API
    curl = f'''curl -s -X GET {os.getenv("CONNECT_SERVER")}/zoltar/wish?wish={wish} -H "Authorization: Key {os.getenv('CONNECT_API_KEY')}" -H "accept: */*"'''
    x    = os.popen(curl).read()
    
    # Return query result
    return eval(x)[0]

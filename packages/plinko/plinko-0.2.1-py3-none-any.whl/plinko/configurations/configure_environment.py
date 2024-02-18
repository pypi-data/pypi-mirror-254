'''
Configuration to determine environment user is operating in.

Copyright (C) 2024 Nat Hawkins & Mike Chappelow

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

def configure_environment():
    '''
    Add CONNECT_SERVER to environment variables in order to authenticate 
    to Connect servers and call proper zoltar API endpoint. Also sets
    CONNECT_SERVER_TYPE to either PROD or DEV to control downstream flows.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    int
        1 if CONNECT_SERVER and CONNECT_SERVER_TYPE environment variables can be set, 
            else 0
    '''
    # Check to ensure environment is not set
    if (not os.getenv("CONNECT_SERVER") is None) and (not os.getenv("CONNECT_SERVER_TYPE") is None):
        return 0

    # Check for hostname
    hostname_ = os.popen('hostname').read().strip()

    # Verify server and set environment accordingly
    connect_server_      = None
    connect_server_type_ = None

    # Kortex environment - DEV
    if hostname_ in ['usaws3320', 'usaws3321', 'usaws3322', 'usaws3323']:
        connect_server_      = "https://dev.positconnect.analytics.kellogg.com"
        connect_server_type_ = "DEV"

    # Kortex environment - PROD
    if hostname_ in ["usaws1320", "usaws1321", "usaws1322", "usaws1323"]:
        connect_server_      = "https://prod.positconnect.analytics.kellogg.com"
        connect_server_type_ = "PROD"

    # Legacy environment - PROD
    if hostname_ in ["usaws1170", "usaws1171", "usaws1172", "usaws1173", "usaws1174", "usaws1175"]:
        connect_server_      = "https://rstudioconnect.analytics.kellogg.com"
        connect_server_type_ = "PROD"

    # NOTE: Legacy environment - DEV is not supported
    if hostname_ in ["usaws3170", "usaws3171", "usaws3172", "usaws3173"]:
        raise NotImplementedError("Zoltar is currently not supported in this environment")

    # Default to Kortex environment - PROD for all other executions
    if (connect_server_ is None) and (connect_server_type_ is None):
        connect_server_      = "https://prod.positconnect.analytics.kellogg.com"
        connect_server_type_ = "PROD"

    # Set environment variables
    os.environ['CONNECT_SERVER']      = connect_server_
    os.environ['CONNECT_SERVER_TYPE'] = connect_server_type_

    # Check environment variables
    if (os.getenv("CONNECT_SERVER") == connect_server_) and (os.getenv("CONNECT_SERVER_TYPE") == connect_server_type_):
        return 1
    return 0
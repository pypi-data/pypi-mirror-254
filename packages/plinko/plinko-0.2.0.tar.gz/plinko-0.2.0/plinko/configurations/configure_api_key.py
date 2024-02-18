'''
Set CONNECT_API_KEY Environment Variable from .Renviron File.

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


def configure_api_key():
    '''
    Add CONNECT_API_KEY to $PATH in order to authenticate to Connect servers
    
    Parameters
    ----------
    None
    
    Returns
    -------
    int
        1 if CONNECT_API_KEY environment variable is located in a .Renviron 
        file either in current working directory or home directory, else 0
    '''
    # If environment variable is not set, os.getenv("<variable name>")
    # will return None. If it is not None, the API key is recognized
    # and set in the evironment.
    if not os.getenv("CONNECT_API_KEY") is None: return 0
    
    # If environment is not set, checks the current working directory and
    # home directory for a .Renviron file and read CONNECT_API_KEY from there
    for target_filename in [os.path.expanduser(os.getcwd() + "/.Renviron"), 
                            os.path.expanduser("~" + "/.Renviron")]:
        # Check file exists
        if not os.path.exists(target_filename): continue        
    
        # Read .Renviron file 
        with open(target_filename, "r") as f:
            # Find variable labeled CONNECT_API_KEY
            environment_variables = f.readlines()
            connect_api_key       = [_x for _x in environment_variables if "CONNECT_API_KEY" in _x]

        if len(connect_api_key) == 0: continue
        
        connect_api_key = connect_api_key[0].split("=")[-1].strip()
        if "'" in connect_api_key or '"' in connect_api_key: 
            connect_api_key = connect_api_key[1:-1]
        
        # Set environment variable 
        os.environ["CONNECT_API_KEY"] = connect_api_key
        return 0
                
    # At this point in the execution, no CONNECT_API_KEY has been found
    print("After checking your home directory and your current working directory, " \
          "there does not appear to be a .Renviron file with CONNECT_API_KEY present. " \
          "Please ensure file exists and contains an API key and try again.")
    return 1
    
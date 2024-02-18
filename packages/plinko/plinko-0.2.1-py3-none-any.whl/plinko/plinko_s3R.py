'''
Connect to Amazon AWS S3 Storage (Cold Storage).

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
import boto3
from plinko.zoltar import zoltar_ask
from plinko.configurations import configure_username


def plinko_s3R():
    '''
    Establish needed environment variables and global environment variables
    for connecting and reading/writing data to AWS S3 storage (Cold Storage)

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Dicitonary containing s3BucketName and connection object from boto3.client()
    '''
    # Check for API Key configuration
    if os.getenv("CONNECT_API_KEY") is None: configure_username()

    # Check for existing AWS S3 configuration information
    if os.getenv("AWS_SECRET_ACCESS_KEY") is not None: 
        print("You already have a defined S3 connection configured in your global environment.")
        print("You can only assume one role at a time. You must restart your session to connect to a different S3 storage location.")
        return None

    # Define configuration
    os.environ["AWS_ACCESS_KEY_ID"]     = zoltar_ask("aws_key")
    os.environ["AWS_SECRET_ACCESS_KEY"] = zoltar_ask("aws_secretkey") 
    os.environ["AWS_DEFAULT_REGION"]    = "us-east-1"

    # Return bucket name and session client for accessing data
    return {"s3BucketName": zoltar_ask("s3BucketName"), "conn": boto3.client("s3")} 
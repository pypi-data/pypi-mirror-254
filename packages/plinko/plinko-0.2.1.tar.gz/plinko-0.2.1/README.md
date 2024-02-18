# Python Link Operations with `plinko`

![](resource/plinko-hex-final.png)

Python equivalent to the [`klink`](https://github.com/mikechappelow/klink.git) package developed by Mike Chappelow to establish secure remote connections to external data sources using service account credentials.

## Installation

`plinko` can be installed by executing the following command from the Terminal window:

`pip install plinko`

## Examples

### `plinko_hadoop`

Given security constraints, Hadoop DEV can only be accessed from Workbench/Connect DEV, and Hadoop PROD from Workbench/Connect PROD.

```python
import pandas as pd
from plinko import plinko_hadoop

# First argument is the environment (PROD/DEV), the second argument is the schema
conn = plinko_hadoop("PROD", "default")

# Use functions such as pd.read_sql to execute queries by passing connection object
# Queries will execute for Hadoop databases as well as SQL databases
df = pd.read_sql("SELECT * FROM <table name>", conn)
```

### `plinko_postgres`

```python
import pandas as pd
from plinko import plinko_postgres

# Only DEV is currently supported, the second argument is the database
conn = plinko_hadoop("DEV", "default")

# Use functions such as pd.read_sql to execute queries by passing connection object
df = pd.read_sql("SELECT * FROM <table name>", conn)
```

### `plinko_redshift`

Curreently there is only a single Redshift instance supported by `plinko_redshift`.

```python
import pandas as pd
from plinko import plinko_redshift

# Only argument is used to designate the environment (PROD/DEV/QA)
conn = plinko_redshift("DEV")

# Use functions such as pd.read_sql to execute queries by passing connection object
df = pd.read_sql("SELECT * FROM <table name>", conn)
```

### `plinko_s3`

```python
from plinko import plinko_s3

# Returns a data dictionary with bucket name and client object from boto3 library
s3_connection_information = plinko_s3()

print(s3_connection_information['s3BucketName'])
s3_connection_information['conn'].get_object(Bucket = s3_connection_information['s3BucketName'], Key = '<name of object in S3>')
```

### `plinko_s3R`

```python
from plinko import plinko_s3R

# Returns a data dictionary with bucket name and client object from boto3 library
s3_connection_information = plinko_s3R()

print(s3_connection_information['s3BucketName'])
s3_connection_information['conn'].get_object(Bucket = s3_connection_information['s3BucketName'], Key = '<name of object in S3>')
```

### `plinko_sql`

```python
import pandas as pd
from plinko import plinko_sql

# First argument is the environment (PROD/DEV), the second argument is the database
conn = plinko_sql("DEV", "default")

# Use functions such as pd.read_sql to execute queries by passing connection object
df = pd.read_sql("SELECT * FROM <table name>", conn)
```

### Zoltar

Service account credentials are automatically managed by the various methods listed above. If you would like to access a specific credential for use in other programs, the following method can be called:

```python
from plinko.zoltar import zoltar_ask

zoltar_ask("<credential ID>")
```

To see available credential ID in Zoltar, the following method can be called:

```python
from plinko.zoltar import zoltar_list

zoltar_list()
```

As a note, not all users will be able to execute `zoltar_list()` depending on account-level permissions.

### Configurations

The various `plinko` connection methods will execute any necessary configurations for the user at runtime. To establish critical environment variables (e.g., `CONNECT_API_KEY`) outside of executing a `plinko` connection function, the following methods can be called:

```python
from plinko import configurations

# Looks for .Renviron file in current working directory and home directory,
# establishes CONNECT_API_KEY _only_
configure_api_key()

# Uses CONNECT_API_KEY to establish username as environment variable. If CONNECT_API_KEY
# not defined, will also execute configure_api_key()
configure_username()
```

## Development

### Want to Get Involved?

Feel free to file a [pull request](https://github.com/kelloggcompany/plinko/pulls)! Pull requests will be reviewed by repository admins prior to merging. All pull requests should include a thorough summary of changes and/or new functionalities. Please ensure no secure credentials are hard-coded in your code from testing as this will delay the merging process.

### Feature Request

To request a feature, please raise a [git issue](https://github.com/kelloggcompany/plinko/issues) and use the tag "enhancement."

### Something Wrong?

To report a bug, please raise a [git issue](https://github.com/kelloggcompany/plinko/issues) and use the tag "bug."

### Building and Depoloying

1. `python setup.py sdist bdist_wheel`   

2. `twine upload dist/*`

When deploying to `pypi`, API key should be used for secure deployment. Username: `__token__`, Password: `pypi-<API token>`. If 'pypi-' prefix is not included with API token, authentication will fail.

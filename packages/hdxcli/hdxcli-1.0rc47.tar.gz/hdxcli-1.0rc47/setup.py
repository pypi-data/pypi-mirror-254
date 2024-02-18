# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hdx_cli',
 'hdx_cli.cli_interface',
 'hdx_cli.cli_interface.common',
 'hdx_cli.cli_interface.dictionary',
 'hdx_cli.cli_interface.function',
 'hdx_cli.cli_interface.integration',
 'hdx_cli.cli_interface.job',
 'hdx_cli.cli_interface.migrate',
 'hdx_cli.cli_interface.pool',
 'hdx_cli.cli_interface.profile',
 'hdx_cli.cli_interface.project',
 'hdx_cli.cli_interface.role',
 'hdx_cli.cli_interface.set',
 'hdx_cli.cli_interface.sources',
 'hdx_cli.cli_interface.storage',
 'hdx_cli.cli_interface.stream',
 'hdx_cli.cli_interface.table',
 'hdx_cli.cli_interface.transform',
 'hdx_cli.cli_interface.user',
 'hdx_cli.library_api',
 'hdx_cli.library_api.common',
 'hdx_cli.library_api.ddl',
 'hdx_cli.library_api.ddl.extensions',
 'hdx_cli.library_api.userdata',
 'hdx_cli.library_api.utility']

package_data = \
{'': ['*'],
 'hdx_cli': ['ddl-files/clickhouse/*', 'ddl-files/ecs/*', 'ddl-files/sql/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pydantic>=2.5.3,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'sqlglot>=10.5.10,<11.0.0',
 'toml>=0.10.2,<0.11.0',
 'trogon>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['hdxcli = hdx_cli.main:main']}

setup_kwargs = {
    'name': 'hdxcli',
    'version': '1.0rc47',
    'description': 'Hydrolix command line utility to do CRUD operations on projects, tables, transforms and other resources in Hydrolix clusters',
    'long_description': '[![](images/hdxcli.png)](https://github.com/hydrolix/hdx-cli)\n\n\n`hdxcli` is a command-line tool to work with hydrolix projects and tables\ninteractively.\n\nCommon operations such as CRUD operations on projects/tables/transforms \nand others  can be performed.\n\n# Hdx-cli installation\n\nYou can install `hdxcli` from pip:\n\n```shell\npip install hdxcli\n```\n## System Requirements\nPython version `>= 3.10` is required.\n\nMake sure you have the correct Python version installed before proceeding \nwith the installation of `hdxcli`.\n\n# Usage\n\n## Command-line tool organization\n\nThe tool is organized, mostly with the general invocation form of:\n\n```shell\nhdxcli <resource> [<subresource...] <verb> [<resource_name>]\n```\n\nTable and project resources have defaults that depend on the profile\nyou are working with, so they can be omitted if you previously used \nthe `set` command.\n\nFor all other resources, you can use `--transform`, `--dictionary`, \n`--source`, etc. Please see the command line help for more information.\n\n## Profiles\n`hdxcli` supports multiple profiles. You can use a default profile or\nuse the `--profile` option to operate on a non-default profile.\n\nWhen trying to invoke a command, if a login to the server is necessary, \na prompt will be shown and the token will be cached.\n\n## Listing and showing profiles\n\nListing profiles:\n```shell\nhdxcli profile list\n```\n\nShowing default profile:\n```shell\nhdxcli profile show\n```\n\n## Projects, tables and transforms\n\nThe basic operations you can do with these resources are:\n\n- list them\n- create a new resource\n- delete an existing resource\n- modify an existing resource\n- show a resource in raw json format\n- show settings from a resource\n- write a setting\n- show a single setting\n\n## Working with transforms\n\nYou can create and override transforms with the following commands.\n\nCreate a transform:\n``` shell\nhdxcli transform create -f <transform-settings-file> <transform-name>\n```\n\nRemember that a transform is applied to a table in a project, so whatever \nyou set with the command-line tool will be the target of your transform.\n\n\nIf you want to override it, do:\n\n``` shell\nhdxcli --project <project-name> --table <table-name> transform create -f <transform-settings-file>.json <transform-name>\n```\n\n## Ingest\n### Batch Job\nCreate a batch job:\n\n``` shell\nhdxcli job batch ingest <job-name> <job-settings>.json\n```\n\n`job-name` is the name of the job that will be displayed when listing batch \njobs. `job-settings` is the path to the file containing the specifications \nrequired to create that ingestion (for more information on the required \nspecifications, see Hydrolix API Reference).\n\nIn this case, the project, table, and transform are being omitted and the \nCLI will use the default transform within the project and table previously \nconfigured in the profile with the `--set` command. Otherwise, you can add \n`--project <project-name>, --table <table-name> --transform <transform-name>`.\n\nThis allows you to execute the command as follows:\n``` shell\nhdxcli --project <project-name>, --table <table-name> --transform <transform-name> job batch ingest <job-name> <job-settings>.json\n```\n\n# Commands\n\n- Profile\n  - *list*\n    - `hdxcli profile list`\n  - *add*\n    - `hdxcli profile add <profile-name>`\n  - *show*\n    - `hdxcli --profile <profile-name> profile show`\n- Set/Unset\n  - *set*\n    - `hdxcli set <project-name> <table-name>`\n  - *unset*\n    - `hdxcli unset`\n- Project\n  - *list*\n    - `hdxcli project list`\n  - *create*\n    - `hdxcli project create <project-name>`\n  - *delete*\n    - `hdxcli project delete <project-name>`\n  - *activity*\n    - `hdxcli --project <project-name> project activity`\n  - *stats*\n    - `hdxcli --project <project-name> project stats`\n  - *show*\n    - `hdxcli --project <project-name> project show`\n  - *settings*\n    - `hdxcli --project <project-name> project settings`\n    - `hdxcli --project <project-name> project settings <setting-name>`\n    - `hdxcli --project <project-name> project settings <setting-name> <new-value>`\n- Table\n- Transform\n- Job\n- Purgejobs\n- Sources\n- Dictionary\n- Dictionary Files\n- Function\n- Storage\n- Integration\n- Migrate\n- Version\n\n# FAQ: Common operations\n\n## Showing help \n\nIn order to see what you can do with the tool:\n\n``` shell\nhdxcli --help\n```\n\nCheck which commands are available for each resource by typing:\n``` shell\nhdxcli [<resource>...] [<verb>] --help\n```\n\n## Performing operations against another server\n\nIf you want to use `hdxcli` against another server, use `--profile` option:\n``` shell\nhdxcli --profile <profile-name> project list\n```\n\n## Obtain indented resource information\n\nWhen you use the verb `show` on any resource, the output looks like this:\n``` shell\nhdxcli --project <project-name> project show\n{"name": "project-name", "org": "org-uuid", "description": "description", "uuid": "uuid", ...}\n```\n\nIf you need to have an indented json version, just add `-i`, `--indent int`:\n``` shell\nhdxcli --project <project-name> project show -i 4\n{\n    "name": "project-name", \n    "org": "org-uuid", \n    "description": "description", \n    "uuid": "uuid", \n    ...,\n}\n```',
    'author': 'German Diago Gomez',
    'author_email': 'german@hydrolix.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

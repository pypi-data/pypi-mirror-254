# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nested_chat_plugin_sdk']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.103.0,<0.104.0', 'pydantic-settings>=2.0.3,<3.0.0']

setup_kwargs = {
    'name': 'nested-chat-plugin-sdk',
    'version': '0.1.1',
    'description': '',
    'long_description': '\n\n# Plugin SDK for FastAPI\n\nThe Plugin SDK nested-chat-plugin-sdk is a FastAPI extension that provides a convenient way to handle requests for creating, updating, deleting, and executing operations.\n\n## Installation\n\nInstall dependencies using Poetry and activate the virtual environment. [Learn how to install Poetry](https://python-poetry.org/docs/)\n\n```bash\npoetry install\npoetry shell\n````\n\nInstall the SDK using [Poetry](https://python-poetry.org/):\n\n```bash\npoetry add nested-chat-plugin-sdk\n```\n\n## Example\n```python\nfrom fastapi import FastAPI, Request\nfrom nested_chat_plugin_sdk.sdk import PluginRouter, SyncRequest\n\napp = FastAPI()\nplugin_router = PluginRouter(api_url="")\n\n@plugin_router.on_create\nasync def handle_create(data: SyncRequest):\n    print("create", data)\n\n@plugin_router.on_update\nasync def handle_update(data: SyncRequest):\n    print("update", data)\n\n@plugin_router.on_delete\nasync def handle_delete(data: SyncRequest):\n    print("delete", data)\n\n@plugin_router.on_execute\nasync def handle_execute(request: Request):\n    print("execute", request)\n\napp.include_router(plugin_router)\n\n```\n\n## API Routes\n\n### `/sync`\n\n- `POST`: Create data\n- `PUT`: Update data\n- `DELETE`: Delete data\n\n### `/execute`\n\n- `POST`: Execute operation\n\n## SyncRequest Schema\n\n```python\nfrom nested_chat_plugin_sdk.schemes import SyncRequest\n\nclass SyncRequest(BaseModel):\n    project: dict[str, Any]\n    core: dict[str, Any]\n    variable: dict[str, Any]\n    variable_enum_item: dict[str, Any] = {}\n    variable_group: str | None = None\n\n\n```\n\n\n\n',
    'author': 'vladvavilov',
    'author_email': 'vladvav94@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

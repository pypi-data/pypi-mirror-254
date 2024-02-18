# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flakely']
setup_kwargs = {
    'name': 'flakely',
    'version': '2024.1.31',
    'description': "Signed snowflake ID's",
    'long_description': "# Flakely\n\nAllows for the generation and validation of SHA256 signed snowflakes.\n\n## Installation\n\n```shell\npip install flakely\n```\n\n## Usage\n\nThe `flakely.Flakely` class handles generation and validation of the signed snowflakes. It accepts the following arguemnts:\n\n- `device: int` a device ID that is encoded into each snowflake\n- `process: int` a process ID that is encoded into each snowflake\n- `secret: str | bytes` used to generate unpredictable signature hashes\n\n`Flakely.generate() -> int`\n\nGenerates a new signed snowflake and returns it as an `int`.\n\n`Flakely.generate_bytes() -> bytes`\n\nGenerates a new signed snowflake and returns it as a `bytes` object.\n\n`Flakely.validate(snowflake: int | bytes) -> bool`\n\nChecks that a snowflake's signature is valid for the payload.\n\n`Flakely.get_signature(flake: bytes) -> bytes`\n\nGenerates a signature for the snowflake payload as SHA256 digest.\n\n`Flakely.get_tick() -> int`\n\nReturns an integer to use as the timestamp.\n",
    'author': 'Zech Zimmerman',
    'author_email': 'hi@zech.codes',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

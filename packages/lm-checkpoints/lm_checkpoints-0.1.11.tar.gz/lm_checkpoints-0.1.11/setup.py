# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lm_checkpoints', 'lm_checkpoints.testing']

package_data = \
{'': ['*']}

install_requires = \
['accelerate>=0.24.1,<0.25.0',
 'torch>=2.0.0,!=2.0.1,!=2.1.0',
 'transformers>=4.35.0,<5.0.0']

setup_kwargs = {
    'name': 'lm-checkpoints',
    'version': '0.1.11',
    'description': 'Simple library for loading checkpoints of language models.',
    'long_description': '# lm-checkpoints\nSimple library for dealing with language model checkpoints.\n\nInstall using `pip install lm-checkpoints`.\n\n## Example\nSay you want to compute some metrics for all model checkpoints of Pythia 160m, but only seed 0.\n\n```\nfrom lm_checkpoints import PythiaCheckpoints\n\nfor ckpt in PythiaCheckpoints(size=160,seed=[0]):\n    # Do something with ckpt.model or ckpt.tokenizer\n```\n\nOr if you only want to load steps `0, 1, 2, 4, 8, 16` for all available seeds:\n```\nfrom lm_checkpoints import PythiaCheckpoints\n\nfor ckpt in PythiaCheckpoints(size=160,step=[0, 1, 2, 4, 8, 16]):\n    # Do something with ckpt.model or ckpt.tokenizer\n```\n\nAlternatively, you may want to load all final checkpoints of MultiBERTs:\n```\nfrom lm_checkpoints import MultiBERTCheckpoints\n\nfor ckpt in MultiBERTCheckpoints.final_checkpoints():\n    # Do something with ckpt.model or ckpt.tokenizer\n```',
    'author': 'Oskar van der Wal',
    'author_email': 'odw@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hlt_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'swarms', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'hlt-torch',
    'version': '0.0.1',
    'description': 'Paper - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Humanoid Locomotion Transformer\nThis is an implementation of the robotic transformer for humanoid robots from the premier paper from berkely: "Real-World Humanoid Locomotion with Reinforcement Learning". Here we implement the state policy model which is an MLP/FFN and a Transformer model that intakes both history and action tokens to output the next action sequence.\n\n\n## Install\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/HLT',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

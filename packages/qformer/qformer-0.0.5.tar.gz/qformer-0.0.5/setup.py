# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qformer']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'swarms', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'qformer',
    'version': '0.0.5',
    'description': 'qformer - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# Qformer\nImplementation of Qformer from BLIP2 in Zeta Lego blocks. The implementation is here straight from Figure 2. In particular the image block and text block.\n\n## Install\n`pip3 install qformer`\n\n\n## Usage\n```python\nimport torch\nfrom qformer import QFormer\n\nx = torch.randn(\n    1, 32, 512\n)  # Create a random tensor of shape (1, 32, 512)\n\nimg = torch.randn(\n    1, 32, 512\n)  # Create another random tensor of shape (1, 32, 512)\n\nqformer = QFormer(\n    512, 8, 8, 0.1, 2, 2\n)  # Create an instance of the QFormer model\n\ny = qformer(\n    x, img\n)  # Apply the QFormer model to the input tensors x and img\n\nprint(y.shape)  # Print the shape of the output tensor y\n\n\n```\n\n\n# License\nMIT\n\n\n\n# Citation\n```bibtext\n@misc{li2023blip2,\n    title={BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models}, \n    author={Junnan Li and Dongxu Li and Silvio Savarese and Steven Hoi},\n    year={2023},\n    eprint={2301.12597},\n    archivePrefix={arXiv},\n    primaryClass={cs.CV}\n}\n```',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/qformer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

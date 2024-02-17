# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qwak_inference',
 'qwak_inference.batch_client',
 'qwak_inference.configuration',
 'qwak_inference.realtime_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.0.0,<3.0.0']

extras_require = \
{':python_full_version >= "3.7.1" and python_version < "3.10"': ['numpy>=1.21.6'],
 ':python_version >= "3.10"': ['numpy>=1.24.0'],
 'batch': ['qwak-core>=0.3.52',
           'boto3>=1.24.89,<2.0.0',
           'joblib>=1.1.0,<2.0.0',
           'pyarrow>=6.0.0,<11.0.0'],
 'batch:python_full_version >= "3.7.1" and python_version < "3.8"': ['pandas<1.4',
                                                                     'pandas<1.4'],
 'batch:python_version >= "3.8" and python_version < "3.12"': ['pandas>=1.4.0',
                                                               'pandas>=1.4.0'],
 'feedback': ['qwak-core>=0.3.52',
              'boto3>=1.24.89,<2.0.0',
              'joblib>=1.1.0,<2.0.0'],
 'feedback:python_full_version >= "3.7.1" and python_version < "3.8"': ['pandas<1.4',
                                                                        'pandas<1.4'],
 'feedback:python_version >= "3.8" and python_version < "3.12"': ['pandas>=1.4.0',
                                                                  'pandas>=1.4.0']}

setup_kwargs = {
    'name': 'qwak-inference',
    'version': '0.1.13',
    'description': 'Qwak Inference is a Python library for running predictions again Qwak Models.',
    'long_description': '# Qwak Inference\n\nQwak is an end-to-end production ML platform designed to allow data scientists to build, deploy, and monitor their models in production with minimal engineering friction.\nQwak Inference contains tools that allow predicting against the Qwak Platform\n',
    'author': 'Qwak',
    'author_email': 'info@qwak.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)

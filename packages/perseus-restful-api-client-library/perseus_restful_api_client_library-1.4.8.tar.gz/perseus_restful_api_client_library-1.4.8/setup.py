# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['majormode',
 'majormode.perseus',
 'majormode.perseus.client',
 'majormode.perseus.client.service',
 'majormode.perseus.client.service.account',
 'majormode.perseus.client.service.area',
 'majormode.perseus.client.service.category',
 'majormode.perseus.client.service.notification',
 'majormode.perseus.client.service.social',
 'majormode.perseus.client.service.team',
 'majormode.perseus.client.service.team.test',
 'majormode.perseus.client.unittest']

package_data = \
{'': ['*']}

install_requires = \
['perseus-core-library>=1.19,<2.0', 'requests>=2.31,<3.0']

setup_kwargs = {
    'name': 'perseus-restful-api-client-library',
    'version': '1.4.8',
    'description': 'Perseus RESTful API Client Python Library',
    'long_description': '# Perseus RESTful API Client Python Library\n\nRepository of classes that provide Pythonic interfaces to connect to a RESTful API server developed with Perseus RESTful API server framework.\n\n## Python Library `Poster 0.8.1`\n\nNote: this library includes a modified version of `poster 0.8.1`, which original version provides a set of classes and functions to facilitate making HTTP POST (or PUT) requests using the standard multipart/form-data encoding.\n\nThe original library `poster 0.8.1` cannot be used to upload file uploaded into memory (i.e., stream-to-memory), like for instance django `InMemoryUploadedFile`. The reason is that such file-like object doesn\'t support the method `fileno()` used by the `poster 0.8.1` to determine the size of the file-like object to upload in Python module `poster.encode`:\n\n```python\nif fileobj is not None and filesize is None:\n    # Try and determine the file size\n    try:\n        self.filesize = os.fstat(fileobj.fileno()).st_size\n    except (OSError, AttributeError):\n        try:\n            fileobj.seek(0, 2)\n            self.filesize = fileobj.tell()\n            fileobj.seek(0)\n        except:\n            raise ValueError("Could not determine filesize")\n```\n\nThis code raises the exception `io.UnsupportedOperation` that `poster 0.8.1` doesn\'t catch. Chris AtLee included Alon Hammerman\'s patch in the tag `tip` of the library ``poster`, for catching the`io.UnsupportedOperation for fileno` on 2013-03-12:\n\n```python\ntry:\n    from io import UnsupportedOperation\nexcept ImportError:\n    UnsupportedOperation = None\n\n(...)\n\nif fileobj is not None and filesize is None:\n    # Try and determine the file size\n    try:\n        self.filesize = os.fstat(fileobj.fileno()).st_size\n    except (OSError, AttributeError, UnsupportedOperation):\n        try:\n            fileobj.seek(0, 2)\n            self.filesize = fileobj.tell()\n            fileobj.seek(0)\n        except:\n            raise ValueError("Could not determine filesize")\n```\n\nHowever, the latest version of `poster` installable with `pip` is still `0.8.1`.\n',
    'author': 'Daniel CAUNE',
    'author_email': 'daniel.caune@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/majormode/perseus-restful-api-client-python-library',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

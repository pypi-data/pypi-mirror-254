import os
import re
from setuptools import setup,find_packages


requires = ["requests==2.31.0","urllib3==2.2.0"]
_long_description = """

## NewtApi

> Newt Api Json Server For Python and app To Myket

<p align="center">
    <img src="https://s8.uupload.ir/files/img_20240202_130735_894_u6yf.png" alt="ArseinRubika" width="128">
    <br>
    <b>NewtApi</b>
    <br>
</p>


### How to import the Rubik's library

``` bash
from NewtApi import Client
```

### How to install the library

``` bash
pip install NewtApi==1.0.0
```

### My ID Channel in Rubika

``` bash
@Newt__Server
```
## An example:
``` python
from NewtApi import Client

api = Client("username Api"," password Api")

buildApi = api.addApi('test',"data text or json")

print(buildApi)
```



"""

setup(
    name = "NewtApi",
    version = "1.0.0",
    author = "AbolfazlMirzaei",
    author_email = "newtapi@gmail.com",
    description = ("Python library for working with server Api (New Api)"),
    license = "MIT",
    keywords = ["api","API","Api","newtapi","NewtApi","NewtAPI","NEWTAPI"],
    url = "https://www.arver.ir/",
    packages = ['NewtApi'],
    long_description=_long_description,
    long_description_content_type = 'text/markdown',
    install_requires=requires,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
    ],
)

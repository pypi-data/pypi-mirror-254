import re
import os
import sys
import py_compile
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r"VERSION\s+=\s+(.*)")

thisdir = os.path.dirname(__file__)
readme = open(os.path.join(thisdir, "README.rst")).read()

with open("enrichsdk/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    name="enrichsdk",
    version="5.1.7",
    description="Enrich Developer Kit",
    long_description=readme,
    url="http://github.com/pingali/scribble-enrichsdk",
    author="Venkata Pingali",
    author_email="pingali@scribbledata.io",
    license="All rights reserved",
    scripts=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "ruptures",
        "wheel",
        "click>=7.1.2",
        "aioitertools==0.8.0",

        "typing-extensions==4.8.0",
        "glob2==0.7",
        "httpx",
        "h2",
        "chardet==4.0.0",
        "requests==2.26.0",
        "requests-oauthlib==0.8.0",
        "pytest>=5.1.7",
        "pandas>=1.3.5,<1.5",
        "distributed==2.30.1",
        "idna==2.8",
        "coverage==5.5",
        "flake8",
        "raven==6.6.0",
        "python-json-logger==2.0.4",
        "python-dateutil>=2.8.1",
        "pydantic<=1.10.10",

        # numpy/statsmodels issues
        "numpy<=1.23.0",

        # Celery breaks without these..
        # https://github.com/celery/celery/issues/7607
        "s3fs>=0.5.1,<=0.5.2",
        "fsspec>=0.8.5,<=0.8.7",

        "botocore>=1.19.51,<=1.24.21",
        "aiobotocore>=1.2.1,<=1.2.2",

        "colored==1.3.5",
        #"flask-multistatic==1.0",
        "humanize==0.5.1",
        "pytz>=2020.1",
        #"Flask==2.0.3",
        "Jinja2>=3.1.3",
        "pytest-cov",
        "Markdown>=2.9.10",
        "prompt-toolkit>3.0.1,<3.1.0",
        "pyarrow>=0.9.0",
        "cytoolz>=0.9.0.1",
        "jsonschema>=3.2.0",
        "scipy<=1.10.0",
        "seaborn",
        #"flask_cors",
        #'moto>=1.3.14',
        "packaging<=20.0",
        "dask>=2.17.0,<20.0.0",
        "prefect>=0.15.7,<0.15.11",
        "distro>=1.4.0",
        "gcsfs==0.6.0",
        "jupyter-core>=4.12.0",
        "nbformat>=5.1.7",
        "tzlocal>=2.0.0",
        "texttable",
        "pykafka",
        "redis",
        "gitpython",
        "logstash_formatter",
        "pyhive",
        "pyfiglet",
        "sqlalchemy>=1.4.0",
        "kafka-python==2.0.2",
        "pykafka==2.8.0",
        "papermill>=2.3.4",
        "sqllineage",
        "google-cloud-logging",
        "unidecode",
        "faker",
        "xlsxwriter",
        "cryptography",
        "pymongo",
        "great-expectations==0.15.39",
        "pandas-stubs==1.5.3.230321",
        "anyio<=3.5.0",
        "openai",
        "pretty-html-table",

        # prophet dependencies
        "plotly>=4.0.0",
        "prophet==1.1.3",

        # classification
        "imblearn==0.0",

        # Boto
        #"boto3==1.16.0"

        # Azure dependencies
        "msgraph-sdk==1.0.0a13",
        "msal>=1.24.0,<=1.25.0"

    ],
    entry_points={
        "console_scripts": [
            "enrichpkg=enrichsdk.scripts.enrichpkg:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

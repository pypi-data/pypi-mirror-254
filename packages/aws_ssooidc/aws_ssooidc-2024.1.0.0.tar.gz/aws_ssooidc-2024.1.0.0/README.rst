===============
**aws_ssooidc**
===============

Overview
--------

Create temporary credentials with AWS SSO-OIDC access tokens.

Prerequisites
-------------

- *Python >= 3.6*
- *boto3 (https://pypi.org/project/boto3/) >= 1.17.78*

Required (Positional) Arguments
-------------------------------

- Position 1: sso_url (the start URL for your AWS SSO login)

Optional (Keyword) Arguments
----------------------------

- client_name
    - Description: Arbitrary name of the SSO client to create.
    - Type: String
    - Default: 'ssoclient'
- region
    - Description: Your AWS region.
    - Type: String
    - Default: 'us-east-1'
- timeout
    - Description: Number of tries before giving up.
    - Type: Integer
    - Default: 30

Usage
-----

Installation:

.. code-block:: BASH

   pip3 install aws-ssooidc
   # or
   python3 -m pip install aws-ssooidc

In Python3:

.. code-block:: PYTHON

   import aws_ssooidc as sso

   response = sso.gettoken('<sso_url>')
   access_token = response['accessToken']

In BASH:

.. code-block:: BASH

   python [/path/to/]aws_ssooidc \
   -u <sso_url>

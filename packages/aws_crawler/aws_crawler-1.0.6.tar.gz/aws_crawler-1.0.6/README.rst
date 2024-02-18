===============
**aws_crawler**
===============

Overview
--------

Crawl through active AWS accounts in an organization using master assumed role.

Usage
-----

Installation:

.. code-block:: BASH

    pip3 install aws_crawler
    python3 -m pip install aws_crawler

Example:

.. code-block:: PYTHON

   """
   Get caller identity from the STS service.

   Authenticate with AWS SSO.
   """
   import argparse
   import boto3
   from botocore import exceptions
   from aws_authenticator import AWSAuthenticator as awsauth
   import aws_crawler

   # Get and parse command line arguments.
   myparser = argparse.ArgumentParser(
      add_help=True,
      allow_abbrev=False,
      description="Get STS credentials for AWS accounts in an organization",
      usage="%(prog)s [options]"
   )
   myparser.add_argument(
      "-V",
      "--version",
      action="version",
      version="%(prog)s 1.0.6"
   )
   myparser.add_argument(
      "-u",
      "--sso_url",
      action="store",
      help="[REQUIRED] SSO URL",
      required=True,
      type=str
   )
   myparser.add_argument(
      "-a",
      "--account",
      action="store",
      help="[REQUIRED] SSO Account ID",
      required=True,
      type=str
   )
   myparser.add_argument(
      "-r",
      "--sso_role",
      action="store",
      help="[OPTIONAL: default = AWSViewOnlyAccess] SSO Role Name",
      required=False,
      default="AWSViewOnlyAccess",
      type=str
   )
   myparser.add_argument(
      "-n",
      "--assumed_role",
      action="store",
      help="[OPTIONAL: default = AWSViewOnlyAccess] Assumed Role Name",
      required=False,
      default="AWSViewOnlyAccess",
      type=str
   )
   myparser.add_argument(
      "-e",
      "--external_id",
      action="store",
      help="[OPTIONAL: default = None] External ID",
      required=False,
      default=None,
      type=str
   )
   myparser.add_argument(
      "-g",
      "--region",
      action="store",
      help="[OPTIONAL: default = us-east-1] Region Name",
      required=False,
      default="us-east-1",
      type=str
   )
   args = myparser.parse_args()
   sso_url = args.sso_url
   sso_role_name = args.sso_role
   sso_account_id = args.account
   assumed_role_name = args.assumed_role
   external_id = args.external_id
   region = args.region

   # Login to AWS.
   auth = awsauth(
      sso_url=sso_url,
      sso_role_name=sso_role_name,
      sso_account_id=sso_account_id,
   )
   session = auth.sso()

   # Get account list.
   accounts = aws_crawler.list_accounts(session)
   account_ids = [account['Id'] for account in accounts]

   # Crawl through each account.
   for account_id in account_ids:
      print(f"Working on {account_id}...")

      try:
         credentials = aws_crawler.get_credentials(
            session,
            f'arn:aws:iam::{account_id}:role/{assumed_role_name}',
            external_id
         )

         client = boto3.client(
            'sts',
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key'],
            aws_session_token=credentials['aws_session_token'],
            region_name=region
         )

         response = client.get_caller_identity()['UserId']
      
      except exceptions.ClientError as e:
         response = 'Could not assume role'
      
      print(response)

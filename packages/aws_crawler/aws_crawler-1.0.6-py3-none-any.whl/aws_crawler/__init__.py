#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Crawl through active AWS accounts in an organization using master assumed role."""
import argparse
from pprint import pprint as pp
import boto3
from botocore import exceptions
from multithreader import threads
from aws_authenticator import AWSAuthenticator as awsauth


__version__ = '1.0.6'


def list_accounts(
    session
) -> list:
    """List all AWS accounts in the organization."""
    print('Getting accounts...')

    client = session.client('organizations')

    paginator = client.get_paginator('list_accounts')
    accounts = []
    for page in paginator.paginate():
        for account in page['Accounts']:
            if account['Status'] == 'ACTIVE':
                accounts.append(account)
    
    print(f'Found {len(accounts)} active accounts...')

    return accounts


def get_credentials(
    session,
    assumed_role_arn: str,
    external_id: str
) -> dict:
    """Get AWS assumed role credentials with STS."""
    client = session.client('sts')

    if external_id is not None:
        sts_r = client.assume_role(
            RoleArn=assumed_role_arn,
            RoleSessionName='aws-org-crawler',
            ExternalId=external_id
        )

    else:
        sts_r = client.assume_role(
            RoleArn=assumed_role_arn,
            RoleSessionName='aws-org-crawler'
        )

    return {
        'aws_access_key_id': sts_r['Credentials']['AccessKeyId'],
        'aws_secret_access_key': sts_r['Credentials']['SecretAccessKey'],
        'aws_session_token': sts_r['Credentials']['SessionToken']
    }


def test_function(
    account_id: str,
    items: dict
) -> dict:
    """Get AWS STS caller identities from accounts."""
    print(f'Working on {account_id}...')

    try:
        credentials = get_credentials(
            items['session'],
            f'arn:aws:iam::{account_id}:role/{items["assumed_role_name"]}',
            items['external_id']
        )

        client = boto3.client(
            'sts',
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key'],
            aws_session_token=credentials['aws_session_token'],
            region_name=items['region']
        )
        response = client.get_caller_identity()['UserId']
    
    except exceptions.ClientError as e:
        response = 'Could not assume role'

    return {
        'account_id': account_id,
        'details': response
    }


def main():
    """Execute test function with SSO login and multithreading."""
    # Get and parse command line arguments.
    myparser = argparse.ArgumentParser(
        add_help=True,
        allow_abbrev=False,
        description='Get STS credentials for AWS accounts in an organization',
        usage='%(prog)s [options]'
    )
    myparser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'{__file__} {__version__}'
    )
    myparser.add_argument(
        '-u',
        '--sso_url',
        action='store',
        help='[REQUIRED] SSO URL',
        required=True,
        type=str
    )
    myparser.add_argument(
        '-a',
        '--account',
        action='store',
        help='[REQUIRED] SSO Account ID',
        required=True,
        type=str
    )
    myparser.add_argument(
        '-r',
        '--sso_role',
        action='store',
        help='[OPTIONAL: default = AWSViewOnlyAccess] SSO Role Name',
        required=False,
        default='AWSViewOnlyAccess',
        type=str
    )
    myparser.add_argument(
        '-n',
        '--assumed_role',
        action='store',
        help='[OPTIONAL: default = AWSViewOnlyAccess] Assumed Role Name',
        required=False,
        default='AWSViewOnlyAccess',
        type=str
    )
    myparser.add_argument(
        '-e',
        '--external_id',
        action='store',
        help='[OPTIONAL: default = None] External ID',
        required=False,
        default=None,
        type=str
    )
    myparser.add_argument(
        '-g',
        '--region',
        action='store',
        help='[OPTIONAL: default = us-east-1] Region Name',
        required=False,
        default='us-east-1',
        type=str
    )
    myparser.add_argument(
        '-t',
        '--thread_num',
        action='store',
        help='[OPTIONAL: default = 10] Number of threads to use',
        required=False,
        default=10,
        type=int
    )
    args = myparser.parse_args()
    sso_url = args.sso_url
    sso_role_name = args.sso_role
    sso_account_id = args.account
    assumed_role_name = args.assumed_role
    external_id = args.external_id
    region = args.region
    thread_num = args.thread_num

    # Login to AWS.
    auth = awsauth(
        sso_url=sso_url,
        sso_role_name=sso_role_name,
        sso_account_id=sso_account_id,
    )
    session = auth.sso()

    # Get account list.
    accounts = list_accounts(session)
    account_ids = [account['Id'] for account in accounts]

    # Execute function with multithreading.
    items = {
        'session': session,
        'assumed_role_name': assumed_role_name,
        'external_id': external_id,
        'region': region
    }
    results = threads(
        test_function,
        account_ids,
        items,
        thread_num=thread_num
    )

    # Print results.
    pp(results)

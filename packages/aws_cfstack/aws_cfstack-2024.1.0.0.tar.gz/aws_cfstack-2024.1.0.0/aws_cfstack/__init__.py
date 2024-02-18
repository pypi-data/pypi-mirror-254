"""Get AWS CloudFormation stack template and parameters."""
import boto3
import json
import os
import argparse
import aws_authenticator


__version__ = "2024.1.0.0"


def get_stack(
    output_path: str,
    auth_method: str,
    profile_name: str = None,
    access_key_id: str = None,
    secret_access_key: str = None,
    sso_url: str = None,
    sso_role_name: str = None,
    sso_account_id: str = None,
) -> None:
    """Download template and parameters for the corresponding stack."""
    # Clean output_path.
    output_path = output_path.rstrip('/')

    # Authenticate to an AWS account and service.
    auth = aws_authenticator.AWSAuthenticator(
        profile_name=profile_name,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        sso_url=sso_url,
        sso_role_name=sso_role_name,
        sso_account_id=sso_account_id,
    )
    if auth_method == "iam":
        session = auth.iam()
    elif auth_method == "profile":
        session = auth.profile()
    elif auth_method == "sso":
        session = auth.sso()
    else:
        raise ValueError("Invalid auth method")
    cf = session.client("cloudformation")

    # GEt caller identity to create working directory inside output_path.
    sts = session.client("sts")
    account_id = sts.get_caller_identity()['Account']
    work_dir = f"{output_path}/aws_cf_stacks/{account_id}"
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    # Get stack list from the specified account.
    paginator = cf.get_paginator('list_stacks')
    response_iterator = paginator.paginate(
        StackStatusFilter=[
            'CREATE_COMPLETE',
            'ROLLBACK_COMPLETE',
            'UPDATE_COMPLETE',
            'UPDATE_ROLLBACK_COMPLETE'
        ]
    )

    # Get stack template and parameters.
    for page in response_iterator:
        for summary in page['StackSummaries']:
            if not summary['StackName'].startswith("StackSet-"):
                template = cf.get_template(
                    StackName=summary['StackName']
                )
                print(f"Writing {work_dir}/{summary['StackName']}.template...")
                with open(f"{work_dir}/{summary['StackName']}.template", "w+") as f:
                    f.write(template['TemplateBody'])
                parameters = cf.describe_stacks(
                    StackName=summary['StackName']
                )
                try:
                    print(f"Writing {work_dir}/{summary['StackName']}.parameters...")
                    with open(f"{work_dir}/{summary['StackName']}.parameters", "w+") as f:
                        f.write(json.dumps(parameters['Stacks'][0]['Parameters']))
                except KeyError as e:
                    print(f"No parameter found for {summary['StackName']}.")

    return None


def get_params():
    """Get script inputs."""
    myparser = argparse.ArgumentParser(
        add_help=True,
        allow_abbrev=False,
        description="Get AWS CloudFormation stack template and parameters.",
        usage="%(prog)s [options]",
    )
    myparser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 2024.1.0.0"
    )
    myparser.add_argument(
        "-o",
        "--output_path",
        action="store",
        help="Output path to store artifacts.",
        required=True,
        type=str,
    )
    myparser.add_argument(
        "-m",
        "--auth_method",
        action="store",
        help="AWS authentication method. Valid values can be profile, iam, or sso.",
        required=True,
        type=str,
    )
    myparser.add_argument(
        "-p",
        "--profile_name",
        action="store",
        help="AWSCLI profile name for authenticating with a profile.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-k",
        "--access_key_id",
        action="store",
        help="AWSCLI IAM access key ID for authenticating with an IAM user.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-s",
        "--secret_access_key",
        action="store",
        help="AWSCLI IAM secret access key for authenticating with an IAM user.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-a",
        "--sso_account_id",
        action="store",
        help="AWS account ID for authenticating with AWS SSO.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-r",
        "--sso_role_name",
        action="store",
        help="AWS SSO role name for authenticating with AWS SSO.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-u",
        "--sso_url",
        action="store",
        help="AWS SSO login URL for authenticating with AWS SSO.",
        nargs="?",
        default=None,
        required=False,
        type=str,
    )
    return myparser.parse_args()


def main():
    """Execute module as a script."""
    params = get_params()
    report = get_stack(
        params.output_path,
        params.auth_method,
        profile_name=params.profile_name,
        access_key_id=params.access_key_id,
        secret_access_key=params.secret_access_key,
        sso_url=params.sso_url,
        sso_role_name=params.sso_role_name,
        sso_account_id=params.sso_account_id,
    )

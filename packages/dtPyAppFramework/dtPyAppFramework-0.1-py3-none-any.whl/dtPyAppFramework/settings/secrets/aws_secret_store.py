from .secret_store import AbstractSecretStore, SecretsStoreException
from shutil import which
from ...misc import run_cmd
import boto3
import logging

class AWSSecretsStore(AbstractSecretStore):
    """
    A class representing an AWS Secrets Store for managing secrets.

    Attributes:
        store_priority (int): Priority of the secret store.
        store_name (str): Name of the secret store.
        application_settings (Settings): An instance of Settings providing application settings.
        aws_profile (str): AWS profile for the secrets store.
        aws_region (str): AWS region for the secrets store.
        aws_session (boto3.session.Session): Boto3 session for interacting with AWS.
        aws_secretsmanager (boto3.client): Boto3 client for AWS Secrets Manager.
    """

    def __init__(self, store_priority, store_name, application_settings) -> None:
        """
        Initialize the AWSSecretsStore.

        Args:
            store_priority (int): Priority of the secret store.
            store_name (str): Name of the secret store.
            application_settings (Settings): An instance of Settings providing application settings.
        """
        super().__init__(store_name, "AWS_Secrets_Store", store_priority, application_settings)

        # Check if AWS CLI is installed
        if not which("aws"):
            raise SecretsStoreException("AWS Secrets Store requires the AWS Command Line Utility to be installed.")

        # Get AWS profile
        self.aws_profile = self.get_store_setting('aws_profile')
        if not self.aws_profile:
            raise SecretsStoreException('AWS Secrets Store is missing required aws_profile parameter.')

        # Get AWS region
        self.aws_region = self.get_store_setting('aws_region')
        if not self.aws_region:
            raise SecretsStoreException('AWS Secrets Store is missing required aws_region parameter.')

        self.aws_session = None

        # Initialize AWS session based on profile type
        if self.aws_profile == 'key':
            aws_access_key_id = self.get_store_setting('aws_access_key_id')
            aws_secret_access_key = self.get_store_setting('aws_secret_access_key')
            if not aws_access_key_id or not aws_secret_access_key:
                raise SecretsStoreException('AWS Secrets Store of type key requires both aws_access_key_id and aws_secret_access_key parameters.')
            self.aws_session = boto3.session.Session(region_name=self.aws_region, aws_access_key_id=aws_access_key_id,
                                                     aws_secret_access_key=aws_secret_access_key)
        elif self.aws_profile == 'ec2':
            self.aws_session = boto3.session.Session(region_name=self.aws_region)
        elif self.aws_profile.startswith('sso'):
            aws_sso_profile = self.aws_profile.split(':')[1]
            aws_sso_resp = run_cmd(f'aws sso login --profile {aws_sso_profile}')
            if not aws_sso_resp or "Successfully logged into Start URL" not in aws_sso_resp:
                raise SecretsStoreException(f"Unable to initialise SSO for the AWS profile {aws_sso_profile}.")
            self.aws_session = boto3.session.Session(region_name=self.aws_region)
        else:
            raise SecretsStoreException(f"Unrecognised AWS Profile type {self.aws_profile}.")

        # Initialize AWS Secrets Manager client
        self.aws_secretsmanager = self.aws_session.client('secretsmanager')
        try:
            # Check if AWS Secrets Manager is accessible
            self.aws_secretsmanager.list_secrets()
        except Exception as ex:
            raise SecretsStoreException(f'AWS Secrets Store, Not Available. Error: {str(ex)}')

    def get_secret(self, key, default_value=None):
        """
        Get a secret from the AWS Secrets Manager.

        Args:
            key (str): Key of the secret.
            default_value: Default value to return if the secret is not found.

        Returns:
            Secret value if found, else default_value.
        """
        try:
            entry = self.aws_secretsmanager.get_secret_value(SecretId=key)['SecretString']
        except Exception as ex:
            logging.error(str(ex))
            entry = None

        if not entry:
            entry = default_value

        return entry

    def set_secret(self, key, value):
        """
        Set a secret in the AWS Secrets Manager.

        Args:
            key (str): Key of the secret.
            value: Value of the secret.
        """
        try:
            resp = self.aws_secretsmanager.create_secret(Name=key, SecretString=value, ForceOverwriteReplicaSecret=True)
            if "Name" not in resp:
                raise SecretsStoreException(f'Inconsistent response from AWS: {str(resp)}')
        except Exception as ex:
            logging.error(str(ex))
            raise SecretsStoreException(str(ex))

    def delete_secret(self, key):
        """
        Delete a secret from the AWS Secrets Manager.

        Args:
            key (str): Key of the secret.

        Returns:
            True if the secret is deleted, else False.
        """
        try:
            resp = self.aws_secretsmanager.delete_secret(SecretId=key, ForceDeleteWithoutRecovery=True)
            if "Name" not in resp:
                raise SecretsStoreException(f'Inconsistent response from AWS: {str(resp)}')
        except Exception as ex:
            logging.error(str(ex))
            raise SecretsStoreException(str(ex))

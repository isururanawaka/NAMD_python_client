import logging
import time
import json

from airavata_sdk.clients.keycloak_token_fetcher import Authenticator

from airavata_sdk.clients.api_server_client import APIServerClient

from airavata_sdk.clients.credential_store_client import CredentialStoreClient

from airavata.model.experiment.ttypes import ExperimentModel, ExperimentType, UserConfigurationDataModel
from airavata.model.scheduling.ttypes import ComputationalResourceSchedulingModel

from airavata_sdk.clients.utils.data_model_creation_util import DataModelCreationUtil

from airavata_sdk.clients.utils.api_server_client_util import APIServerClientUtil

from airavata_sdk.clients.utils.experiment_handler_util import  ExperimentHandlerUtil

from airavata_sdk.clients.sftp_file_handling_client import SFTPConnector

from airavata_sdk.transport.settings import GatewaySettings

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

configFile = "/Users/isururanawaka/Documents/Airavata_Repository/NAMD_Test/NAMD_python_client/resources/settings.ini"


experiment_handler = ExperimentHandlerUtil(configFile)

experiment_handler.launch_experiment(user_id='isjarana@iu.edu', experiment_name='testing_simple',
                                     description='sample_exp',
                                     local_input_path='./gaussian')


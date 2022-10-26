import logging
import os
from airavata_sdk.clients.utils.experiment_handler_util import ExperimentHandlerUtil

logger = logging.getLogger("airavata_sdk.clients.utils.experiment_handler_util")

logger.setLevel(logging.INFO)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
configFile = "./resources/settings_namd.ini"

experiment_handler = ExperimentHandlerUtil(configFile)


def create_NAMD_file_mapping(input_file_list):
    ff_parameter_file = []
    file_mapping = {}
    for x in input_file_list:
        if x.endswith(".prm") or x.endswith(".str"):
            ff_parameter_file.append(x)
        elif x == 'qwikmd_equilibration_0_constraints.pdb':
            file_mapping['Constraints_pdb'] = x
        elif x.endswith(".pdb"):
            file_mapping['Coordinates-PDB-file'] = x
        elif x.endswith(".conf"):
            file_mapping['MD_Instructions_Input'] = x
        elif x.endswith('.psf'):
            file_mapping['Protein-Structure-File'] = x
    file_mapping['ff-parameter-files'] = ff_parameter_file
    return file_mapping


file_list = ['par_all36_carb.prm', 'par_all36_cgenff.prm',
             'par_all36_lipid.prm', 'par_all36_na.prm',
             'par_all36_prot.prm', 'qwikmd_equilibration_0.conf',
             'qwikmd_equilibration_0_constraints.pdb', 'toppar_all36_carb_glycopeptide.str',
             'toppar_water_ions_namd.str', 'ubq-test_QwikMD.pdb', 'ubq-test_QwikMD.psf']

experiment_handler.launch_experiment(experiment_name='namd_simple',
                                     description='sample_exp',
                                     local_input_path='./namd', input_file_mapping=create_NAMD_file_mapping(file_list),
                                     computation_resource_name='Expanse',
                                     queue_name='shared', output_path='./output')

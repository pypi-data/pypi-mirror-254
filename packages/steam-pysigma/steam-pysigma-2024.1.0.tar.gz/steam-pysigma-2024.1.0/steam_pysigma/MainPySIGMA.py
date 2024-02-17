import os
from pathlib import Path
import logging
import subprocess

from steam_pysigma.comsol.BuildComsolModel import BuildComsolModel
from steam_pysigma.data import DataPySIGMA as dS
from steam_pysigma.utils.Utils import get_user_settings, read_data_from_yaml
from steam_pysigma.utils.Utils import make_folder_if_not_existing

class MainPySIGMA:
    """
        Class to generate SIGMA models
    """

    def __init__(self, model_folder: str = None, verbose: bool = False):
        """

        :param input_file_path: path to input yaml file
        :param input_coordinates_path: path to file with coordinates to evaluate B_field
        :param model_folder: Output path of java files and mph model.
        :param path_to_results: location of comsol-generated results
        :param verbose:
        """

        logger = logging.getLogger()
        if verbose:
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.DEBUG)

        self.model_folder = model_folder
        make_folder_if_not_existing(self.model_folder)

    def build(self, input_yaml_file_path: str = None, input_coordinates_path=None, results_folder_name=None, settings=None):
        """
        Triggers building of Comsol model
        """
        dm = read_data_from_yaml(input_yaml_file_path, dS.DataPySIGMA)
        input_folder_path = os.path.dirname(input_yaml_file_path)
        sdm = read_data_from_yaml(f'{os.path.splitext(input_yaml_file_path)[0]}.set', dS.MultipoleSettings)
        roxie_data = read_data_from_yaml(f'{os.path.splitext(input_yaml_file_path)[0]}.geom', dS.SIGMAGeometry)
        bh_curve_database = Path(input_folder_path, dm.Sources.bh_curve_source).resolve()
        if not os.path.exists(bh_curve_database):
            raise Exception(f'Path to bh_curve_source specified in the input file {input_yaml_file_path} is: {bh_curve_database}, but it does not exist!')
        if results_folder_name:
            path_to_results = os.path.join(self.model_folder, results_folder_name)
        else:
            path_to_results = self.model_folder
        make_folder_if_not_existing(path_to_results)
        if not settings:
            settings_folder = os.path.join(Path(__file__).parent.parent, 'tests')
            settings = get_user_settings(settings_folder)
        BuildComsolModel(model_data=dm, input_conductor_params=sdm, settings=settings,
                         output_path=self.model_folder, path_to_results=path_to_results,
                         input_coordinates_path=input_coordinates_path, roxie_data=roxie_data,
                         bh_curve_database=bh_curve_database)

    def run_pysigma(self, magnet_name):
        # Establish necessary paths
        batch_file_path = os.path.join(self.model_folder, f"{magnet_name}_Model_Compile_and_Open.bat")
        print(f'Running Comsol model via: {batch_file_path}')
        current_path = os.getcwd()
        os.chdir(self.model_folder)   # must change path to the folder with .bat file otherwise it does not work
        proc = subprocess.Popen([batch_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        (stdout, stderr) = proc.communicate()
        log_file_path = os.path.join(self.model_folder, "log_bat_file.txt")
        error = False
        if proc.returncode != 0:
            print(stderr)
            raise ValueError(
                f"Batch file throws an error, COMSOL model could not be completed! Review error at {log_file_path}.")
        else:
            print(stdout)
            error_lines = []
            for line in stdout.split('\n'):
                if "error" in line.lower():
                    error = True
                if error:
                    error_lines.append(line)
        with open(log_file_path, 'w') as logfile:
            logfile.write(stdout)
        os.chdir(current_path)
        if error:
            # Additional code to format error_lines into a readable message
            error_message = '\n'.join(error_lines)
            error_message = error_message[:200]  # Limit error_message to 200 characters
            raise ValueError(
                f"Batch file throws an error, COMSOL model could not be completed! Error message:\n{error_message}...\nReview full log at {log_file_path}.")
        else:
            print(f"Running batch file passes! See log file at {log_file_path}.")
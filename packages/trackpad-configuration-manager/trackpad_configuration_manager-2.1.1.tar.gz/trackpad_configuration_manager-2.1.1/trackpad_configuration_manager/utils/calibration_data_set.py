import json
import os
import sys

from trackpad_configuration_manager.configuration import Calibration, Configuration, BaseConfigFile


class HapticCalibrationProfileLevel:
    VOLUME_25 = "25%"
    VOLUME_50 = "50%"
    VOLUME_75 = "75%"
    VOLUME_100 = "100%"


class SensingCalibrationProfileLevel:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ConfigurationFactory:

    @staticmethod
    def create(file_name: str) -> BaseConfigFile:
        file = open(file_name)
        json_data = json.load(file)
        file.close()

        if {"file-type", "target_address", "target_cpu"}.issubset(json_data.keys()) is False:
            raise Exception("Invalid file format")

        match json_data["file-type"]["value"]:
            case "calibration":
                return Calibration(json_data, file_name)
            case "configuration":
                return Configuration(json_data, file_name)


class CalibrationDataSet(Calibration):
    CALIBRATION_STRING = "calibration"

    FEEDBACK_DICT = {"25%": 0, "50%": 1, "75%": 2, "100%": 3}

    def __init__(self, template_calibration_file_path: str):

        json_data = None

        with open(template_calibration_file_path, 'r') as file:
            json_data = json.load(file)

        if json_data is None:
            raise Exception("Error while loading json file")

        self.__validate_json_template(json_data)

        super(CalibrationDataSet, self).__init__(json_data, template_calibration_file_path)

        self.target_cpu = self.json_data["target_cpu"]["value"]

    def __validate_json_template(self, json_data):

        if "file-type" not in json_data:
            raise Exception("Invalid file format")

        if json_data["file-type"]["value"] != self.CALIBRATION_STRING:
            raise Exception("Wrong file type")

        if json_data["version"]["value"] != 3:
            raise Exception("Wrong version of json file")

        # not containing "target_address" key
        if "target_address" not in json_data:
            raise Exception("No target address in json file")

        if "target_cpu" not in json_data:
            raise Exception("No target cpu in json file")

    def get_nbr_zone_x(self):
        return self.json_data["configuration"]["division"]["nbWidthDivision"]

    def get_nbr_zone_y(self):
        return self.json_data["configuration"]["division"]["nbHeightDivision"]

    def update_sensing_profile(self, level: SensingCalibrationProfileLevel, sensing_matrix):

        # validate matrix is two dimensional
        if len(sensing_matrix) == 0 or len(sensing_matrix[0]) == 0:
            raise Exception("Invalid matrix size")

        if level == SensingCalibrationProfileLevel.LOW or level == SensingCalibrationProfileLevel.MEDIUM or \
                level == SensingCalibrationProfileLevel.HIGH:

            sensing_entries = self.json_data["configuration"]["value"]["sensing"]["value"]
            for index in range(len(sensing_entries)):
                if level in sensing_entries[index]:
                    matrix_ref_profile = sensing_entries[index][level]["value"]
                    self.__update_ref_matrix(matrix_ref_profile, sensing_matrix)
                    return

            raise Exception("Cannot update the sensing profile")
        else:
            raise Exception("Invalid sensing level")

    def update_feedback_profile(self, level: HapticCalibrationProfileLevel, feedback_matrix):

        # validate matrix is two dimensional
        if len(feedback_matrix) == 0 or len(feedback_matrix[0]) == 0:
            raise Exception("Invalid matrix size")

        if level == HapticCalibrationProfileLevel.VOLUME_25 or level == HapticCalibrationProfileLevel.VOLUME_50 or \
                level == HapticCalibrationProfileLevel.VOLUME_75 or \
                level == HapticCalibrationProfileLevel.VOLUME_100:

            feedback_entries = self.json_data["configuration"]["value"]["feedback"]["value"]
            for index in range(len(feedback_entries)):
                if level in feedback_entries[index]:
                    matrix_ref_profile = feedback_entries[index][level]["value"]
                    self.__update_ref_matrix(matrix_ref_profile, feedback_matrix)
                    return
        else:
            raise Exception("Invalid feedback level")

    def __update_ref_matrix(self, calibration_matrix_ref, new_matrix):

        # zero matrix
        for i in range(len(calibration_matrix_ref)):
            for j in range(len(calibration_matrix_ref[i])):
                calibration_matrix_ref[i][j].set_file_value_from_int(0)

        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                calibration_matrix_ref[i][j].set_file_value_from_int(new_matrix[i][j])

    def save_output_json_file(self, output_json_file: str, output_directory=""):

        output_calibration_file = os.path.join(output_directory, output_json_file)

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            output_calibration_file = os.path.join(os.path.dirname(sys.executable), output_calibration_file)

        output_calibration_file = os.path.join(output_directory, output_calibration_file)

        self.save_on_file(output_calibration_file)

    def save_to_hex_file(self, hex_file_path: str):
        hex_file = self.get_hex_file()
        hex_file.generate_file(hex_file_path)

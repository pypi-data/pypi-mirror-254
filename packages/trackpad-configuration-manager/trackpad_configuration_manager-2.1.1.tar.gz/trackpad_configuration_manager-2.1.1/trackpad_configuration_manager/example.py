from datetime import datetime

from trackpad_configuration_manager.probe.probe import Probe
from trackpad_configuration_manager.utils.calibration_data_set import CalibrationDataSet, \
    SensingCalibrationProfileLevel, HapticCalibrationProfileLevel

# example: How to load a calibration file template, update and save it on a device via the ST-Link probe
if __name__ == "__main__":
    calibration_data_set = CalibrationDataSet("template/calibration_Gen2.json")

    # update the sensing profile for medium sensitivity
    # These value are computed using the calibration methodology provided by Boreas separately

    #                   Top of trackpad
    sensing_matrix = [[1, -2, 0],  # index [0,0], [0,1], [0,2]
                      [2, 10, 1],  # index [1,0], [1,1], [1,2]
                      [3, 12, 3]]  # index [2,0], [2,1], [2,2]
    #               Bottom of trackpad

    calibration_data_set.update_sensing_profile(SensingCalibrationProfileLevel.MEDIUM, sensing_matrix)

    # update the haptic profile for 50% volume
    # These value are computed using the calibration methodology provided by Boreas separately

    #                   Top of trackpad
    feedback_matrix = [[10, 5, 2],  # index [0,0], [0,1], [0,2]
                       [4, 5, 6],   # index [1,0], [1,1], [1,2]
                       [7, 8, 9]]   # index [2,0], [2,1], [2,2]
    #               Bottom of trackpad

    calibration_data_set.update_feedback_profile(HapticCalibrationProfileLevel.VOLUME_50, feedback_matrix)

    # save the updated json file with timestamp in the file name
    json_output_name = "calibration_Gen2_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    calibration_data_set.save_output_json_file(json_output_name)

    # save on the device via ST-Link probe. The unique id is the serial number of the ST-Link probe.
    unique_id = "002000343137510439383538"
    probe = Probe(unique_id, calibration_data_set.target_cpu, blocking=False, delay_between_ops=True)

    calibration_data_set.save_on_device(probe)

    # save the calibration data set in hex and bin format
    calibration_data_set.save_to_hex_file("calibration_Gen2.hex")
    calibration_data_set.save_to_bin_file("calibration_Gen2.bin")

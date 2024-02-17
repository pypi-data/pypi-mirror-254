import csv
import os
import argparse
import sys
import pkg_resources
import cv2
import shutil
import commentjson

try:
    from ehdg_tools.ehdg_updater import get_index, run_updater, update_csv
    from ehdg_tools.ehdg_okn_checker import detect_with_okn_detector, signal_checker, apply_okn_detection_rule
    from ehdg_tools.ehdg_buffers import TinyFillBuffer
    from ehdg_tools.ehdg_plotter import get_folder_info_from_summary_csv
    from ehdg_tools.ehdg_functions import check_commandline_program
except ModuleNotFoundError:
    tool_install_cmd = "pip install ehdg_tools -U"
    os.system(tool_install_cmd)

try:
    from ehdg_pupil_detector import ehdg_pupil_detector
except ModuleNotFoundError:
    detector_install_cmd = "pip install ehdg_pupil_detector -U"
    os.system(detector_install_cmd)


# This function is to check whether file location and necessary file exist or not
# return array of element which contains file directory, exist or not, excepted file name
def get_file_dir_exist_array(file_name_array_input):
    file_dir_exist_array = []
    for expected_string, name in file_name_array_input:
        file_exist = os.path.isfile(name)
        if file_exist:
            if expected_string in str(name):
                file_exist = True
            else:
                file_exist = False
        file_dir_exist_array.append([name, file_exist, expected_string])
    return file_dir_exist_array


# This function is to read given csv and return first data of given column
def get_timestamp_from_csv(csv_dir_input, column_name_input):
    with open(csv_dir_input, "r") as csv_file:
        csv_data_array = csv.reader(csv_file, delimiter=',')
        header_array = next(csv_data_array)
        first_row = next(csv_data_array)
        data_position = get_index(column_name_input, header_array)

        return float(first_row[data_position])


# This function is to start and end index of given trial in given gaze.csv file
def get_start_end_info(csv_input, trial_id_input):
    start_index = None
    end_index = None
    with open(csv_input, "r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        header_array = next(csv_data)
        rows = []
        for data in csv_data:
            rows.append(data)

        event_string_position = get_index("event_string", header_array)

        start_marker_found = False
        for index, row in enumerate(rows):
            event_string = row[event_string_position]
            if not start_marker_found:
                if "start_marker" in event_string and trial_id_input in event_string:
                    start_index = index
                    start_marker_found = True
            else:
                if "end_marker" in event_string:
                    end_index = index
                    break

        csv_file.close()
        return {"start_index": start_index, "end_index": end_index}


# This function is replace incorrect data rows with correct data rows
def replace_with_correct_data(trial_dir_input, gaze_dir_input, gaze_start_end_input):
    gaze_start_index = gaze_start_end_input["start_index"]
    gaze_end_index = gaze_start_end_input["end_index"]

    # get is_event, event_id and direction value from the input csv
    # because gaze.csv does not have these values
    with open(trial_dir_input, "r") as trial_csv_file:
        trial_csv_data = csv.reader(trial_csv_file, delimiter=',')
        trial_header_array = next(trial_csv_data)
        is_event_position = get_index("is_event", trial_header_array)
        event_id_position = get_index("event_id", trial_header_array)
        direction_position = get_index("direction", trial_header_array)
        trial_rows = []
        for data in trial_csv_data:
            trial_rows.append(data)
        is_event_value = trial_rows[0][is_event_position]
        event_id_value = trial_rows[0][event_id_position]
        direction_value = trial_rows[0][direction_position]
        trial_csv_file.close()

    # get the trial data from gaze.csv by using start index and end index
    with open(gaze_dir_input, "r") as gaze_csv_file:
        gaze_csv_data = csv.reader(gaze_csv_file, delimiter=',')
        header_array = next(gaze_csv_data)

        # sts = sensor timestamp, g = gaze, rts = record timestamp
        # get the header positions which rows need to be modified and used
        g_is_event_position = get_index("is_event", header_array)
        g_event_string_position = get_index("event_string", header_array)
        g_sts_position = get_index("sensor_timestamp", header_array)
        g_rts_position = get_index("record_timestamp", header_array)

        rows = []
        for data in gaze_csv_data:
            rows.append(data)
        correct_data_array = rows[gaze_start_index: gaze_end_index + 1]

        output_data_array = []

        first_sts = 0
        got_first_sts = False
        for data in correct_data_array:
            output_data = data
            # record first sensor timestamp to be used to calculate record timestamp
            if not got_first_sts:
                first_sts = float(data[g_sts_position])
                got_first_sts = True
            record_ts = float(data[g_sts_position]) - first_sts
            # noinspection PyTypeChecker
            # modify and add columns from gaze data to trial data
            output_data[g_rts_position] = record_ts
            output_data[g_is_event_position] = is_event_value
            output_data[g_event_string_position] = event_id_value
            output_data.append(direction_value)
            output_data_array.append(output_data)

        gaze_csv_file.close()

    # rewrite and replace incorrect data with correct data
    with open(trial_dir_input, mode='w', newline="") as new_destination_file:
        csv_writer = csv.DictWriter(new_destination_file, fieldnames=trial_header_array)
        csv_writer.writeheader()
        for data in output_data_array:
            data_to_write = {}
            for ind, name in enumerate(trial_header_array):
                data_to_write[name] = data[ind]
            csv_writer.writerow(data_to_write)

        new_destination_file.close()


# This function is the main function to correct trial data lost issue
# by calling get_start_end_info and replace_with_correct_data
# It also has error handling in case of error
def fix_trial_data_lost(trial_dir_input, gaze_dir_input):
    success = True
    error_string = None
    try:
        trial_csv_file_name = os.path.basename(trial_dir_input)
        output_dir = str(trial_dir_input).replace(trial_csv_file_name, "")
        trial_id, extra_string = str(trial_csv_file_name).split("_", 1)
        gaze_start_end_info = get_start_end_info(gaze_dir_input, trial_id)

        replace_with_correct_data(trial_dir_input, gaze_dir_input, gaze_start_end_info)
    except Exception as error:
        success = False
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error_string = f"Error occurred:error type:{type(error).__name__} in line number:{exc_tb.tb_lineno}."
        trial_csv_file_name = None
        output_dir = None

    return trial_csv_file_name, output_dir, success, error_string


# This function is to get the build-in directory of config file by package name and config file name
def get_config_location(package_name, config_file_name):
    config_dir = pkg_resources.resource_filename(package_name, config_file_name)

    return config_dir


# This function is to update the trial csv file by calling run_updater function
# It has error handling in case of error
def oknpatch_update_csv(input_csv_file_dir, extra_string_for_updated_csv, updater_config):
    success = True
    error_string = None
    try:
        csv_file_name = os.path.basename(input_csv_file_dir)
        updated_file_name = extra_string_for_updated_csv + csv_file_name
        output_dir = input_csv_file_dir.replace(csv_file_name, updated_file_name)
        output_csv_dir = run_updater(updater_config, input_csv_file_dir, output_dir)
        trial_csv_file_name = os.path.basename(output_csv_dir)
        output_dir_without_folder = output_csv_dir.replace(trial_csv_file_name, "")
    except Exception as error:
        success = False
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error_string = f"Error occurred:error type:{type(error).__name__} in line number:{exc_tb.tb_lineno}."
        trial_csv_file_name = None
        output_dir_without_folder = None

    return trial_csv_file_name, output_dir_without_folder, success, error_string


# This function is to replace direction column value of input csv file with given direction input 1 or -1
def replace_with_new_direction(csv_file_input, direction_input):
    replace_successful = True
    if int(direction_input) == 1 or int(direction_input) == -1:
        try:
            with open(csv_file_input, "r") as trial_csv_file:
                trial_csv_data = csv.reader(trial_csv_file, delimiter=',')
                trial_header_array = next(trial_csv_data)
                direction_position = get_index("direction", trial_header_array)
                trial_rows = []
                for data in trial_csv_data:
                    trial_rows.append(data)
                trial_csv_file.close()

            for row in trial_rows:
                row[direction_position] = direction_input

            # rewrite and replace incorrect data with correct data
            with open(csv_file_input, mode='w', newline="") as new_destination_file:
                csv_writer = csv.DictWriter(new_destination_file, fieldnames=trial_header_array)
                csv_writer.writeheader()
                for data in trial_rows:
                    data_to_write = {}
                    for ind, name in enumerate(trial_header_array):
                        data_to_write[name] = data[ind]
                    csv_writer.writerow(data_to_write)

                new_destination_file.close()
        except Exception as error:
            replace_successful = False
            exc_type, exc_obj, exc_tb = sys.exc_info()
            error_string = f"Error occurred:error type:{type(error).__name__} in line number:{exc_tb.tb_lineno}."
            print(error_string)
    else:
        print(f"Direction input must be 1 or -1 but input is {direction_input}")
        replace_successful = False

    return replace_successful


# This function is to change the direction of given csv file and rerun csv updating and okn detecting
def change_direction_and_rerun(csv_file_input, direction_input, extra_string_input, updater_config_input,
                               detector_config_input):
    error_string = None
    result_folder_dir = None
    try:
        replace_successful = replace_with_new_direction(csv_file_input, direction_input)
        if replace_successful:
            updated_file, output_file_location, success, error = oknpatch_update_csv(csv_file_input,
                                                                                     extra_string_input,
                                                                                     updater_config_input)
            updated_file_dir = os.path.join(output_file_location, updated_file)
            result_folder_dir = detect_with_okn_detector(updated_file_dir, detector_config_input)
        else:
            print("okntool could not finish \"change_direction_and_rerun\" process because of error or invalid "
                  "direction input.")
            success = False
    except Exception as error:
        success = False
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error_string = f"Error occurred:error type:{type(error).__name__} in line number:{exc_tb.tb_lineno}."
        result_folder_dir = None

    return result_folder_dir, success, error_string


# opmdc = opm_detector_config_location, es = extra_string, uc = updater_config_location,
# di = direction_input, okndc = okn_detector_config_location,
# pil = plot info location, ril = rule info location
def rerun_recording(main_folder_dir, opmdc, es, uc, di, okndc, pil, ril, overwritten=False,
                    using_pupil_detector=False, buffer_length=7):
    if not os.path.isdir(main_folder_dir):
        print("Recording folder input to be rerun does not exist.")
        return
    rerun_detector = ehdg_pupil_detector.Detector()
    error_string = None
    try:
        with open(opmdc) as opm_config:
            config_info = commentjson.load(opm_config)
            print("<Config Detector Properties>")
            print(config_info)
            detector_properties = config_info
        rerun_detector.update_config(detector_properties)
        updated_properties = rerun_detector.get_config_info()
        print("<Updated Detector Properties>")
        print(updated_properties)
    except Exception as error:
        print(f"Error in retrieving info from config file:{opmdc}!")
        return False, error

    try:
        with open(pil) as plot_info_config:
            plot_info = commentjson.load(plot_info_config)
            print("<Plot Info>")
            try:
                # Retrieve trial plot info from config
                trial_plot_info = plot_info["trial_plot"]
                print(trial_plot_info)

                # Retrieve summary plot info from config
                summary_plot_info = plot_info["summary_plot"]
                print(summary_plot_info)

                # signal_csv_folder_name = trial_plot_info["signal_csv_folder_name"]
                signal_csv_name = trial_plot_info["signal_csv_name"]

                summary_csv_name = summary_plot_info["summary_csv_name"]
            except KeyError:
                print(f"Error in retrieving plot info from config file:{pil}!")
                return False, str(KeyError)
    except Exception as error:
        print(f"Error in retrieving plot info from config file:{pil}!")
        return False, error

    try:
        with open(ril) as rule_info_config:
            rule_info = commentjson.load(rule_info_config)
            print("<Rule Info>")
            try:
                default_rule_set = rule_info["default_rule_set"]
                rule_set = rule_info["rule_set"]
                rule_to_be_applied = None
                for rs in rule_set:
                    if rs["name"] == default_rule_set:
                        rule_to_be_applied = rs
                        break
            except KeyError:
                try:
                    rule_to_be_applied = rule_info["rule"]
                except KeyError:
                    rule_to_be_applied = None

        if rule_to_be_applied:
            try:
                min_chain_length = rule_to_be_applied["min_chain_length"]
                min_unchained_okn = rule_to_be_applied["min_unchained_okn"]
            except KeyError:
                print("okn detector rules are missing in this config.")
                return
        else:
            print("okn detector rules are missing in this config.")
            return
    except Exception as error:
        print(f"Error in retrieving info from config file:{ril}!")
        return False, error

    summary_csv_dir = os.path.join(main_folder_dir, "trials", summary_csv_name)
    if not os.path.isfile(summary_csv_dir):
        print(f"Expected summary csv: {summary_csv_dir} could not be found.")
        new_summary_csv_dir = input("Please link for summary csv here: ")
        new_summary_csv_dir_exist = os.path.isfile(new_summary_csv_dir)
        if not new_summary_csv_dir_exist:
            print(f"Input summary csv: {new_summary_csv_dir_exist} could not be found.")
            print("Therefore, stopping the process.")
            return
        else:
            summary_csv_dir = new_summary_csv_dir
    data_info_array = get_folder_info_from_summary_csv(summary_csv_dir)

    print(f"Overwritten: {overwritten}")
    trials_folder_dir = os.path.join(main_folder_dir, "trials")
    if not os.path.isdir(trials_folder_dir):
        print(f"Trials folder could not be found in input dir:{main_folder_dir}.")
        return
    if overwritten:
        rerun_folder_dir = trials_folder_dir
    else:
        rerun_folder_name = "rerun_trials"

        # avoiding overwritten with while loop
        while True:
            temp_rerun_folder_dir = os.path.join(main_folder_dir, rerun_folder_name)
            if os.path.isdir(temp_rerun_folder_dir):
                string_array = str(rerun_folder_name).split("_")
                try:
                    rerun_number = int(string_array[-1])
                    string_array[-1] = str(rerun_number + 1)
                    rerun_folder_name = "_".join(string_array)
                except ValueError:
                    rerun_folder_name = f"{rerun_folder_name}_1"
            else:
                os.mkdir(temp_rerun_folder_dir)
                rerun_folder_dir = temp_rerun_folder_dir
                break

    if not overwritten:
        # copy the trial video file from each trial folder into rerun folder
        for data_info in data_info_array:
            trial_id = data_info["trial_id"]
            disk_condition = data_info["disk_condition"]
            trial_name = f"{trial_id}_{disk_condition}"
            if using_pupil_detector:
                trial_video_name = f"{trial_name}_cropped.mp4"
                trial_video_dir = os.path.join(trials_folder_dir, trial_name, trial_video_name)
                paste_folder = os.path.join(rerun_folder_dir, trial_name)
                if not os.path.isdir(paste_folder):
                    os.mkdir(paste_folder)
                paste_file_dir = os.path.join(paste_folder, trial_video_name)
                if not os.path.isfile(trial_video_dir):
                    print(f"Trial video: {trial_video_name} could not be found.")
                    print("Starting splitting the video.")
                    print("Checking whether there is okntool in this computer or not.")
                    is_there_okntool = check_commandline_program("okntool")
                    if is_there_okntool:
                        split_video_cmd = f"okntool -t sv -d {main_folder_dir}"
                        os.system(split_video_cmd)
                    else:
                        print("Please install or upgrade okntool first then rerun this process.")
                        print("pip install okntool -U")
                        return
                shutil.copyfile(trial_video_dir, paste_file_dir)
            else:
                trial_csv_name = f"{trial_name}.csv"
                trial_csv_dir = os.path.join(trials_folder_dir, trial_name, trial_csv_name)
                if not os.path.isfile(trial_csv_dir):
                    print(f"{trial_csv_name} is missing in the recording folder.")
                    return
                paste_folder = os.path.join(rerun_folder_dir, trial_name)
                if not os.path.isdir(paste_folder):
                    os.mkdir(paste_folder)
                paste_file_dir = os.path.join(paste_folder, trial_csv_name)
                shutil.copyfile(trial_csv_dir, paste_file_dir)
    else:
        for data_info in data_info_array:
            trial_id = data_info["trial_id"]
            disk_condition = data_info["disk_condition"]
            trial_name = f"{trial_id}_{disk_condition}"
            if using_pupil_detector:
                trial_video_name = f"{trial_name}_cropped.mp4"
                trial_video_dir = os.path.join(trials_folder_dir, trial_name, trial_video_name)
                if not os.path.isfile(trial_video_dir):
                    print(f"Trial video: {trial_video_name} could not be found.")
                    print("Starting splitting the video.")
                    print("Checking whether there is okntool in this computer or not.")
                    is_there_okntool = check_commandline_program("okntool")
                    if is_there_okntool:
                        split_video_cmd = f"okntool -t sv -d {main_folder_dir}"
                        os.system(split_video_cmd)
                    else:
                        print("Please install or upgrade okntool first then rerun this process.")
                        print("pip install okntool -U")
                        return
            else:
                trial_csv_name = f"{trial_name}.csv"
                trial_csv_dir = os.path.join(trials_folder_dir, trial_name, trial_csv_name)
                if not os.path.isfile(trial_csv_dir):
                    print(f"{trial_csv_name} is missing in the recording folder.")
                    return

    rerun_summary_csv_info = []
    for data_info in data_info_array:
        temp_dict = data_info.copy()
        trial_id = data_info["trial_id"]
        disk_condition = data_info["disk_condition"]
        event_id = data_info["event_id"]
        if di:
            direction = di
        else:
            direction = data_info["direction"]
        temp_dict["direction"] = direction
        trial_name = f"{trial_id}_{disk_condition}"
        trial_folder_dir = os.path.join(rerun_folder_dir, trial_name)
        rerun_buffer = TinyFillBuffer(buffer_length)
        if not os.path.isdir(trial_folder_dir):
            print(f"Folder directory: {trial_folder_dir} could not be found.")
            return
        if using_pupil_detector:
            rerun_trial_csv_dir = rerun_trial_with_pupil_detector(rerun_detector, rerun_buffer, trial_folder_dir,
                                                                  event_id, direction)
        else:
            trial_csv_name = f"{trial_name}.csv"
            rerun_trial_csv_dir = os.path.join(trial_folder_dir, trial_csv_name)
        updated_csv = update_csv(rerun_trial_csv_dir, es, uc)
        signal_output_dir = detect_with_okn_detector(updated_csv, okndc)
        signal_data = signal_checker(signal_output_dir, signal_csv_name)
        temp_dict["min_chain_length_rule"] = min_chain_length
        temp_dict["min_unchained_okn_rule"] = min_unchained_okn
        temp_dict["max_chain_length_signal_data"] = signal_data["max_chain_length"]
        temp_dict["unchained_okn_total_signal_data"] = signal_data["unchained_okn_total"]
        is_there_okn = apply_okn_detection_rule(signal_data, min_chain_length, min_unchained_okn)
        temp_dict["okn"] = is_there_okn
        okn_matlab = 1 if is_there_okn else 0
        temp_dict["okn_matlab"] = okn_matlab
        rerun_summary_csv_info.append(temp_dict)

        trial_plot_cmd = f"okntool -t trial -d {trial_folder_dir} -c {pil}"
        os.system(trial_plot_cmd)

    summary_csv_name = os.path.basename(summary_csv_dir)
    rerun_summary_csv_dir = os.path.join(rerun_folder_dir, summary_csv_name)
    rerun_header_array = []
    if rerun_summary_csv_info:
        for header in rerun_summary_csv_info[0]:
            rerun_header_array.append(header)
    else:
        print("There is no info in rerun summary csv info array.")
        return False, error_string
    rewrite_summary_csv(rerun_summary_csv_dir, rerun_summary_csv_info, rerun_header_array)
    summary_plot_cmd = f"okntool -t summary -d {rerun_folder_dir} -c {pil}"
    os.system(summary_plot_cmd)

    return True, error_string, rerun_folder_dir


# opmdc = opm_detector_config_location, es = extra_string, uc = updater_config_location,
# di = direction_input, okndc = okn_detector_config_location,
# pil = plot info location, ril = rule info location
def fix_neon_csv_and_rerun(main_folder_dir, es, uc, okndc, pil, ril):
    if not os.path.isdir(main_folder_dir):
        print("Recording folder input to be rerun does not exist.")
        return

    error_string = None

    try:
        with open(pil) as plot_info_config:
            plot_info = commentjson.load(plot_info_config)
            print("<Plot Info>")
            try:
                # Retrieve trial plot info from config
                trial_plot_info = plot_info["trial_plot"]
                print(trial_plot_info)

                # Retrieve summary plot info from config
                summary_plot_info = plot_info["summary_plot"]
                print(summary_plot_info)

                # signal_csv_folder_name = trial_plot_info["signal_csv_folder_name"]
                signal_csv_name = trial_plot_info["signal_csv_name"]

                summary_csv_name = summary_plot_info["summary_csv_name"]
            except KeyError:
                print(f"Error in retrieving plot info from config file:{pil}!")
                return False, str(KeyError)
    except Exception as error:
        print(f"Error in retrieving plot info from config file:{pil}!")
        return False, error

    try:
        with open(ril) as rule_info_config:
            rule_info = commentjson.load(rule_info_config)
            print("<Rule Info>")
            try:
                default_rule_set = rule_info["default_rule_set"]
                rule_set = rule_info["rule_set"]
                rule_to_be_applied = None
                for rs in rule_set:
                    if rs["name"] == default_rule_set:
                        rule_to_be_applied = rs
                        break
            except KeyError:
                try:
                    rule_to_be_applied = rule_info["rule"]
                except KeyError:
                    rule_to_be_applied = None

        if rule_to_be_applied:
            try:
                min_chain_length = rule_to_be_applied["min_chain_length"]
                min_unchained_okn = rule_to_be_applied["min_unchained_okn"]
            except KeyError:
                print("okn detector rules are missing in this config.")
                return
        else:
            print("okn detector rules are missing in this config.")
            return
    except Exception as error:
        print(f"Error in retrieving info from config file:{ril}!")
        return False, error

    summary_csv_dir = os.path.join(main_folder_dir, "trials", summary_csv_name)
    if not os.path.isfile(summary_csv_dir):
        print(f"Expected summary csv: {summary_csv_dir} could not be found.")
        new_summary_csv_dir = input("Please link for summary csv here: ")
        new_summary_csv_dir_exist = os.path.isfile(new_summary_csv_dir)
        if not new_summary_csv_dir_exist:
            print(f"Input summary csv: {new_summary_csv_dir_exist} could not be found.")
            print("Therefore, stopping the process.")
            return
        else:
            summary_csv_dir = new_summary_csv_dir
    data_info_array = get_folder_info_from_summary_csv(summary_csv_dir)

    gaze_csv_dir = os.path.join(main_folder_dir, "gaze.csv")
    fix_neon_csv(gaze_csv_dir)

    trials_folder_dir = os.path.join(main_folder_dir, "trials")
    if not os.path.isdir(trials_folder_dir):
        print(f"Trials folder could not be found in input dir:{main_folder_dir}.")
        return

    rerun_summary_csv_info = []
    for data_info in data_info_array:
        temp_dict = data_info.copy()
        trial_id = data_info["trial_id"]
        disk_condition = data_info["disk_condition"]
        trial_name = f"{trial_id}_{disk_condition}"
        trial_folder_dir = os.path.join(trials_folder_dir, trial_name)
        if not os.path.isdir(trial_folder_dir):
            print(f"Folder directory: {trial_folder_dir} could not be found.")
            return
        trial_csv_name = f"{trial_name}.csv"
        rerun_trial_csv_dir = os.path.join(trial_folder_dir, trial_csv_name)
        fix_neon_csv(rerun_trial_csv_dir)
        updated_csv = update_csv(rerun_trial_csv_dir, es, uc)
        signal_output_dir = detect_with_okn_detector(updated_csv, okndc)
        signal_data = signal_checker(signal_output_dir, signal_csv_name)
        temp_dict["min_chain_length_rule"] = min_chain_length
        temp_dict["min_unchained_okn_rule"] = min_unchained_okn
        temp_dict["max_chain_length_signal_data"] = signal_data["max_chain_length"]
        temp_dict["unchained_okn_total_signal_data"] = signal_data["unchained_okn_total"]
        is_there_okn = apply_okn_detection_rule(signal_data, min_chain_length, min_unchained_okn)
        temp_dict["okn"] = is_there_okn
        okn_matlab = 1 if is_there_okn else 0
        temp_dict["okn_matlab"] = okn_matlab
        rerun_summary_csv_info.append(temp_dict)

        trial_plot_cmd = f"okntool -t trial -d {trial_folder_dir} -c {pil} -gc {gaze_csv_dir}"
        os.system(trial_plot_cmd)

    summary_csv_name = os.path.basename(summary_csv_dir)
    rerun_summary_csv_dir = os.path.join(trials_folder_dir, summary_csv_name)
    rerun_header_array = []
    if rerun_summary_csv_info:
        for header in rerun_summary_csv_info[0]:
            rerun_header_array.append(header)
    else:
        print("There is no info in rerun summary csv info array.")
        return False, error_string
    rewrite_summary_csv(rerun_summary_csv_dir, rerun_summary_csv_info, rerun_header_array)
    summary_plot_cmd = f"okntool -t summary -d {trials_folder_dir} -c {pil} -gc {gaze_csv_dir}"
    os.system(summary_plot_cmd)

    return True, error_string, trials_folder_dir


def fix_neon_csv(csv_dir):
    neon_gaze_max_width = 1600
    neon_gaze_max_height = 1200
    print(f"Fixing {csv_dir}.")
    with open(csv_dir, "r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        header_array = next(csv_data)
        rows = []
        for data in csv_data:
            rows.append(data)

        x_value_position = get_index("x_value", header_array)
        y_value_position = get_index("y_value", header_array)

    data_array_to_rewrite = []
    for row in rows:
        x_value = float(row[x_value_position])
        y_value = float(row[y_value_position])
        x_nom = x_value / neon_gaze_max_width
        y_nom = y_value / neon_gaze_max_height
        temp_dict = {}
        for ind, name in enumerate(header_array):
            if name == "x_nom":
                temp_dict[name] = x_nom
            elif name == "y_nom":
                temp_dict[name] = y_nom
            else:
                temp_dict[name] = row[ind]
        data_array_to_rewrite.append(temp_dict)

    with open(csv_dir, mode='w', newline="") as new_destination_file:
        csv_writer = csv.DictWriter(new_destination_file, fieldnames=header_array)
        csv_writer.writeheader()
        for data in data_array_to_rewrite:
            csv_writer.writerow(data)

        new_destination_file.close()


def is_pnm_recording(dir_input):
    pnm_video_dir = os.path.join(dir_input, "pnm_eye_video.mp4")
    if os.path.isfile(pnm_video_dir):
        return True
    else:
        return False


def rerun_trial_with_pupil_detector(detector, buffer, trial_folder_dir, event_id_input, direction_input):
    trial_name = os.path.basename(trial_folder_dir)
    trial_video_name = f"{trial_name}_cropped.mp4"
    trial_video_dir = os.path.join(trial_folder_dir, trial_video_name)
    if not os.path.isfile(trial_video_dir):
        print(f"Trial video: {trial_video_name} could not be found.")
        return
    output_csv_dir = os.path.join(trial_folder_dir, f"{trial_name}.csv")
    redetect(detector, buffer, trial_video_dir, output_csv_dir, event_id_input, direction_input)

    return output_csv_dir


def redetect(detector, buffer, trial_video, output_csv_dir, event_id_input, direction_input):
    cap = cv2.VideoCapture(trial_video)

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    print(f"frame_rate:{frame_rate}")
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(f"frame_width:{frame_width}")
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"frame_height:{frame_height}")
    frame_count = 0

    with open(output_csv_dir, mode='w', newline="") as destination_file:
        header_names = ["x_value", "y_value", "x_nom", "y_nom",
                        "record_timestamp", "sensor_timestamp",
                        "frame_rate", "is_event", "event_id",
                        "direction", "confidence", "diameter",
                        "ellipse_axis_a", "ellipse_axis_b",
                        "ellipse_angle"]
        csv_writer = csv.DictWriter(destination_file, fieldnames=header_names)
        csv_writer.writeheader()

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame_count += 1
                frame_time = frame_count / frame_rate
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                result = detector.detect(gray)
                d_ts = result["detector_timestamp"]
                # center_of_pupil = result["center_of_pupil"]
                reversed_center_of_pupil = result["reversed_center_of_pupil"]
                x_value = float(reversed_center_of_pupil[0])
                y_value = float(reversed_center_of_pupil[1])
                axes_of_pupil = result["axes_of_pupil"]
                major_axis = float(axes_of_pupil[0])
                minor_axis = float(axes_of_pupil[1])
                angle_of_pupil = float(result["angle_of_pupil"])
                diameter_of_pupil = float(result["average_diameter_of_pupil"])
                confidence = 0 if x_value <= 0 and y_value <= 0 else 1
                pupil_data = {}
                pupil_data["x_value"] = x_value
                pupil_data["y_value"] = y_value
                pupil_data["major_axis"] = major_axis
                pupil_data["minor_axis"] = minor_axis
                pupil_data["angle_of_pupil"] = angle_of_pupil
                pupil_data["diameter_of_pupil"] = diameter_of_pupil
                pupil_data["confidence"] = confidence
                pupil_data["timestamp"] = d_ts
                pupil_data["record_timestamp"] = frame_time
                return_data = buffer.add(pupil_data)
                if return_data is not None:
                    temp_dict = get_data_dict(return_data, frame_rate, frame_width, frame_height, event_id_input,
                                              direction_input)
                    csv_writer.writerow(temp_dict)
            else:
                got_first_data = False
                for return_data in buffer.buffer:
                    if not got_first_data:
                        got_first_data = True
                    else:
                        temp_dict = get_data_dict(return_data, frame_rate, frame_width, frame_height, event_id_input,
                                                  direction_input)
                        csv_writer.writerow(temp_dict)
                destination_file.close()
                break


def rewrite_summary_csv(csv_dir, info_array, header_array):
    with open(csv_dir, mode='w', newline="") as destination_file:
        header_names = header_array
        csv_writer = csv.DictWriter(destination_file, fieldnames=header_names)
        csv_writer.writeheader()

        for info in info_array:
            csv_writer.writerow(info)
        destination_file.close()


def get_data_dict(data_input, frame_rate, frame_width, frame_height, event_id_input, direction_input):
    d_ts = float(data_input["timestamp"])
    record_timestamp = float(data_input["record_timestamp"])
    x_value = float(data_input["x_value"])
    y_value = float(data_input["y_value"])
    major_axis = float(data_input["major_axis"])
    minor_axis = float(data_input["minor_axis"])
    angle_of_pupil = float(data_input["angle_of_pupil"])
    diameter_of_pupil = float(data_input["diameter_of_pupil"])
    confidence = float(data_input["confidence"])
    ellipse_axis_a = major_axis
    ellipse_axis_b = minor_axis
    ellipse_angle = angle_of_pupil
    diameter = diameter_of_pupil
    frame_rate_input = float(frame_rate)
    sensor_time_stamp = d_ts
    temp_dict = {}
    temp_dict["x_value"] = x_value
    temp_dict["y_value"] = y_value
    temp_dict["x_nom"] = x_value / frame_width
    temp_dict["y_nom"] = 1 - (y_value / frame_height)
    temp_dict["record_timestamp"] = record_timestamp
    temp_dict["sensor_timestamp"] = sensor_time_stamp
    temp_dict["frame_rate"] = frame_rate_input
    temp_dict["is_event"] = 0
    temp_dict["event_id"] = event_id_input
    temp_dict["direction"] = direction_input
    temp_dict["confidence"] = confidence
    temp_dict["diameter"] = diameter
    temp_dict["ellipse_axis_a"] = ellipse_axis_a
    temp_dict["ellipse_axis_b"] = ellipse_axis_b
    temp_dict["ellipse_angle"] = ellipse_angle

    return temp_dict


def valid_config_name(name_to_be_checked):
    if str(name_to_be_checked).lower().endswith(".json") or str(name_to_be_checked).lower().endswith(".config"):
        return True
    else:
        return False


def show_config(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            if type(config_info) is dict:
                for key in config_info:
                    print(f"{key}: {config_info[key]}")
            else:
                for info in config_info:
                    print(info)
    except Exception as error:
        print(f"Error:{error}")


def show_uc(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            filter_info = config_info["filters"]
            for info in filter_info:
                print(info)
    except Exception as error:
        print(f"Error:{error}")


def show_okndc(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            detector_info = config_info["detector"]
            for key in detector_info:
                print(f"{key}: {detector_info[key]}")
    except Exception as error:
        print(f"Error:{error}")


def show_plot_info(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            for plot_title in config_info:
                print(str(plot_title).upper())
                for key in config_info[plot_title]:
                    print(f"{key}: {config_info[plot_title][key]}")
                print("")
    except Exception as error:
        print(f"Error:{error}")


def main():
    parser = argparse.ArgumentParser(prog='oknpatch',
                                     description='OKNPATCH package.')
    parser.add_argument('--version', action='version', version='4.0.1'),
    parser.add_argument("-t", dest="type_input", required=True, default=None,
                        help="issue type to fix", metavar="issue type")
    parser.add_argument("-i", dest="input_file", required=False, default=None,
                        metavar="input file to be fixed or updated")
    parser.add_argument("-d", dest="directory_input", required=False, default=None,
                        metavar="directory to be fixed or updated")
    parser.add_argument("-ow", dest="overwritten", required=False, default=None,
                        metavar="overwritten is allowed or not")
    parser.add_argument("-gi", dest="gaze_input", required=False, default=None,
                        metavar="gaze file to be referenced")
    parser.add_argument("-es", dest="extra_string", required=False, default=None,
                        metavar="extra string to be used to named update csv")
    parser.add_argument("-uc", dest="updater_config", required=False, default=None,
                        metavar="config to be used to update input csv")
    parser.add_argument("-di", dest="direction_input", required=False, default=None,
                        metavar="direction input to rerun")
    parser.add_argument("-okndc", dest="okn_detector_config", required=False, default=None,
                        metavar="config to be used to in okn detector")
    parser.add_argument("-opmdc", dest="opm_detector_config", required=False, default=None,
                        metavar="OPM detector config")
    parser.add_argument("-pi", dest="plot_info", required=False, default=None,
                        metavar="plot info")
    parser.add_argument("-ri", dest="rule_info", required=False, default=None,
                        metavar="rule info")
    parser.add_argument("-pd", dest="pupil_detector", required=False, default=None,
                        metavar="pupil detector")
    parser.add_argument("-bl", dest="buffer_length", required=False, default=None,
                        metavar="buffer length")

    args = parser.parse_args()
    type_input = args.type_input
    input_file = args.input_file
    default_extra_string = "updated_"
    default_buffer_length = 7

    if type_input:
        if str(type_input) == "trial_data_lost":
            gaze_input = args.gaze_input
            # If first input and second input are provided or not "None"
            if input_file and gaze_input:
                # Check whether any of those files is missing or not and the file name is correct or not
                file_name_array = [["trial", input_file], ["gaze", gaze_input]]
                dir_exist_array = get_file_dir_exist_array(file_name_array)
                all_file_found = True

                # Display if any of file is missing
                for exist_array in dir_exist_array:
                    if not exist_array[1]:
                        print("")
                        print(f"Error! {exist_array[2]} file is missing in {exist_array[0]}.")
                        print("")
                        all_file_found = False

                # No file is missing
                if all_file_found:
                    print("")
                    print("All necessary csv files are found.")
                    print("")
                    output_file, output_file_location, success, error = fix_trial_data_lost(input_file, gaze_input)
                    if success:
                        print(f"{output_file} is created in {output_file_location}")
                    else:
                        print(error)
            else:
                if not input_file and not gaze_input:
                    print("")
                    print(f"Necessary arguments are missing to run oknpatch:{type_input}.")
                    print("Example Usage:")
                    print("oknpatch -t trial_data_lost -i csv_to_be_fixed -gi gaze_csv_to_be_referenced")
                    print("")
                elif not input_file:
                    print("")
                    print(f"File to be fixed or updated is missing in the argument to fix {type_input} issue.")
                    print("Example Usage:")
                    print("oknpatch -t trial_data_lost -i csv_to_be_fixed -gi gaze_csv_to_be_referenced")
                    print("")
                elif not gaze_input:
                    print("")
                    print(f"Gase file input is missing to fix {type_input} issue.")
                    print("Example Usage:")
                    print("oknpatch -t trial_data_lost -i csv_to_be_fixed -gi gaze_csv_to_be_referenced")
                    print("")
        elif str(type_input) == "update":
            extra_string = args.extra_string
            updater_config = args.updater_config
            # If first input is provided or not "None"
            if input_file:
                # Check whether input file exists or not
                file_exist = os.path.isfile(input_file)
                if file_exist:
                    print("")
                    print("Input file is found.")
                    print("")
                    # Determine whether default extra_string or custom input needs to be used
                    if extra_string:
                        extra_string = str(extra_string)
                    else:
                        print("There is no extra string input to name updated_csv.")
                        extra_string = default_extra_string
                        print(f"Therefore using default extra string:{extra_string}")

                    # Determine whether build-in config or input config needs to be used
                    if updater_config:
                        valid_file_name = valid_config_name(str(updater_config))
                        if valid_file_name:
                            config_dir_exist = os.path.isfile(updater_config)
                            if config_dir_exist:
                                updater_config_location = updater_config
                            else:
                                print("Input updater config does not exist.")
                                updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                                print(f"Therefore using default updater config from package.")
                        else:
                            print(f"Input file name:{updater_config} is not a config file.")
                            print("It must be .json file or .config file.")
                            return
                    else:
                        print("There is no update config location input.")
                        updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                        print(f"Therefore using default updater config from package.")
                    output_file, output_file_location, success, error = oknpatch_update_csv(input_file,
                                                                                            extra_string,
                                                                                            updater_config_location)
                    if success:
                        print(f"{output_file} is created in {output_file_location}")
                    else:
                        print(error)
                else:
                    print(f"Input file:{input_file} does not exist.")
            else:
                print("")
                print(f"Input file to be fixed is missing to fix {type_input} issue.")
                print("oknpatch -t update -i csv_to_be_updated [-es extra_string] [-uc updater_config]")
                print("")
        elif str(type_input) == "change_direction_rerun_trial" or str(type_input) == "cdrrt":
            extra_string = args.extra_string
            updater_config = args.updater_config
            direction_input = args.direction_input
            if direction_input:
                try:
                    direction_input = int(direction_input)
                    if direction_input == -1 or direction_input == 1:
                        direction_input = None
                except ValueError:
                    if str(direction_input).lower() == "left":
                        direction_input = -1
                    elif str(direction_input).lower() == "right":
                        direction_input = 1
                    else:
                        direction_input = None
                if not direction_input:
                    print("")
                    print("Invalid direction input.")
                    print("Direction input must be 1, -1, right or left.")
                    print("")
                    return
            else:
                print("")
                print("The direction input is missing.")
                print("oknpatch -t change_direction_and_rerun -i csv_to_be_fixed -di direction_input")
                print("")
                return
            okn_detector_config = args.okn_detector_config
            if input_file and direction_input:
                # Determine whether default extra_string or custom input needs to be used
                if extra_string:
                    extra_string = str(extra_string)
                    print("Extra string input is found.")
                else:
                    extra_string = default_extra_string
                    print(f"There is no extra string input. Therefore using default extra string:{extra_string}")

                # Determine whether build-in config or input config needs to be used
                if updater_config:
                    valid_file_name = valid_config_name(str(updater_config))
                    if valid_file_name:
                        config_dir_exist = os.path.isfile(updater_config)
                        if config_dir_exist:
                            updater_config_location = updater_config
                        else:
                            print("Input updater config does not exist.")
                            updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                            print(f"Therefore using default updater config from package.")
                    else:
                        print(f"Input file name:{updater_config} is not a config file.")
                        print("It must be .json file or .config file.")
                        return
                else:
                    print("There is no update config location input.")
                    updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                    print(f"Therefore using default updater config from package.")

                if okn_detector_config:
                    valid_file_name = valid_config_name(str(okn_detector_config))
                    if valid_file_name:
                        okn_detector_config_dir_exist = os.path.isfile(okn_detector_config)
                        if okn_detector_config_dir_exist:
                            print("Input okn detector config location is found.")
                            okn_detector_config_location = okn_detector_config
                        else:
                            print("Input okn detector config does not exist.")
                            okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                            print(f"Therefore using default okn detector config from package.")
                    else:
                        print(f"Input file name:{okn_detector_config} is not a config file.")
                        print("It must be .json file or .config file.")
                        return
                else:
                    print("There is no update config location input.")
                    okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                    print(f"Therefore using default updater config from package.")

                result_folder_dir, success, error = change_direction_and_rerun(input_file, direction_input,
                                                                               extra_string, updater_config_location,
                                                                               okn_detector_config_location)
                if success:
                    print(f"Rerunning is successful and result folder is created in {result_folder_dir}.")
                else:
                    print(f"Rerunning is unsuccessful.")
                    if error:
                        print(error)
            else:
                print("")
                print("The csv file to be fixed is missing.")
                print("oknpatch -t change_direction_and_rerun -i csv_to_be_fixed -di direction_input")
                print("")

        elif str(type_input) == "rerun_recording" or str(type_input) == "rrr":
            directory_input = args.directory_input
            if directory_input is None:
                print("")
                print("The directory to be rerun is missing in the commandline.")
                print("oknpatch -t rerun_recording -d directory_to_be_rerun")
                print("(or)")
                print("oknpatch -t rrr -d directory_to_be_rerun")
                print("")
                return
            overwritten = args.overwritten
            if overwritten is not None:
                overwritten_indicators = ["yes", "y", "1", "allow"]
                if str(overwritten).lower() in overwritten_indicators:
                    overwritten = True
                else:
                    overwritten = False
            else:
                overwritten = False
            pupil_detector = args.pupil_detector
            if pupil_detector is not None:
                print("pupil detector input is found.")
                valid_pupil_detector_on_indicators = ["on", "y", "1", "true"]
                if str(pupil_detector).lower() in valid_pupil_detector_on_indicators:
                    pupil_detector = True
                    print(f"Rerun recording will be rerun with pupil detector.")
                else:
                    pupil_detector = False
                    print(f"Rerun recording will be rerun without pupil detector.")
                    print("Add -pd on in the command line to turn on pupil detector.")
            else:
                pupil_detector = False
                print(f"Rerun recording will be rerun without pupil detector.")
                print("Add -pd on in the command line to turn on pupil detector.")
            buffer_length = args.buffer_length
            if buffer_length is not None:
                try:
                    buffer_length = int(buffer_length)
                    if pupil_detector:
                        print("There is buffer length input.")
                        print(f"Pupil detector will be using Tiny Fill Buffer with length:{buffer_length}.")
                except ValueError:
                    buffer_length = default_buffer_length
                    if pupil_detector:
                        print("There is buffer length input.")
                        print("Invalid buffer length input.")
                        print(f"Pupil detector will be using Tiny Fill Buffer with default length:{buffer_length}.")
            else:
                buffer_length = default_buffer_length
                if pupil_detector:
                    print("There is no buffer length input.")
                    print(f"Pupil detector will be using Tiny Fill Buffer with default length:{buffer_length}.")
            extra_string = args.extra_string
            updater_config = args.updater_config
            direction_input = args.direction_input
            if direction_input:
                try:
                    direction_input = int(direction_input)
                    if direction_input == -1 or direction_input == 1:
                        direction_input = None
                except ValueError:
                    if str(direction_input).lower() == "left":
                        direction_input = -1
                    elif str(direction_input).lower() == "right":
                        direction_input = 1
                    else:
                        direction_input = None
                if not direction_input:
                    print("")
                    print("Invalid direction input.")
                    print("Therefore, direction will be set according to the summary csv.")
                    print("")
            else:
                print("")
                print("There is no direction input.")
                print("Therefore, direction will be set according to the summary csv.")
                print("")

            okn_detector_config = args.okn_detector_config
            opm_detector_config = args.opm_detector_config

            if extra_string:
                extra_string = str(extra_string)
            else:
                extra_string = default_extra_string

            if updater_config:
                valid_file_name = valid_config_name(str(updater_config))
                if valid_file_name:
                    config_dir_exist = os.path.isfile(updater_config)
                    if config_dir_exist:
                        print("Input updater config config location is found.")
                        updater_config_location = updater_config
                    else:
                        print("Input updater config does not exist.")
                        updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                        print(f"Therefore using default updater config from package.")
                else:
                    print(f"Input updater config:{updater_config} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no update config location input.")
                updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                print(f"Therefore using default updater config from package.")

            if okn_detector_config:
                valid_file_name = valid_config_name(str(okn_detector_config))
                if valid_file_name:
                    okn_detector_config_dir_exist = os.path.isfile(okn_detector_config)
                    if okn_detector_config_dir_exist:
                        print("Input okn detector config location is found.")
                        okn_detector_config_location = okn_detector_config
                    else:
                        print("Input okn detector config does not exist.")
                        okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                        print(f"Therefore using default okn detector config from package.")
                else:
                    print(f"Input okn detector config:{okn_detector_config} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no okn detector config location input.")
                okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                print(f"Therefore using default okn detector config from package.")

            if opm_detector_config:
                valid_file_name = valid_config_name(str(opm_detector_config))
                if valid_file_name:
                    okn_detector_config_dir_exist = os.path.isfile(opm_detector_config)
                    if okn_detector_config_dir_exist:
                        print("Input opm detector config location is found.")
                        opm_detector_config_location = opm_detector_config
                    else:
                        print("Input opm detector config does not exist.")
                        opm_detector_config_location = get_config_location("oknpatch", "opm_detector_config.json")
                        print(f"Therefore using default opm detector config from package.")
                else:
                    print(f"Input opm detector config:{opm_detector_config} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no opm detector config location input.")
                opm_detector_config_location = get_config_location("oknpatch", "opm_detector_config.json")
                print(f"Therefore using default opm detector config from package.")

            plot_info = args.plot_info
            if plot_info:
                valid_file_name = valid_config_name(str(plot_info))
                if valid_file_name:
                    plot_info_exist = os.path.isfile(plot_info)
                    if plot_info_exist:
                        print("Input plot info location is found.")
                        plot_info_location = plot_info
                    else:
                        print("Input plot info does not exist.")
                        plot_info_location = get_config_location("oknpatch", "oknserver_graph_plot_config.json")
                        print(f"Therefore using default plot info from package.")
                else:
                    print(f"Input plot info:{plot_info} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no plot info location input.")
                plot_info_location = get_config_location("oknpatch", "oknserver_graph_plot_config.json")
                print(f"Therefore using default plot info from package.")

            rule_info = args.rule_info
            if rule_info:
                valid_file_name = valid_config_name(str(rule_info))
                if valid_file_name:
                    rule_info_exist = os.path.isfile(rule_info)
                    if rule_info_exist:
                        print("Input rule info location is found.")
                        rule_info_location = rule_info
                    else:
                        print("Input rule info does not exist.")
                        rule_info_location = get_config_location("oknpatch", "okn_detection_rule.json")
                        print(f"Therefore using default rule info from package.")
                else:
                    print(f"Input rule info:{rule_info} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no rule info location input.")
                rule_info_location = get_config_location("oknpatch", "okn_detection_rule.json")
                print(f"Therefore using default rule info from package.")

            success, error, rerun_folder_dir = rerun_recording(directory_input, opm_detector_config_location,
                                                               extra_string,
                                                               updater_config_location,
                                                               direction_input, okn_detector_config_location,
                                                               plot_info_location, rule_info_location,
                                                               overwritten, pupil_detector, buffer_length)
            if success:
                print(f"Rerun recording is successful and all the rerun data will be in {rerun_folder_dir}.")
            else:
                print(f"Rerun recording is unsuccessful.")
                if error:
                    print(error)
        elif str(type_input) == "fix_neon_csv_and_rerun" or str(type_input) == "fncar":
            directory_input = args.directory_input
            okn_detector_config = args.okn_detector_config
            extra_string = args.extra_string
            updater_config = args.updater_config
            plot_info = args.plot_info
            rule_info = args.rule_info
            if directory_input is None:
                print("")
                print("The directory to be rerun is missing in the commandline.")
                print("oknpatch -t fix_neon_csv_and_rerun -d directory_to_be_rerun")
                print("(or)")
                print("oknpatch -t fncar -d directory_to_be_rerun")
                print("")
                return

            is_it_pnm_recording = is_pnm_recording(directory_input)
            if not is_it_pnm_recording:
                print("")
                print("This recording is not PNM recording.")
                print("")
                return

            if okn_detector_config:
                valid_file_name = valid_config_name(str(okn_detector_config))
                if valid_file_name:
                    okn_detector_config_dir_exist = os.path.isfile(okn_detector_config)
                    if okn_detector_config_dir_exist:
                        print("Input okn detector config location is found.")
                        okn_detector_config_location = okn_detector_config
                    else:
                        print("Input okn detector config does not exist.")
                        okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                        print(f"Therefore using default okn detector config from package.")
                else:
                    print(f"Input okn detector config:{okn_detector_config} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no okn detector config location input.")
                okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                print(f"Therefore using default okn detector config from package.")

            if extra_string:
                extra_string = str(extra_string)
            else:
                extra_string = default_extra_string

            if updater_config:
                valid_file_name = valid_config_name(str(updater_config))
                if valid_file_name:
                    config_dir_exist = os.path.isfile(updater_config)
                    if config_dir_exist:
                        print("Input updater config config location is found.")
                        updater_config_location = updater_config
                    else:
                        print("Input updater config does not exist.")
                        updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                        print(f"Therefore using default updater config from package.")
                else:
                    print(f"Input updater config:{updater_config} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no update config location input.")
                updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                print(f"Therefore using default updater config from package.")

            if plot_info:
                valid_file_name = valid_config_name(str(plot_info))
                if valid_file_name:
                    plot_info_exist = os.path.isfile(plot_info)
                    if plot_info_exist:
                        print("Input plot info location is found.")
                        plot_info_location = plot_info
                    else:
                        print("Input plot info does not exist.")
                        plot_info_location = get_config_location("oknpatch", "oknserver_graph_plot_config.json")
                        print(f"Therefore using default plot info from package.")
                else:
                    print(f"Input plot info:{plot_info} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no plot info location input.")
                plot_info_location = get_config_location("oknpatch", "oknserver_graph_plot_config.json")
                print(f"Therefore using default plot info from package.")

            if rule_info:
                valid_file_name = valid_config_name(str(rule_info))
                if valid_file_name:
                    rule_info_exist = os.path.isfile(rule_info)
                    if rule_info_exist:
                        print("Input rule info location is found.")
                        rule_info_location = rule_info
                    else:
                        print("Input rule info does not exist.")
                        rule_info_location = get_config_location("oknpatch", "okn_detection_rule.json")
                        print(f"Therefore using default rule info from package.")
                else:
                    print(f"Input rule info:{rule_info} is not a config file.")
                    print("It must be .json file or .config file.")
                    return
            else:
                print("There is no rule info location input.")
                rule_info_location = get_config_location("oknpatch", "okn_detection_rule.json")
                print(f"Therefore using default rule info from package.")

            success, error, rerun_folder_dir = fix_neon_csv_and_rerun(directory_input, extra_string,
                                                                      updater_config_location,
                                                                      okn_detector_config_location,
                                                                      plot_info_location, rule_info_location)
            if success:
                print(f"Fixing Neon Csv and Rerun is successful and all the rerun data will be in {rerun_folder_dir}.")
            else:
                print(f"Fixing Neon Csv and Rerun is unsuccessful.")
                if error:
                    print(error)
        elif "show" in str(type_input):
            try:
                _, flag = str(type_input).split("=")
                if flag == "uc":
                    print("Default Updater Config Info")
                    updater_config_location = get_config_location("oknpatch", "gazefilters.json")
                    show_uc(updater_config_location)
                elif flag == "okndc":
                    print("Default OKN Detector Config Info")
                    okn_detector_config_location = get_config_location("oknpatch", "okndetector.gaze.config")
                    show_okndc(okn_detector_config_location)
                elif flag == "opmdc":
                    print("Default OPM Detector Config Info")
                    opm_detector_config_location = get_config_location("oknpatch", "opm_detector_config.json")
                    show_config(opm_detector_config_location)
                elif flag == "pi":
                    print("Default Plot Info")
                    plot_info_location = get_config_location("oknpatch", "oknserver_graph_plot_config.json")
                    show_plot_info(plot_info_location)
                elif flag == "ri":
                    print("Default Rule Info")
                    rule_info_location = get_config_location("oknpatch", "okn_detection_rule.json")
                    show_config(rule_info_location)
                elif flag == "es":
                    print(f"Default Extra String = \"{default_extra_string}\".")
                elif flag == "bl":
                    print(f"Default Buffer Length = \"{default_buffer_length}\".")
                elif flag == "ow":
                    print(f"Default Overwritten Flag = \"False\".")
                elif flag == "pd":
                    print(f"Default Using Pupil Detector Flag = \"False\".")
                else:
                    print(f"Invalid flag name.")
            except ValueError:
                print("Invalid show type message.")
                print("It must be joined with \"=\". Example:\"show=uc\".")
                return
        else:
            print(f"Invalid issue type: {type_input}")
    else:
        print("There is no type input -t.")

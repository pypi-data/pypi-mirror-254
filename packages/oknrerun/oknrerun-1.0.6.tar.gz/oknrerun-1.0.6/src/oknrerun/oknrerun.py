import csv
import os
import argparse
import importlib.metadata
from importlib.resources import files
import cv2
import shutil
import commentjson
from ehdg_tools.ehdg_updater import update_csv
from ehdg_tools.ehdg_okn_checker import detect_with_okn_detector, signal_checker, apply_okn_detection_rule
from ehdg_tools.ehdg_buffers import TinyFillBuffer
from ehdg_tools.ehdg_plotter import get_folder_info_from_summary_csv
from ehdg_tools.ehdg_functions import check_commandline_program
from ehdg_pupil_detector import ehdg_pupil_detector


# from oknrerun.ui import start_rerun_ui

# This function is to get built-in config location with new library (from importlib.resources import files)
def get_config_location(module_name, config_file_name):
    config_dir = files(module_name).joinpath(config_file_name)
    return str(config_dir)


# This function is print normal config information
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


# This function is print updater config information
# This is separate function because we only want to see filters info from it
def show_uc(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            filter_info = config_info["filters"]
            for info in filter_info:
                print(info)
    except Exception as error:
        print(f"Error:{error}")


# This function is print updater config information
# This is separate function because we only want to see detector info from it
def show_okndc(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            detector_info = config_info["detector"]
            for key in detector_info:
                print(f"{key}: {detector_info[key]}")
    except Exception as error:
        print(f"Error:{error}")


# This function is print updater config information
# This is separate function because we only want to see individual plot info from it
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


# This function to get non overlapped folder name from input recording directory
def get_rerun_folder_dir(recording_dir):
    folder_name = os.path.basename(recording_dir)

    if "_rerun" in folder_name:
        string_array = str(folder_name).split("_")
        last_string = string_array[-1]
        extra_number = 0
        if "rerun" in last_string:
            extra_string = str(last_string).replace("rerun", "", 1)
            print(f"\"{extra_string}\"")
            if extra_string == "":
                checking_name = "rerun1"
            else:
                try:
                    extra_number = int(extra_string)
                    print(extra_number)
                    extra_number += 1
                    checking_name = f"rerun{extra_number}"
                except ValueError:
                    return f"{folder_name}_rerun"
            string_array[-1] = checking_name
            new_folder_name = "_".join(string_array)
            temp_dir = str(recording_dir).replace(folder_name, new_folder_name)
        else:
            checking_name = "rerun"
            string_array.append(checking_name)
            new_folder_name = "_".join(string_array)
            temp_dir = str(recording_dir).replace(folder_name, new_folder_name)

        while True:
            if os.path.isdir(temp_dir):
                extra_number += 1
                checking_name = f"rerun{extra_number}"
                string_array[-1] = checking_name
                new_folder_name = "_".join(string_array)
                temp_dir = str(recording_dir).replace(folder_name, new_folder_name)
            else:
                return temp_dir
    else:
        string_array = str(folder_name).split("_")
        checking_name = "rerun"
        string_array.append(checking_name)
        new_folder_name = "_".join(string_array)
        temp_dir = str(recording_dir).replace(folder_name, new_folder_name)

        extra_number = 0
        while True:
            if os.path.isdir(temp_dir):
                extra_number += 1
                checking_name = f"rerun{extra_number}"
                string_array[-1] = checking_name
                new_folder_name = "_".join(string_array)
                temp_dir = str(recording_dir).replace(folder_name, new_folder_name)
            else:
                return temp_dir


# This function is to check the config file type is valid or not
def valid_config_name(name_to_be_checked):
    if str(name_to_be_checked).lower().endswith(".json") or str(name_to_be_checked).lower().endswith(".config"):
        return True
    else:
        return False


# This function is copy all the data inside from the input directory excluding the folder from ignore folder array.
# It ignores to copy the files inside, but it creates the directory for it.
# Because we do not want to copy unnecessary files.
def copy_folder_with_ignore_folder(copy_dir, paste_dir, ignore_folder_array):
    file_folder_list = os.listdir(copy_dir)
    for file_folder in file_folder_list:
        first_letter = str(file_folder).lower()[0]
        if first_letter == ".":
            pass
        else:
            copy_path = os.path.join(copy_dir, file_folder)
            paste_path = os.path.join(paste_dir, file_folder)
            if file_folder in ignore_folder_array and os.path.isdir(copy_path):
                os.mkdir(paste_path)
            else:
                if os.path.isdir(copy_path):
                    shutil.copytree(copy_path, paste_path)
                else:
                    shutil.copy(copy_path, paste_path)

    return paste_dir


# opmdc = opm_detector_config_location, es = extra_string, uc = updater_config_location,
# di = direction_input, okndc = okn_detector_config_location,
# pil = plot info location, ril = rule info location, pdt = pupil detector type
# scd = summary csv dir
def rerun_recording(folder_dir, data_info_array_input, opmdc, es, uc, di, okndc, pil, ril,
                    scd, using_pupil_detector=False, pdt="opm", buffer_length_input=7):
    error_string = None

    # If user uses pupil detector then retrieve detector info from its config
    if using_pupil_detector:
        if pdt == "opm":
            rerun_detector = ehdg_pupil_detector.Detector()
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
        else:
            print("Only opm is available for now.")
            print("Therefore, stopping the process.")
            return
    else:
        rerun_detector = None

    # Retrieving plot info to redraw trial and summary plots
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

                signal_csv_folder_name = trial_plot_info["signal_csv_folder_name"]
                signal_csv_name = trial_plot_info["signal_csv_name"]
            except KeyError:
                print(f"Error in retrieving plot info from config file:{pil}!")
                return False, str(KeyError)
    except Exception as error:
        print(f"Error in retrieving plot info from config file:{pil}!")
        return False, error

    # Retrieving rule info to reapply in making decision of whether there is okn or not
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
                    rule_to_be_applied = config_info["rule"]
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

    # Getting trials folder directory from input directory
    rerun_trials_folder_dir = os.path.join(folder_dir, "trials")
    gaze_csv_dir = os.path.join(folder_dir, "gaze.csv")

    # This array is to collect the trial info and rewrite the summary csv
    rerun_summary_csv_info = []
    for data_info in data_info_array_input:
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
        trial_folder_dir = os.path.join(rerun_trials_folder_dir, trial_name)
        rerun_buffer = TinyFillBuffer(buffer_length_input)
        if not os.path.isdir(trial_folder_dir):
            print(f"Folder directory: {trial_folder_dir} could not be found.")
            return
        # Redetecting with pupil detector if the user want to use it
        if using_pupil_detector:
            rerun_trial_csv_dir = rerun_trial_with_pupil_detector(rerun_detector, rerun_buffer, trial_folder_dir,
                                                                  event_id, direction)
        else:
            trial_csv_name = f"{trial_name}.csv"
            rerun_trial_csv_dir = os.path.join(trial_folder_dir, trial_csv_name)

        # Re-updating, redetecting with okn detector and reapplying rules
        updated_csv = update_csv(rerun_trial_csv_dir, es, uc)
        is_there_detector = check_commandline_program("okndetector")
        if is_there_detector:
            signal_output_dir = detect_with_okn_detector(updated_csv, okndc)
        else:
            raise FileNotFoundError("OKN detector cannot be found.")
        signal_data = signal_checker(signal_output_dir, signal_csv_name)
        temp_dict["min_chain_length_rule"] = min_chain_length
        temp_dict["min_unchained_okn_rule"] = min_unchained_okn
        temp_dict["max_chain_length_signal_data"] = signal_data["max_chain_length"]
        temp_dict["unchained_okn_total_signal_data"] = signal_data["unchained_okn_total"]
        is_there_okn = apply_okn_detection_rule(signal_data, min_chain_length, min_unchained_okn)
        temp_dict["okn"] = is_there_okn
        okn_matlab = 1 if is_there_okn else 0
        temp_dict["okn_matlab"] = okn_matlab

        # Collecting rerun trial info
        rerun_summary_csv_info.append(temp_dict)

        # Redrawing trial plot
        trial_plot_cmd = f"okntool -t trial -d {trial_folder_dir} -c {pil} -gc {gaze_csv_dir}"
        os.system(trial_plot_cmd)

    summary_csv_name = os.path.basename(scd)
    rerun_summary_csv_dir = os.path.join(rerun_trials_folder_dir, summary_csv_name)

    # Retrieving header names
    rerun_header_array = []
    if rerun_summary_csv_info:
        for header in rerun_summary_csv_info[0]:
            rerun_header_array.append(header)
    else:
        print("There is no info in rerun summary csv info array.")
        return False, error_string

    # Rewriting summary csv with rerun trial info
    rewrite_summary_csv(rerun_summary_csv_dir, rerun_summary_csv_info, rerun_header_array)

    # Redrawing summary plot
    summary_plot_cmd = f"okntool -t summary -d {rerun_trials_folder_dir} -c {pil} -gc {gaze_csv_dir}"
    os.system(summary_plot_cmd)

    return True, error_string, folder_dir


# This function is to redetect with pupil detector by given detector and tiny fill buffer
def redetect(detector, buffer, trial_video, output_csv_dir, event_id_input, direction_input):
    print(os.path.basename(trial_video))
    cap = cv2.VideoCapture(trial_video)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    print(f"frame_rate:{frame_rate}")
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(f"frame_width:{frame_width}")
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"frame_height:{frame_height}")
    frame_count = 0

    print("")
    print(f"Rerunning {trial_video} with detector")
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


# This function is to rewrite the summary csv
def rewrite_summary_csv(csv_dir, info_array, header_array):
    with open(csv_dir, mode='w', newline="") as destination_file:
        header_names = header_array
        csv_writer = csv.DictWriter(destination_file, fieldnames=header_names)
        csv_writer.writeheader()

        for info in info_array:
            csv_writer.writerow(info)
        destination_file.close()


# This function is create the data dict by given data, frame info, event id and trial direction
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


# This folder to organize the process before redetecting with pupil detector
def rerun_trial_with_pupil_detector(detector, buffer, trial_folder_dir, event_id_input, direction_input):
    if not detector:
        print("Input detector is None.")
        return
    trial_name = os.path.basename(trial_folder_dir)
    trial_video_name = f"{trial_name}_cropped.mp4"
    trial_video_dir = os.path.join(trial_folder_dir, trial_video_name)
    if not os.path.isfile(trial_video_dir):
        print(f"Trial video: {trial_video_name} could not be found.")
        return
    output_csv_dir = os.path.join(trial_folder_dir, f"{trial_name}.csv")
    redetect(detector, buffer, trial_video_dir, output_csv_dir, event_id_input, direction_input)

    return output_csv_dir


# This function is to find the file name in the config folder
def get_config_name(config_folder_input, search_string, search_string_two=None):
    file_list = os.listdir(config_folder_input)
    if search_string_two:
        for file_name in file_list:
            if str(search_string) in str(file_name) or str(search_string_two) in str(file_name):
                file_path = os.path.join(config_folder_input, file_name)
                if os.path.isfile(file_path):
                    return str(file_name)
    else:
        for file_name in file_list:
            if str(search_string) in str(file_name):
                file_path = os.path.join(config_folder_input, file_name)
                if os.path.isfile(file_path):
                    return str(file_name)
    return "nothing"


def main():
    parser = argparse.ArgumentParser(prog='oknrerun',
                                     description='OKNRERUN package.')
    oknrerun_version = importlib.metadata.version('oknrerun')
    parser.add_argument('--version', action='version', version=oknrerun_version),
    parser.add_argument("--display", dest="display", required=False, default=None,
                        metavar="display config or defaults")
    parser.add_argument("-d", dest="directory_input", required=False, default=None,
                        metavar="directory to be fixed or updated")
    parser.add_argument("-okndc", dest="okn_detector_config", required=False, default=None,
                        metavar="config to be used to in okn detector")
    parser.add_argument("-pd", dest="pupil_detector", required=False, default=None,
                        metavar="pupil detector")
    parser.add_argument("-bl", dest="buffer_length", required=False, default=None,
                        metavar="buffer length")
    parser.add_argument("-opmdc", dest="opm_detector_config", required=False, default=None,
                        metavar="OPM detector config")
    parser.add_argument("-uc", dest="updater_config", required=False, default=None,
                        metavar="config to be used to update input csv")
    parser.add_argument("-es", dest="extra_string", required=False, default=None,
                        metavar="extra string to be used to named update csv")
    parser.add_argument("-di", dest="direction_input", required=False, default=None,
                        metavar="direction input to rerun")
    parser.add_argument("-ri", dest="rule_info", required=False, default=None,
                        metavar="rule info")
    parser.add_argument("-pi", dest="plot_info", required=False, default=None,
                        metavar="plot info")

    args = parser.parse_args()
    # checking whether just display config or rerun
    display = args.display
    default_extra_string = "updated_"
    default_buffer_length = 7
    default_pupil_detector_type = "opm"
    if display is None:
        directory_input = args.directory_input
        if directory_input is None:
            print("There is no directory input.")
            print("Please use flag -d to input recording folder directory.")
            return
        else:
            if not os.path.isdir(str(directory_input)):
                print(f"Invalid directory input: {str(directory_input)}")
                return
            else:
                directory_input = str(directory_input)
                config_folder_dir = os.path.join(directory_input, "config")
                if os.path.isdir(config_folder_dir):
                    print("Config folder is found.")
                else:
                    print("Config folder could not be found.")
                    return

                    # Get new folder name which will not overwrite existing folders
        rerun_folder_dir = get_rerun_folder_dir(str(directory_input))

        # Ignore folders so that it will not copy unnecessary files
        ignore_folder_array = ["config", "trials"]

        # Copy all files but ignore config and trials folders
        rerun_folder_dir = copy_folder_with_ignore_folder(str(directory_input), rerun_folder_dir, ignore_folder_array)

        # Check whether summary csv is there or not.
        # If not, ask user to give the file link and continue.
        # If user gives invalid link, then stop the process.
        summary_csv_dir = os.path.join(str(directory_input), "trials", "okn_detector_summary.csv")
        if not os.path.isfile(summary_csv_dir):
            print(f"Expected summary csv: {summary_csv_dir} could not be found.")
            new_summary_csv_dir = input("Please link for summary csv here: ")
            valid_csv_name = str(os.path.basename(summary_csv_dir)).endswith(".csv")
            new_summary_csv_dir_exist = os.path.isfile(new_summary_csv_dir)
            if not new_summary_csv_dir_exist:
                print(f"Input summary csv: {new_summary_csv_dir_exist} could not be found.")
                print("Therefore, stopping the process.")
                return
            else:
                if not valid_csv_name:
                    print("File is found but it is not csv file.")
                    print("Therefore, stopping the process.")
                    return
                else:
                    summary_csv_dir = new_summary_csv_dir

        # Get all info from summary csv
        data_info_array = get_folder_info_from_summary_csv(summary_csv_dir)

        # check all inputs and handle accordingly
        pupil_detector = args.pupil_detector
        pupil_detector_type = default_pupil_detector_type
        if pupil_detector is not None:
            print("pupil detector input is found.")
            valid_pupil_detector_input = ["opm", "on", "y", "1", "true"]
            if str(pupil_detector).lower() in valid_pupil_detector_input:

                available_pupil_detector_types = ["opm"]
                if str(pupil_detector).lower() in available_pupil_detector_types:
                    print(f"Rerunning with pupil detector: {pupil_detector}.")
                    pupil_detector_type = pupil_detector
                else:
                    print(f"Pupil detector input does not include "
                          f"specific pupil detector or could not be found.")
                    print(f"Therefore, rerunning with default pupil detector: opm.")
                pupil_detector = True
            else:
                print(f"Invalid pupil detector command or type input.")
                print(f"Valid input are {valid_pupil_detector_input}.")
                continue_or_not = input("Would you like to rerun without using pupil detector? y/n  ")
                if str(continue_or_not).lower() == "y":
                    pupil_detector = False
                    print(f"Rerunning without pupil detector.")
                    print("Add -pd flag in the command line to use pupil detector.")
                else:
                    print(f"Stopping the process.")
                    return
        else:
            pupil_detector = False
            print(f"Rerunning without pupil detector.")
            print("Add -pd flag in the command line to use pupil detector.")
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
                    print(f"There is buffer length input but it is invalid: {buffer_length}.")
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
                    updater_config_location = get_config_location("oknrerun", "gazefilters.json")
                    print(f"Therefore using built-in updater config from package.")
            else:
                print(f"Input updater config:{updater_config} is not a config file.")
                print("It must be .json file or .config file.")
                return
        else:
            updater_config_name = get_config_name(config_folder_dir, "gazefilter")
            updater_config_location = os.path.join(config_folder_dir, updater_config_name)
            if os.path.isfile(updater_config_location):
                print(f"Using updater config from {updater_config_location}.")
            else:
                print("There is no updater config input and cannot be found in config folder.")
                updater_config_location = get_config_location("oknrerun", "gazefilters.json")
                print(f"Therefore using built-in updater config from package.")

        if okn_detector_config:
            valid_file_name = valid_config_name(str(okn_detector_config))
            if valid_file_name:
                okn_detector_config_dir_exist = os.path.isfile(okn_detector_config)
                if okn_detector_config_dir_exist:
                    print("Input okn detector config location is found.")
                    okn_detector_config_location = okn_detector_config
                else:
                    print("Input okn detector config does not exist.")
                    okn_detector_config_location = get_config_location("oknrerun", "okndetector.gaze.config")
                    print(f"Therefore using built-in okn detector config from package.")
            else:
                print(f"Input okn detector config:{okn_detector_config} is not a config file.")
                print("It must be .json file or .config file.")
                return
        else:
            detector_config_name = get_config_name(config_folder_dir, "okndetector")
            okn_detector_config_location = os.path.join(config_folder_dir, detector_config_name)
            if os.path.isfile(okn_detector_config_location):
                print(f"Using detector config from {okn_detector_config_location}.")
            else:
                print("There is no detector config input and cannot be found in config folder.")
                okn_detector_config_location = get_config_location("oknrerun", "okndetector.gaze.config")
                print(f"Therefore using built-in okn detector config from package.")

        if opm_detector_config:
            valid_file_name = valid_config_name(str(opm_detector_config))
            if valid_file_name:
                okn_detector_config_dir_exist = os.path.isfile(opm_detector_config)
                if okn_detector_config_dir_exist:
                    print("Input opm detector config location is found.")
                    opm_detector_config_location = opm_detector_config
                else:
                    print("Input opm detector config does not exist.")
                    opm_detector_config_location = get_config_location("oknrerun", "opm_detector_config.json")
                    print(f"Therefore using default opm detector config from package.")
            else:
                print(f"Input opm detector config:{opm_detector_config} is not a config file.")
                print("It must be .json file or .config file.")
                return
        else:
            opm_detector_config_location = get_config_location("oknrerun", "opm_detector_config.json")
            if pupil_detector:
                print("There is no opm detector config location input.")
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
                    plot_info_location = get_config_location("oknrerun", "oknserver_graph_plot_config.json")
                    print(f"Therefore using default plot info from package.")
            else:
                print(f"Input plot info:{plot_info} is not a config file.")
                print("It must be .json file or .config file.")
                return
        else:
            plot_config_name = get_config_name(config_folder_dir, "plot")
            plot_info_location = os.path.join(config_folder_dir, plot_config_name)
            if os.path.isfile(plot_info_location):
                print(f"Using plot config from {plot_info_location}.")
            else:
                print("There is no plot config input and cannot be found in config folder.")
                plot_info_location = get_config_location("oknrerun", "oknserver_graph_plot_config.json")
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
                    rule_info_location = get_config_location("oknrerun", "okn_detection_rule.json")
                    print(f"Therefore using default rule info from package.")
            else:
                print(f"Input rule info:{rule_info} is not a config file.")
                print("It must be .json file or .config file.")
                return
        else:
            rule_info_name = get_config_name(config_folder_dir, "oknserver_config", "rule")
            rule_info_location = os.path.join(config_folder_dir, rule_info_name)
            if os.path.isfile(rule_info_location):
                print(f"Using rule info from {rule_info_location}.")
            else:
                print("There is no rule info input and cannot be found in config folder.")
                rule_info_location = get_config_location("oknrerun", "okn_detection_rule.json")
                print(f"Therefore using default rule info from package.")

        # copy config files which will be used in the process into config folder
        config_folder_dir = os.path.join(rerun_folder_dir, "config")
        shutil.copy(updater_config_location, os.path.join(config_folder_dir,
                                                          os.path.basename(updater_config_location)))
        shutil.copy(okn_detector_config_location, os.path.join(config_folder_dir,
                                                               os.path.basename(okn_detector_config_location)))
        shutil.copy(plot_info_location, os.path.join(config_folder_dir, os.path.basename(plot_info_location)))
        shutil.copy(rule_info_location, os.path.join(config_folder_dir, os.path.basename(rule_info_location)))
        if pupil_detector:
            shutil.copy(opm_detector_config_location, os.path.join(config_folder_dir,
                                                                   os.path.basename(opm_detector_config_location)))

        # copy file from directory input
        copy_trials_dir = os.path.join(str(directory_input), "trials")
        paste_trials_dir = os.path.join(rerun_folder_dir, "trials")
        for data_info in data_info_array:
            trial_id = data_info["trial_id"]
            disk_condition = data_info["disk_condition"]
            trial_name = f"{trial_id}_{disk_condition}"
            paste_trial_folder_dir = os.path.join(paste_trials_dir, trial_name)
            if not os.path.isdir(paste_trial_folder_dir):
                os.mkdir(paste_trial_folder_dir)

        if pupil_detector:
            # If using pupil detector, check whether there is trial video or not
            # If not, create trial videos in rerun trials folder
            # If yes, just copy videos into rerun trials folder

            all_videos_found = True
            for data_info in data_info_array:
                trial_id = data_info["trial_id"]
                disk_condition = data_info["disk_condition"]
                trial_name = f"{trial_id}_{disk_condition}"
                trial_video_name = f"{trial_name}_cropped.mp4"
                trial_video_dir = os.path.join(copy_trials_dir, trial_name, trial_video_name)
                if not os.path.isfile(trial_video_dir):
                    all_videos_found = False
                    break

            if all_videos_found:
                print("Split videos are found in input trial folders")
                print("Therefore, copying those videos into rerun trials folder")
                for data_info in data_info_array:
                    trial_id = data_info["trial_id"]
                    disk_condition = data_info["disk_condition"]
                    trial_name = f"{trial_id}_{disk_condition}"
                    trial_video_name = f"{trial_name}_cropped.mp4"
                    trial_video_dir = os.path.join(copy_trials_dir, trial_name, trial_video_name)
                    paste_trial_folder_dir = os.path.join(paste_trials_dir, trial_name)
                    if not os.path.isdir(paste_trial_folder_dir):
                        os.mkdir(paste_trial_folder_dir)
                    paste_video_dir = os.path.join(paste_trial_folder_dir, trial_video_name)
                    shutil.copy(trial_video_dir, paste_video_dir)
            else:
                print("Split videos are not found in input trial folders")
                print("Starting splitting the video.")
                print("Checking whether there is okntool in this computer or not.")
                is_there_okntool = check_commandline_program("okntool")
                if is_there_okntool:
                    split_video_cmd = f"okntool -t sv -d {str(rerun_folder_dir)}"
                    os.system(split_video_cmd)
                else:
                    print("Please install or upgrade okntool first then rerun this process.")
                    print("pip install okntool -U")
                    return
        else:
            # If running without pupil detector then copy individual trial csv to rerun trial folders
            for data_info in data_info_array:
                trial_id = data_info["trial_id"]
                disk_condition = data_info["disk_condition"]
                trial_name = f"{trial_id}_{disk_condition}"
                trial_csv_name = f"{trial_name}.csv"
                trial_csv_dir = os.path.join(copy_trials_dir, trial_name, trial_csv_name)
                if not os.path.isfile(trial_csv_dir):
                    print(f"{trial_csv_dir} could not be found.")
                    return
                paste_trial_folder_dir = os.path.join(paste_trials_dir, trial_name)
                if not os.path.isdir(paste_trial_folder_dir):
                    os.mkdir(paste_trial_folder_dir)
                paste_csv_dir = os.path.join(paste_trial_folder_dir, trial_csv_name)
                shutil.copy(trial_csv_dir, paste_csv_dir)

        success, error, rerun_folder_dir = rerun_recording(rerun_folder_dir, data_info_array,
                                                           opm_detector_config_location,
                                                           extra_string, updater_config_location,
                                                           direction_input, okn_detector_config_location,
                                                           plot_info_location, rule_info_location,
                                                           summary_csv_dir, pupil_detector,
                                                           pupil_detector_type, buffer_length)
        if success:
            print(f"Rerun recording is successful and all the rerun data will be in {rerun_folder_dir}.")
        else:
            print(f"Rerun recording is unsuccessful.")
            if error:
                print(error)
    else:
        display_flag = str(display)
        if display_flag == "uc":
            print("Default Updater Config Info")
            updater_config_location = get_config_location("oknrerun", "gazefilters.json")
            show_uc(updater_config_location)
        elif display_flag == "okndc":
            print("Default OKN Detector Config Info")
            okn_detector_config_location = get_config_location("oknrerun", "okndetector.gaze.config")
            show_okndc(okn_detector_config_location)
        elif display_flag == "opmdc":
            print("Default OPM Detector Config Info")
            opm_detector_config_location = get_config_location("oknrerun", "opm_detector_config.json")
            show_config(opm_detector_config_location)
        elif display_flag == "pi":
            print("Default Plot Info")
            plot_info_location = get_config_location("oknrerun", "oknserver_graph_plot_config.json")
            show_plot_info(plot_info_location)
        elif display_flag == "ri":
            print("Default Rule Info")
            rule_info_location = get_config_location("oknrerun", "okn_detection_rule.json")
            show_config(rule_info_location)
        elif display_flag == "defaults":
            print(f"Default Extra String = \"{default_extra_string}\".")
            print(f"Default Buffer Length = \"{default_buffer_length}\".")
            print(f"Default Using Pupil Detector Flag = \"False\".")
            print(f"Default Pupil Detector Type = \"{default_pupil_detector_type}\".")
        else:
            print(f"Invalid flag name.")

# OKNPATCH PYTHON PACKAGE LIBRARY MANUAL
## Description
This program will fix or rerun the web experiment related functions.

There are 3 types of oknpatch which are:
1.  **trial_data_lost** to fix the data lost of trial csv by referencing the gaze.csv.  
2.  **update** to rerun the given trial csv by the updater function of the oknserver.  
3.  **change_direction_rerun_trial** to change direction of the trial csv and rerun the updater and okn detection.
4.  **rerun_recording** to rerun all trials with or without pupil detector.
5.  **show** to check built-in config or default.

## Installation requirements and guide
### Anaconda
To install this program, `Anaconda python distributing program` and `Anaconda Powershell Prompt` are needed.  
If you do not have `Anaconda`, please use the following links to download and install:  
Download link: https://www.anaconda.com/products/distribution  
Installation guide link: https://docs.anaconda.com/anaconda/install/  
### PIP install
To install `oknpatch`, you have to use `Anaconda Powershell Prompt`.  
After that, you can use the `oknpatch` from any command prompt.  
In `Anaconda Powershell Prompt`:
```
pip install oknpatch
```  
## Usage guide
### The usage will be depend on the type of oknpatch. 
There is a example folder under `development` folder.  
If you want to test this program, you can clone this repository, install `oknpatch` and run the following command:  
For **trial_data_lost** oknpatch type  
```
oknpatch -t trial_data_lost -i development/example/trial-2_disk-condition-1-1.csv -gi development/example/gaze.csv
```
For **update** oknpatch type  
```
oknpatch -t update -i development/example/trial-2_disk-condition-1-1.csv
```  
That will rerun the updater function of oknserver and produce `updated_trial-2_disk-condition-1-1.csv`.  
Since there is only input (-i) in the command line, it will use default `extra_string` which is "updated_" to give the output csv name and built-in config to update the given csv.  
If you want to give your custom `extra_string`, use (-es):  
If you want to use your own config to update, use (-uc):
```
oknpatch -t update -i development/example/trial-2_disk-condition-1-1.csv -es "(custom extra string)" -uc "(directory to your custom config)"
```
For **change_direction_rerun_trial** oknpatch type  
```
oknpatch -t change_direction_rerun_trial -i development/example/trial-2_disk-condition-1-1.csv -di 1 -okndl (okn_detector_location)
```
That will change the direction column value of the given csv and rerun the updater function of oknserver and produce `updated_trial-2_disk-condition-1-1.csv` and `result` folder which contains `signal.csv`.  
Since there is no input for custom extra string, config to update and config for okn detection in the command line, it will use default `extra_string` which is "updated_" to give the output csv name, built-in updater config and built-in okn detector config.  
If you want to give your custom `extra_string`, use (-es):  
If you want to use your own config to update, use (-uc):
If you want to use your own config for okn detection, use (-okndc):
```
oknpatch -t change_direction_rerun_trial -i development/example/trial-2_disk-condition-1-1.csv -es "(custom extra string)" -uc "(directory to your custom config)" -okndc "(directory to your custom okn detector config)" -di 1 -okndl (okn_detector_location)
```

For **rerun_recording** oknpatch type  
```
oknpatch -t rerun_recording -d recording_folder_directory_to_be_rerun -okndl okn_detector_location
```
Flag indicators -t, -d and -okndl are mandatory.  
Optional flag indicators are as follows:  
1.  -ow = overwritten the trial csv data or not. Default is not overwritten. If you wanna overwrite the original data, you can add -ow yes in the commandline.  
2.  -pd = using pupil detector or not. Default is pupil detector off. If you wanna switch on the pupil detector while rerunning, you can add -pd on in the commandline.  
3.  -bl = tiny full buffer length to be used with pupil detector. Default is 7. If you wanna change it, -bl (buffer_length_integer) in the commandline.  
4.  -es = extra string to name the updated csv. Default is "updated_".  
5.  -uc = updater config location. Default is built-in. If you wanna change the updater config, you can add -uc directory_of_updater_config in the commandline.  
6.  -di = director input to change all the direction in the rerunning.  
7.  -okndc = okn detector config. Default is built-in. If you wanna change the okn detector config, you can add -okndc directory_of_okn_detector_config in the commandline.  
8.  -opmdc = ehdg pupil/opm detector config. Default is built-in. If you wanna change the ehdg pupil/opm detector config, you can add -opmdc directory_of_ehdg_detector_config in the commandline.  
9.  -pi = plot info. Default is built-in. If you wanna change the plot info, you can add -pi directory_of_plot_info_config in the commandline.  
10.  -ri = rule info. Default is built-in. If you wanna change the rule info, you can add -ri directory_of_rule_info_config in the commandline.

For **show** oknpatch type
This type is to check default/built-in config information and defaults.  
Example usage:
```
oknpatch -t show=uc
```
This will show you updater config information.  
Available show commands are as follows:  
1.  show=uc
2.  show=okndc
3.  show=opmdc
4.  show=pi
5.  show=ri
6.  show=es
7.  show=bl
8.  show=ow
9.  show=pd

### To upgrade version  
In `Anaconda Powershell Prompt`,
```
pip install -U oknpatch
```
or
```
pip install --upgrade oknpatch
```

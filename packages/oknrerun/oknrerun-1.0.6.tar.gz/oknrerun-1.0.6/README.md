# OKNRERUN
Python program to rerun eye health diagnostic group's recording data.   
In the rerunning process, it will copy all data into a new folder(which will never overwrite the original folder) except config and trials data.  
Then, it will rerun trial data which includes the pupil detection(optional), updating trial csv, okn detection, applying okn rules and drawing the trial plot.  
At the end of trial rerunning, it will also produce summary csv and summary plot for all trials.  
## External Program Requirement
### ffmpeg
We need ffmpeg when we are rerunning the recording with pupil detection in order to split the video.  
We do not need ffmpeg if we are rerunning without using pupil detector.  

## Installation requirements and guide
### Anaconda
To install this program, `Anaconda python distributing program` and `Anaconda Powershell Prompt` are needed.  
If you do not have `Anaconda`, please use the following links to download and install:  
Download link: https://www.anaconda.com/products/distribution  
Installation guide link: https://docs.anaconda.com/anaconda/install/  
### PIP install
To install `oknrerun`, you have to use `Anaconda Powershell Prompt`.  
After that, you can use the `oknrerun` from any command prompt.  
In `Anaconda Powershell Prompt`:
```
pip install oknrerun
```

### To check and upgrade version  
In `Anaconda Powershell Prompt`,
To check current version
```
oknrerun --version
```
To upgrade
```
pip install -U oknrerun
```

## Usage
We can rerun a recording folder with or without pupil detector.
### Without pupil detector
```
oknrerun -d (directory to recording folder to be rerun) -okndl (directory to okndetector)
```
### With pupil detector
```
oknrerun -d (directory to recording folder to be rerun) -okndl (directory to okndetector) -pd (type or indicator)
```
#### type or indicator
Type = type of pupil detector such as **opm** and **plm**.  
Note: Currently there is only **opm** type.  
Indicator = **on**, **y**, **1** or **true**.  

### Optional flags/arguments
1.  **-uc** (directory to updater config(gazefilters.json))
2.  **-okndc** (directory to okn detector config(okndetector.gaze.config))
3.  **-pi** (directory to plot info(oknserver_graph_plot_config.json))
4.  **-ri** (directory to rule info(the config file which include rules))
5.  **-bl** (buffer length of tiny fill buffer to be used with pupil detector). Default is 7.  
6.  **-opmdc** (directory to opm detector config(opm_detector_config.json))  
7.  **-es** (extra string to give the name of updated trial csv). Default is **updated_**.
8.  **-di** (direction input to overwrite the direction of existing recording direction of **all trials**)

### To check built-in config information and defaults
```
oknrerun --display (config name or defaults)
```
#### Available names
1.  uc (updater config)
2.  okndc (okn detector config)
3.  opmdc (opm detector config)
4.  pi (plot info)
5.  ri (rule info)
6.  defaults

Example usage
```
oknrerun --display uc
```
This will display the built-in information of updater config (gazefilters.json).  

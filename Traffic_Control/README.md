# Traffic Simulation

## Requirements
<br/>

### Python
Creating and activating a Python 3.8 environment in Anaconda should be sufficient
<br/>

### R
R is required only for displaying the plots. RStudio could be used for this purpose. The following packages need to be installed -
<br/>
1. ggplot2
2. ggpubr
3. reshape2
4. viridis
<br/>
<br/>


## Usage
<br/>

### Steps:
<br/>
1. Go to 'Traffic_Control/' and create an algorithm file in 'Algorithms/' named as '`AlgorithmName`_Algo.py'
<br/>
2. Go to 'Traffic_Control/Traffic_Simulation/' and create a config folder in 'Config/' named as '`ConfigurationName`_Config/'
<br/>
3. Go to the root of the repo and execute the following command
<br/>
./run_GUI.sh --config `ConfigurationName` --algo `AlgorithmName` [Other Options]
<br/>
(Details about 'Other Options' are mentioned below in 'Available Options')
<br/>
6. To test all possible algorithms in all possible configurations, execute the following command
<br/>
./test_algos.sh
<br/>
<br/>

### Available Options:
<br/>
1. Graphical simulation only
<br/>
Nothing
<br/>
2. Graphical simulation with logging of traffic metrics and showing of plots
<br/>
--log
<br/>
3. Logging of traffic metrics without graphical simulation or plots
<br/>
--silent_log
<br/>
4. Show only simulation performance plot
<br/>
--only_perf_plot
<br/>
5. Show only comparison plot (config and algo options are Don't Cares)
<br/>
--only_comp_plot
<br/>
<br/>

### Examples:
<br/>
1. To run only graphical simulation of `Static` algorithm in `Default` configuration
<br/>
./run_GUI.sh --config Default --algo Static
<br/>
2. To only log traffic metrics of `Static` algorithm in `Biased` configuration
<br/>
./run_GUI.sh --config Biased --algo Static --silent_log
<br/>
3. To show only comparison plot
<br/>
./run_GUI.sh --config Default(Don't Care) --algo Static(Don't Care) --only_comp_plot
<br/>
4. For simulating all algorithms in all configurations
<br/>
./test_algos.sh
<br/>
<br/>

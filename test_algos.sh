#!/usr/bin/bash

controlPath=Traffic_Control/
simPath=${controlPath}Traffic_Simulation/
configPath=${simPath}Config/
algoPath=${controlPath}Algorithms/

configs=$(ls $configPath)
algos=$(ls $algoPath)

for config in $configs
do
    for algo in $algos
    do
        config=${config//_Config/ }
        config=${config[0]}
        algo=${algo//_Algo.py/ }
        algo=${algo[0]}
        echo -e "\n\nConfiguration: $config\nAlgorithm: $algo"
        ./run_GUI.sh --config ${config} --algo ${algo} --silent_log
    done
done

./run_GUI.sh --config ${config} --algo ${algo} --only_comp_plot
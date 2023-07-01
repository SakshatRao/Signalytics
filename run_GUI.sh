#!/usr/bin/bash

echo ""

# Different Color Settings
RED='\033[0;31m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
NOCOLOR='\033[0m'

if [[ $# -ge 4 ]];
then
    while [[ $# -gt 0 ]]
    do
        key="$1"

        case $key in
            --config)
                config="$2"
                shift
                shift
                ;;
            --algo)
                algo="$2"
                shift
                shift
                ;;
            --log)
                log=1
                shift
                ;;
            --silent_log)
                log=1
                silent_log=1
                shift
                ;;
            --only_perf_plot)
                only_perf_plot=1
                shift
                ;;
            --only_comp_plot)
                only_comp_plot=1
                shift
                ;;
            *)
                echo "Invalid arguments provided"
                echo -e "\nUse the following format:\n${CYAN}./run_GUI.sh -c <Config> -a <Algo> [--log] [--silent_log] [--only_perf_plot] [--only_comp_plot]${NOCOLOR}"
                exit
                ;;
        esac
    done

    config_folder=${config}_Config/
    algo_file=${algo}_Algo.py

    controlPath=Traffic_Control/
    simPath=${controlPath}Traffic_Simulation/
    configPath=${simPath}Config/
    algoPath=${controlPath}Algorithms/
    selConfigPath=${configPath}${config_folder}

    # Using provided configuration and algorithm
    repl_config=s/Default_/${config}_/
    repl_algo=s/Static_/${algo}_/
    repl_Base=s/Base/run_Base/
    repl_graphConfig=s/graph_config/run_graph_config/

    cat ${controlPath}GraphicalSim.py | sed ${repl_config} | sed ${repl_algo} | sed ${repl_Base} | sed ${repl_graphConfig} 1> ${controlPath}run_GraphicalSim.py
    cat ${simPath}Base.py | sed ${repl_config} | sed ${repl_algo} 1> ${simPath}run_Base.py
    cat ${selConfigPath}graph_config.py | sed ${repl_Base} 1> ${selConfigPath}run_graph_config.py
    cat ${simPath}plot_metrics.R | sed ${repl_config} | sed ${repl_algo} 1> ${simPath}run_plot_metrics.R
    cat ${simPath}plot_comparison.R | sed ${repl_config} | sed ${repl_algo} 1> ${simPath}run_plot_comparison.R
    cat ${simPath}update_logs.R | sed ${repl_config} | sed ${repl_algo} 1> ${simPath}run_update_logs.R

    # Running simulation
    echo -e "*** ${YELLOW}Starting Simulation${NOCOLOR} ***"
    if [[ $log -eq 1 ]];
    then
        python3 ${controlPath}run_GraphicalSim.py --to_log --disable_graphics 2>/dev/null
        Rscript ${simPath}run_update_logs.R 2>/dev/null
        if [[ $silent_log -ne 1 ]]
        then
            Rscript ${simPath}run_plot_metrics.R 2>/dev/null
            Rscript ${simPath}run_plot_comparison.R 2>/dev/null
        fi
    else
        if [[ $only_comp_plot -eq 1 ]]
        then
            Rscript ${simPath}run_plot_comparison.R #2>/dev/null
        else
            if [[ $only_perf_plot -eq 1 ]]
            then
                Rscript ${simPath}run_plot_metrics.R
            else
                python3 ${controlPath}run_GraphicalSim.py
            fi
        fi
    fi
    echo -e "\n*** ${RED}Stopping Simulation${NOCOLOR} ***"

    # Removing generated files
    rm ${controlPath}run_GraphicalSim.py 2>/dev/null
    rm ${simPath}run_Base.py 2>/dev/null
    rm ${selConfigPath}run_graph_config.py 2>/dev/null
    rm ${simPath}run_plot_comparison.R 2>/dev/null
    rm ${simPath}run_plot_metrics.R 2>/dev/null
    rm ${simPath}run_update_logs.R 2>/dev/null
    rm -r ${algoPath}__pycache__/ 2>/dev/null
    rm -r ${selConfigPath}__pycache__/ 2>/dev/null
    rm -r ${simPath}__pycache__/ 2>/dev/null
else
    echo -e "${RED}Improper use of command!${NOCOLOR}"
    echo -e "\nUse the following format:\n${CYAN}./run_GUI.sh --config <Config> --algo <Algo> [--log] [--silent_log] [--only_perf_plot] [--only_comp_plot]${NOCOLOR}"
fi

echo ""
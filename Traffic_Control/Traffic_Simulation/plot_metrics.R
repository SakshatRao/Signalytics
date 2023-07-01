#install.packages("ggplot2")
#install.package("ggpubr")

library(ggplot2)
library(ggpubr)
library(reshape2)
library(RColorBrewer)
library(viridisLite)
basePath <- "Traffic_Control/Traffic_Simulation/Logs/"

simType <- 'Default_Config_Static_Algo'
config <- strsplit(simType, '_Config')[[1]][1]
algo <- strsplit(strsplit(simType, 'Config_')[[1]][2], '_Algo')[[1]][1]

log_df <- read.csv(paste(basePath, simType, '.csv', sep = ''))
log_df[, 'RollAvgWaitingTime'] <- data.table::frollmean(log_df[, 'AvgWaitingTime'], 10)
log_df[, 'RollAvgEmergencyWaitingTime'] <- data.table::frollmean(log_df[, 'AvgEmergencyWaitingTime'], 10)
log_df[, 'RollAvgTrafficWaitingTime'] <- data.table::frollmean(log_df[, 'AvgTrafficWaitingTime'], 10)
log_df[, 'RollAvgTrafficLen'] <- data.table::frollmean(log_df[, 'AvgTrafficLen'], 10)
log_df[, 'RollAvgPedestrianWaitingTime'] <- data.table::frollmean(log_df[, 'AvgPedestrianWaitingTime'], 10)

# Average Waiting Time Lineplot
avgWait <- ggplot(log_df, aes(x = SimulationTime)) + geom_line(aes(y = RollAvgWaitingTime)) + labs(title = "Avg Waiting", y = 'Waiting Time', x = 'Seconds')

# Average Traffic Waiting Time Lineplot
avgTrafficWait <- ggplot(log_df, aes(x = SimulationTime)) + geom_line(aes(y = RollAvgTrafficWaitingTime)) + labs(title = "Avg Traffic-weighted Waiting", y = 'Waiting Time', x = 'Seconds')

# Average Emergency Waiting Time Lineplot
avgEmerWait <- ggplot(log_df, aes(x = SimulationTime)) + geom_line(aes(y = RollAvgEmergencyWaitingTime)) + labs(title = "Avg Emergency Waiting", y = 'Waiting Time', x = 'Seconds')

# Average Lane Traffic Length Lineplot
avgTrafficLen <- ggplot(log_df, aes(x = SimulationTime)) + geom_line(aes(y = RollAvgTrafficLen)) + labs(title = "Avg Lane Traffic Length", y = 'Length', x = 'Seconds')

# Average Pedestrian Waiting Time Lineplot
avgPedestrianWait <- ggplot(log_df, aes(x = SimulationTime)) + geom_line(aes(y = RollAvgPedestrianWaitingTime)) + labs(title = "Avg Pedestrian Waiting Time", y = 'Waiting Time', x = 'Seconds')

# Waiting Times Histogram
waitingTime_df <- read.csv(paste(basePath, 'WaitingTimes_', simType, '.csv', sep = ''))
waitingTime <- ggplot(waitingTime_df, aes(x = WaitingTimes)) + geom_histogram(binwidth = 5, color = 'black') + scale_x_continuous(limits = c(1, max(waitingTime_df$WaitingTimes) + 1)) + labs(title = 'Waiting Histogram', x = 'Waiting Time', y = 'Frequency')

gg <- ggarrange(avgWait, avgTrafficWait, avgEmerWait, waitingTime, avgTrafficLen, avgPedestrianWait, nrow = 2, ncol = 3)
#print(gg)

X11()
plot(gg)
while(names(dev.cur()) != 'null device') Sys.sleep(1)

dev.off()
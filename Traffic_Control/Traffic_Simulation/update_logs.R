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

# Avg Waiting Time Heatmap
if (file.exists(paste(basePath, 'performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'performance.csv', sep = ''), row.names = FALSE)
}
perf_df <- read.csv(paste(basePath, 'performance.csv', sep = ''))
rownames(perf_df) <- perf_df$Algo
perf_df[algo, config] <- tail(log_df$RollAvgWaitingTime, n = 1)
perf_df$Algo <- rownames(perf_df)
rownames(perf_df) <- NULL
write.csv(perf_df, paste(basePath, 'performance.csv', sep = ''), row.names = FALSE)

# Std Waiting Time Heatmap
if (file.exists(paste(basePath, 'std_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'std_performance.csv', sep = ''), row.names = FALSE)
}
std_perf_df <- read.csv(paste(basePath, 'std_performance.csv', sep = ''))
rownames(std_perf_df) <- std_perf_df$Algo
std_perf_df[algo, config] <- tail(log_df$StdWaitingTime, n = 1)
std_perf_df$Algo <- rownames(std_perf_df)
rownames(std_perf_df) <- NULL
write.csv(std_perf_df, paste(basePath, 'std_performance.csv', sep = ''), row.names = FALSE)

# Traffic Waiting Time Heatmap
if (file.exists(paste(basePath, 'traffic_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'traffic_performance.csv', sep = ''), row.names = FALSE)
}
traffic_perf_df <- read.csv(paste(basePath, 'traffic_performance.csv', sep = ''))
rownames(traffic_perf_df) <- traffic_perf_df$Algo
traffic_perf_df[algo, config] <- tail(log_df$RollAvgTrafficWaitingTime, n = 1)
traffic_perf_df$Algo <- rownames(traffic_perf_df)
rownames(traffic_perf_df) <- NULL
write.csv(traffic_perf_df, paste(basePath, 'traffic_performance.csv', sep = ''), row.names = FALSE)

# Emergency Waiting Time Heatmap
if (file.exists(paste(basePath, 'emergency_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'emergency_performance.csv', sep = ''), row.names = FALSE)
}
emer_perf_df <- read.csv(paste(basePath, 'emergency_performance.csv', sep = ''))
rownames(emer_perf_df) <- emer_perf_df$Algo
emer_perf_df[algo, config] <- tail(log_df$RollAvgEmergencyWaitingTime, n = 1)
emer_perf_df$Algo <- rownames(emer_perf_df)
rownames(emer_perf_df) <- NULL
write.csv(emer_perf_df, paste(basePath, 'emergency_performance.csv', sep = ''), row.names = FALSE)

# Lane Traffic Length Heatmap
if (file.exists(paste(basePath, 'trafficLen_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'trafficLen_performance.csv', sep = ''), row.names = FALSE)
}
trafficLen_perf_df <- read.csv(paste(basePath, 'trafficLen_performance.csv', sep = ''))
rownames(trafficLen_perf_df) <- trafficLen_perf_df$Algo
trafficLen_perf_df[algo, config] <- tail(log_df$RollAvgTrafficLen, n = 1)
trafficLen_perf_df$Algo <- rownames(trafficLen_perf_df)
rownames(trafficLen_perf_df) <- NULL
write.csv(trafficLen_perf_df, paste(basePath, 'trafficLen_performance.csv', sep = ''), row.names = FALSE)

# Pedestrian Waiting Time Heatmap
if (file.exists(paste(basePath, 'pedestrian_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'pedestrian_performance.csv', sep = ''), row.names = FALSE)
}
pedestrian_perf_df <- read.csv(paste(basePath, 'pedestrian_performance.csv', sep = ''))
rownames(pedestrian_perf_df) <- pedestrian_perf_df$Algo
pedestrian_perf_df[algo, config] <- tail(log_df$RollAvgPedestrianWaitingTime, n = 1)
pedestrian_perf_df$Algo <- rownames(pedestrian_perf_df)
rownames(pedestrian_perf_df) <- NULL
write.csv(pedestrian_perf_df, paste(basePath, 'pedestrian_performance.csv', sep = ''), row.names = FALSE)
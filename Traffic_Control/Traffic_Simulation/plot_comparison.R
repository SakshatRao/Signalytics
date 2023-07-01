#install.packages("ggplot2")
#install.package("ggpubr")

library(ggplot2)
library(ggpubr)
library(reshape2)
library(RColorBrewer)
library(viridisLite)
basePath <- "Traffic_Control/Traffic_Simulation/Logs/"

# Avg Waiting Time Heatmap
if (file.exists(paste(basePath, 'performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'performance.csv', sep = ''), row.names = FALSE)
}
perf_df <- read.csv(paste(basePath, 'performance.csv', sep = ''))
rownames(perf_df) <- perf_df$Algo
perf_df$Algo <- rownames(perf_df)
melted_perf_df <- reshape2::melt(perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
heatmap <- ggplot(melted_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Avg Waiting Time", y = "Algorithms", x = "Config") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

# Std Waiting Time Heatmap
if (file.exists(paste(basePath, 'std_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'std_performance.csv', sep = ''), row.names = FALSE)
}
std_perf_df <- read.csv(paste(basePath, 'std_performance.csv', sep = ''))
rownames(std_perf_df) <- std_perf_df$Algo
std_perf_df$Algo <- rownames(std_perf_df)
melted_std_perf_df <- reshape2::melt(std_perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
std_heatmap <- ggplot(melted_std_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Standard Deviation in Waiting Time", y = "Algorithms", x = "Config") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

# Traffic Waiting Time Heatmap
if (file.exists(paste(basePath, 'traffic_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'traffic_performance.csv', sep = ''), row.names = FALSE)
}
traffic_perf_df <- read.csv(paste(basePath, 'traffic_performance.csv', sep = ''))
rownames(traffic_perf_df) <- traffic_perf_df$Algo
traffic_perf_df$Algo <- rownames(traffic_perf_df)
melted_traffic_perf_df <- reshape2::melt(traffic_perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
traffic_heatmap <- ggplot(melted_traffic_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Avg Traffic-weighted Waiting Time", y = "Algorithms", x = "Config") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

# Emergency Waiting Time Heatmap
if (file.exists(paste(basePath, 'emergency_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'emergency_performance.csv', sep = ''), row.names = FALSE)
}
emer_perf_df <- read.csv(paste(basePath, 'emergency_performance.csv', sep = ''))
rownames(emer_perf_df) <- emer_perf_df$Algo
emer_perf_df$Algo <- rownames(emer_perf_df)
melted_emer_perf_df <- reshape2::melt(emer_perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
emer_heatmap <- ggplot(melted_emer_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Emergency Waiting Time", y = "Algorithms", x = "Config") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

# Lane Traffic Length Heatmap
if (file.exists(paste(basePath, 'trafficLen_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'trafficLen_performance.csv', sep = ''), row.names = FALSE)
}
trafficLen_perf_df <- read.csv(paste(basePath, 'trafficLen_performance.csv', sep = ''))
rownames(trafficLen_perf_df) <- trafficLen_perf_df$Algo
trafficLen_perf_df$Algo <- rownames(trafficLen_perf_df)
melted_trafficLen_perf_df <- reshape2::melt(trafficLen_perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
trafficLen_heatmap <- ggplot(melted_trafficLen_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Lane Traffic Length", y = "Algorithms", x = "Config") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

# Pedestrian Waiting Time Heatmap
if (file.exists(paste(basePath, 'pedestrian_performance.csv', sep = '')) == FALSE)
{
  init_df <- data.frame(Algo = character(), Default = character())
  write.csv(init_df, paste(basePath, 'pedestrian_performance.csv', sep = ''), row.names = FALSE)
}
pedestrian_perf_df <- read.csv(paste(basePath, 'pedestrian_performance.csv', sep = ''))
rownames(pedestrian_perf_df) <- pedestrian_perf_df$Algo
pedestrian_perf_df$Algo <- rownames(pedestrian_perf_df)
melted_pedestrian_perf_df <- reshape2::melt(pedestrian_perf_df, id.vars = c('Algo'), variable.name = 'Config', value.name = 'Scale')
pedestrian_heatmap <- ggplot(melted_pedestrian_perf_df, aes(x = Config, y = Algo)) + geom_tile(aes(fill = Scale)) + labs(title = "Pedestrian Waiting Time") + theme(plot.title = element_text(size = 20), axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_text(size = 15), axis.text.y = element_text(size = 15)) + geom_text(aes(label = round(Scale, 1)), size = 6) + scale_fill_gradient(low = 'blue', high = 'red')

gg <- ggarrange(heatmap, traffic_heatmap, emer_heatmap, std_heatmap, trafficLen_heatmap, pedestrian_heatmap, nrow = 2, ncol = 3)
#print(gg)

X11()
plot(gg)
while(names(dev.cur()) != 'null device') Sys.sleep(1)

dev.off()
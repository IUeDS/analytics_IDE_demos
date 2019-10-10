# Clean-up
rm(list=ls())

# Remember to set working directory to "Source Files Location"

# In R, it's conventional to use "<-" to assign variables to values
x <- 123
# ...but "=" is a homonym
x = 321
# ...but R-truists prefer "<-" to distinguish assignment from equality
# Delete a variable
rm(x)

# Lists are constructed using the "c()" operator (short for concatenate)
x <- c(1,2,3)
# Operations can be applied to all elements in a list
y <- x + 1

# But most of the time you'll be working with dataframes
# Dataframes are X observations of Y variables

# Dataframes can be imported directly from CSV files
data <- read.csv('factor_scores.csv', stringsAsFactors = FALSE)
# Dataframes can be summarized
summary(data)
head(data)
# Dataframe variables are referred to using the $ selector
max(data$Motivations)
meanMotivation <- mean(data$Motivations)
# Observations are selected using brackets [ , ] 
data[data$double_hashedid=="QYd/Tw04aPsBQuaQV8nK3w==",]
# Sometimes there're NAs
# That you want to disappear
data <- na.omit(data)

# There are lots of ways to manipulate data in R
# For example, a for loop
for (i in 1:nrow(data)) {
  if (data$Motivations[i] <= 0) {
    data$Motivations.Cat <- 'Lo'
  }
} 
# Logical indexing is preferred
data$Motivations.Cat[data$Motivations > 0] <- 'Hi'

# But the most preferred grammar for data manipulation
# in R is the "tidyverse" -- a collection of packages
# that share a common philosophy and structure for 
# data manipulation in R.
library(dplyr) # A grammar for data manipulation 
# dplyr lets you use the pipe operator %>% to create
# a processing pipeline without mucking up your workspace
data <- data %>% mutate(Visit.Frequency.Cat = ifelse(Visit.Frequency <= 0, "Lo","Hi"))
# and allows PivotTable-like summarizing
data %>% group_by(Motivations.Cat,Visit.Frequency.Cat) %>% summarize(student_cnt = n())

# Graphing in R is fun!
plot(data$Motivations,data$Concentration.of.Effort)
# ...but a more powerful tool for graphing in R is with ggplot2
# (which is also part of the tidyverse)
library(ggplot2)
p1 <- ggplot(data, aes(x=data$Motivations,y=data$Concentration.of.Effort)) +
   geom_point() +
   geom_smooth(method = "lm") +
   xlab('Motivations') + ylab("Concentration of Effort")
p1
# Try making a boxplot with our categorical variable
data$Motivations.Cat <- factor(data$Motivations.Cat, levels = c("Lo","Hi"))
p2 <- ggplot(data, aes(x=data$Motivations.Cat,y=data$Concentration.of.Effort)) +
   geom_boxplot() +
   xlab('Motivations Category') + ylab("Concentration of Effort")
p2

# Statistics
t.test(data$Concentration.of.Effort ~ data$Motivations.Cat)
mod <- glm(Concentration.of.Effort ~ data$Motivations, data=data)
summary(mod)

# Saving data
save(file="demoData.RData",data)


library(gbm)
library(glmnet)
library(rpart)
require(randomForest)
rm(list = ls())
data <- read.csv("Tree Species Data.csv", header = T)
# Response
oak <- data['Whiteoak']/data['Total']
oak <- oak ** (1/3)
pine <- data['Whitepine']/data['Total']
ash <- data['Ash']/data['Total']

oak <- as.numeric(oak > 0.1)

# Predictors
lidar <- data[,15:20]
hyperspectral <- data[21:length(data)]

# Data sets
oak.hyperspectral <- cbind(oak,hyperspectral)
paste(colnames(hyperspectral), collapse = '+')

lm20 <- lapply(colnames(hyperspectral), function(x) lm(paste("oak", x, sep = ' ~ '), data = oak.hyperspectral))
lapply(lm20,summary)
lapply(1:20,function(x) plot(hyperspectral[,x], oak))

qqnorm(as.matrix(oak))
qqline(as.matrix(oak))


##################### Random forest
rf=randomForest(hyperspectral,as.factor(oak))





################## Tree
tree <- rpart(oak ~.,data=oak.hyperspectral,method='class')
cbind(p<-predict(tree,newdata = oak.hyperspectral)[,2] > 0.5,oak)
sum(abs(p-oak))


################## Forward Selection
full <- glm(oak ~.,family=binomial,data=oak.hyperspectral)
null <- glm(oak ~1,family=binomial,data=oak.hyperspectral)

forward <- step(null,scope = list(upper=formula(full),lower=formula(null)),direction='forward')
cbind(p <- predict(full, newdata = hyperspectral, type = 'response') > 0.5,oak)

sum(abs(p-oak))


################################ Gradient Boosting
fit2 <- gbm(oak ~., data=oak.hyperspectral, distribution = "gaussian", n.trees = 100, interaction.depth = 3, cv.folds = 3, bag.fraction = 0.701)
best.iter <- gbm.perf(fit2,method="OOB")
f.predict <- predict(fit2,hyperspectral,best.iter)
cbind(f.predict,oak)


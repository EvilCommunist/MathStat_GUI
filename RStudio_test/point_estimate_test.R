file_path <- "../r_test_data/test_data_point_estimate.txt"
data <- scan(file_path)
print(data)


# Оценка значения
estimate_a <- mean(data)
round(estimate_a)


# Дисперсия выборочного среднего
sigma_squared <- (sum((data-estimate_a)^2)/length(data))
n <- length(data)
variance_sample_mean <- sigma_squared / n
print(variance_sample_mean)


# Оценка дисперсии
mean_val <- mean(data)
variance_estimate <- sum((data - mean_val)^2) / (length(data))
print(variance_estimate_rounded)


# Функция правдоподобия для распределения Пуассона
data <- c(1, 0, 0, 2, 2) # for Pois must be integer!!!
lambda <- mean(data) # lambda can be set
log_likelihood_pois <- sum(dpois(data, lambda = lambda, log = TRUE))
round(log_likelihood_pois, 3)
# Функция правдоподобия для распределения Биномиального
data <- c(1, 0, 0, 2, 2) # something
size <- max(data)
print(size)
prob <- mean(data)/size
print(mean(data))
print(prob)
log_likelihood_bin <- sum(dbinom(data, size, prob, log = TRUE))
round(log_likelihood_bin, 3)


observations <- c(1, 2, 2)
# Метод моментов
g_x <- mean(observations)
theta_moments <- 1 - (g_x - 1) / (2 - 1)
# Метод максимального правдоподобия
count_1 <- sum(observations == 1)  
count_2 <- sum(observations == 2)  
theta_mle <- count_1 / length(observations)
result <- sprintf("%.2f, %.2f", theta_moments, theta_mle)
cat(result)



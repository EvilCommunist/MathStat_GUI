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


# Рассчёт границ доверительного интервала norm
average_weight <- 249  # средний вес
std_dev <- 10          # стандартное отклонение
n <- 100               # размер выборки
confidence_level <- 0.9

standard_error <- std_dev / sqrt(n)
alpha <- 1 - confidence_level
z_critical <- qnorm(1 - alpha / 2)

lower_bound <- average_weight - z_critical * standard_error
upper_bound <- average_weight + z_critical * standard_error
cat(round(lower_bound, 3), round(upper_bound, 3))


# Построение доверительного интервала t
x_bar <- 10.3  # Средний диаметр
s2 <- 1.21     # Несмещенная оценка дисперсии
n <- 16        # Объем выборки
alpha <- 0.05  # Уровень значимости
s <- sqrt(s2)
print(s)
t_crit <- qt(1 - alpha / 2, df = n - 1)
print(t_crit)

margin_of_error <- t_crit * (s / sqrt(n))
confidence_interval <- c(x_bar - margin_of_error, x_bar + margin_of_error)
print(confidence_interval)


# Построение доверительного интервала chisq 
file_path <- "../r_test_data/conf_int/test_data_qchisq.txt"
data <- scan(file_path)
n <- length(data)
s2 <- sum(data^2)/(n-1)
alpha <- 0.05

chi2_lower <- qchisq(1 - alpha / 2, df = n)
chi2_upper <- qchisq(alpha / 2, df = n)
lower_bound <- (n-1) * s2 / chi2_lower
upper_bound <- (n-1) * s2 / chi2_upper
cat(format(round(lower_bound, 3), nsmall = 3), ",", format(round(upper_bound, 3), nsmall = 3))


# Определение утверждения о проценте неудачи
file_path <- "../r_test_data/conf_int/test_data_error_estimation.txt"
data <- scan(file_path)
alpha <- 0.05
n <- length(data) # размер выборки
p_hat <- mean(data)    # доля брака

z <- qnorm(1 - alpha / 2)
se <- sqrt(p_hat * (1 - p_hat) / n) # стандартная ошибка
lower_bound <- p_hat - z * se # нижняя граница
upper_bound <- p_hat + z * se # верхняя граница
lower_bound <- round(lower_bound, 4)
upper_bound <- round(upper_bound, 4)
R <- ifelse(lower_bound > 0.05, "G", "L")
cat(lower_bound, upper_bound, R, sep = ", ")

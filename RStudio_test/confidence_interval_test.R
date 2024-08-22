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
t_crit <- qt(1 - alpha / 2, df = n - 1)

margin_of_error <- t_crit * (s / sqrt(n))
confidence_interval <- c(x_bar - margin_of_error, x_bar + margin_of_error)
print(confidence_interval)

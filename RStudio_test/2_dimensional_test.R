data <- read.table("../r_test_data/test_data_for_2dimension.txt", header = TRUE)

data_x <- data$data_x # Рост м
data_y <- data$data_y # Вес м

ch_mid_x <- mean(data_x)
ch_mid_y <- mean(data_y)

s_x <- sum((data_x-ch_mid_x)^2) #частичная дисперсия для формулы
s_y <- sum((data_y-ch_mid_y)^2) #частичная дисперсия для формулы

# Коэффициент корреляции:
r_x <- sum((data_x-ch_mid_x)*(data_y-ch_mid_y))/sqrt(s_x*s_y) # "Ручной" рассчёт
print(r_x)

correlation_coefficient <- cor(data_x, data_y) # Встроенная функция
print(correlation_coefficient)

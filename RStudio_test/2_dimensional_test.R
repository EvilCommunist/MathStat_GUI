data <- read.table("../r_test_data/test_data_for_2dimension.txt", header = TRUE)

data_x <- data$data_x # Рост м
data_y <- data$data_y # Вес м

sorted_data_x <- sort(data_x)
sorted_data_y <- sort(data_y)
cat("Первая выборка:", sorted_data_x,
    "\nВторая выборка:", sorted_data_y)

ch_mid_x <- mean(sorted_data_x)
ch_mid_y <- mean(sorted_data_y)
cat("Первичное выборочное среднее:", ch_mid_x,
    "\nВторичное выборочное среднее:", ch_mid_y)

cat("Медиана первой выборки:", median(sorted_data_x),
    "\nМедиана второй выборки:", median(sorted_data_y))

# Первый квартиль
print(sorted_data_x[length(sorted_data_x)*0.25+1])
print(sorted_data_y[length(sorted_data_y)*0.25+1])

# Третий квартиль
print(sorted_data_x[length(sorted_data_x)*0.75+1])
print(sorted_data_y[length(sorted_data_y)*0.75+1])

# Дисперсии
s_x <- sum((data_x-ch_mid_x)^2)/length(data_x) 
s_y <- sum((data_y-ch_mid_y)^2)/length(data_y) 

# Коэффициент корреляции:
r_x <- sum((data_x-ch_mid_x)*(data_y-ch_mid_y))/(length(data_x)*sqrt(s_x*s_y)) # "Ручной" рассчёт
print(r_x)

correlation_coefficient <- cor(data_x, data_y) # Встроенная функция
print(correlation_coefficient)

file_path <- "../r_test_data/test_data_for_1dimension.txt"
data <- scan(file_path)
print(data)


sorted_data <- sort(data) # Нахождение порядковой статистики 
print(sorted_data)

# Выборочное среднее:
ch_mid <- mean(data)
print(ch_mid)

# Выборочная дисперсия
print(sum((sorted_data-ch_mid)^2)/length(sorted_data))

# Выборочная медиана
print(median(sorted_data))

# Первый квартиль
print(sorted_data[length(sorted_data)*0.25+1])

# Второй квартиль
print(sorted_data[length(sorted_data)*0.5+1])

# Третий квартиль
print(sorted_data[length(sorted_data)*0.75+1])

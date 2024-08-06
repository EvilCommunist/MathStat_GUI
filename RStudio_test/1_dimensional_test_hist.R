file_path <- "../r_test_data/test_data_for_1dimension.txt"
data <- scan(file_path)
print(data)

file_path_int <- "../test_data_intervals_1dim.txt"
intervals <- scan(file_path_int)
print(intervals)


lower_limit <- 0  
upper_limit <- max(hist(data, breaks = intervals, plot = FALSE)$counts) + 1  # Максимум частоты + 1

# Создание гистограммы без осей
hist(data, 
     breaks = intervals,
     ylim = c(lower_limit, upper_limit),
     main = "Гистограмма распределения", 
     xlab = "Значения", 
     ylab = "Частота", 
     col = "lightblue", 
     border = "black", 
     axes = FALSE)

# Добавление осей
axis(1)  # Ось X
axis(2, at = seq(lower_limit, upper_limit, by = 1))  # Ось Y с делением 1

box() # Добавление рамки

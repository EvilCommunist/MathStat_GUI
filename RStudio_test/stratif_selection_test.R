# работа со смесями
data <- read.table("../r_test_data/stratas/test_data_stratif_mix.txt", header = TRUE)
w_vector <- data$data_w
a_vector <- data$data_a
sigma_sq_vec <- data$data_sigma_sq
cat( w_vector, "\n", a_vector, "\n", sigma_sq_vec)

E_X <- sum(w_vector*a_vector)
Var_X <- w1 * (sigma1_sq + (a1 - E_X)^2) +
  w2 * (sigma2_sq + (a2 - E_X)^2) +
  w3 * (sigma3_sq + (a3 - E_X)^2)
cat(sprintf("%.1f, %.1f", E_X, Var_X))


# работа со стратами
data <- read.table("../r_test_data/stratas/test_data_stratif_selection.txt", header = TRUE)

strata1 <- data$data_x # Рост м
strata2 <- data$data_y # Вес м

n1 <- length(strata1)
n2 <- length(strata2)

mean1 <- mean(strata1)
mean2 <- mean(strata2)
overall_mean <- (0.4 * mean1) + (0.6 * mean2)

var1 <- sum((strata1-mean1)^2)/length(strata1)
var2 <- sum((strata2-mean2)^2)/length(strata2)
overall_variance <- 0.4*var1 + 0.6*var2 + 0.4*(mean1 - overall_mean)^2 + 0.6*(mean2 - overall_mean)^2

result <- sprintf("%.1f, %.1f", overall_mean, overall_variance)
cat(result)


# Нахождение объёма выборки
data <- read.table("../r_test_data/stratas/test_data_volume_strata.txt", header = TRUE)
n_vec <- data$data_n
d_vec <- data$data_d
N <- data$N[1]
cat(n_vec,"\n", d_vec,"\n", N)

n1 <- N[1]*(n_vec[1]*sqrt(d_vec[1])/(n_vec[1]*sqrt(d_vec[1])+(n_vec[2]*sqrt(d_vec[2]))))
n2 <- N - n1
sprintf("%.0f, %.0f", n1, n2)
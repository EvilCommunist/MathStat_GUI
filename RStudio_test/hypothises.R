n <- 40
sample_mean <- 14.4
sample_sd <- 2.915
mu_0 <- 13.2   
alpha <- 0.01 

Z <- (sample_mean - mu_0) /(sqrt((n/(n-1)))*sample_sd / sqrt(n))
Z_value <- round(Z, 2)
# H0: a_0 <= 13.2
# H1: a_0 > 13.2
critical_value <- qnorm(1 - alpha)   
if (Z_value > critical_value) {
  hypothesis <- "H1"
} else {
  hypothesis <- "H0"
}
cat(Z_value, hypothesis)


# Проверка размера выборки
alpha <- 0.05     
beta <- 0.1      
sigma <- 2
mu_0 <- 5   # H0: a = 5
mu_1 <- 5.5  # H1: a = 5.5
Z_alpha <- qnorm(1 - alpha)
Z_beta <- qnorm(1 - beta)
n <- ((Z_alpha + Z_beta) * sigma / (mu_1 - mu_0))^2
n_min <- ceiling(n)
cat("Объем выборки:", n_min, "\n")

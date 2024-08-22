# работа со смесями
w1 <- 0.3
a1 <- 3
sigma1_sq <- 1

w2 <- 0.6
a2 <- 2
sigma2_sq <- 4

w3 <- 0.1
a3 <- 5
sigma3_sq <- 0.01

E_X <- w1 * a1 + w2 * a2 + w3 * a3
Var_X <- w1 * (sigma1_sq + (a1 - E_X)^2) +
  w2 * (sigma2_sq + (a2 - E_X)^2) +
  w3 * (sigma3_sq + (a3 - E_X)^2)
cat(sprintf("%.1f, %.1f", E_X, Var_X))


# работа со стратами
strata1 <- c(282, 226, 188, 327, 344, 304, 414, 224, 335, 270)
strata2 <- c(417, 851, 742, 1217, 1160, 993, 864, 852, 1286, 988)

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
N1 <- 0.25
N2 <- 0.75
D1 <- 4
D2 <- 6.25
N <- 100

n1 <- N * (N1 * sqrt(D1) / (N1 * sqrt(D1) + N2 * sqrt(D2)))
n2 <- N - n1
sprintf("%.0f, %.0f", n1, n2)
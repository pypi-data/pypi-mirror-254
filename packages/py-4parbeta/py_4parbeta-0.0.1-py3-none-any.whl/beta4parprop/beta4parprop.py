from scipy.stats import beta
import math


def d4parbeta(x, theta1, theta2, alpha1, alpha2):
    if (theta1 < x < theta2):
        pdf = ((x - theta1) ** (alpha1 - 1)) * ((theta2 - x) ** (alpha2 - 1)) / (
                    (theta2 - theta1) ** (alpha1 + alpha2 - 1)) * (
                          math.gamma(alpha1) * math.gamma(alpha2) / math.gamma(alpha1 + alpha2))
    else:
        pdf = 0
    return pdf


def p4parbeta(x, theta1, theta2, alpha1, alpha2):
    if (x <= theta1):
        cdf = 0
    elif (theta1 < x < theta2):
        cdf = beta.cdf(x, a=alpha1, b=alpha2, loc=theta1, scale=(theta2 - theta1))
    else:
        cdf = 1
    return cdf


def q4parbeta(p, theta1, theta2, alpha1, alpha2):
    if p < 0 or p > 1:
        ppf = math.nan
    else:
        ppf = beta.ppf(p, a=alpha1, b=alpha2, loc=theta1, scale=(theta2 - theta1))
    return ppf


def r4parbeta(n, theta1, theta2, alpha1, alpha2):
    return beta.rvs(a=alpha1, b=alpha2, loc=theta1, scale=(theta2 - theta1), size=n)

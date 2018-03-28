from question1a import loss, loss_derivative, gradient_descent
import pandas as pd
import math
import sklearn


def regularized_model():
    lam = .01


def regularize_loss(c_vector, t, a, r, lam):
    standard_loss = loss(c_vector, t, a, r)
    reg_term = 0
    for i in range(1, len(c_vector)):
        reg_term += c_vector[i]**2
    return standard_loss + (lam/2)*reg_term


weights = [1, 1, 1, 1, 1, 1]
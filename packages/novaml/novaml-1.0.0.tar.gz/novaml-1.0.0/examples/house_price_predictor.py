import numpy as np

from novaml.utils import z_score_normalization
from novaml.models import LinearRegression

data = np.loadtxt("data/houses.txt", delimiter=',')

x_train, y_train = data[:, :4], data[:, 4]
x_train = z_score_normalization(x_train)
initial_w, initial_b = np.zeros(x_train.shape[1]), np.array([0.0])

linear_regression = LinearRegression()

final_w, final_b, _, _ = linear_regression.train(
    x=x_train,
    y=y_train,
    w_init=initial_w,
    b_init=initial_b,
    alpha=1.0e-1,
    iterations=1000,
    lambd=0,
)

yhat = linear_regression.predict(x=x_train, w=final_w, b=final_b)

print(f"yhat: {yhat}")
print(f"ytrain: {y_train}")

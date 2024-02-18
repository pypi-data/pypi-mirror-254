import numpy as np
import pytest
from novaml.models import LinearRegression


@pytest.fixture
def linear_regression():
    return LinearRegression()


def test_cost(linear_regression):
    x = np.array([1.0, 2.0])
    y = np.array([300.0, 500.0])
    w = np.array([0, 0])
    b = 0
    lambd = None

    cost = linear_regression._cost(x, y, w, b, lambd)

    assert np.isclose(cost, 85000, rtol=1e-05, atol=1e-08)


def test_gradient_descent(linear_regression):
    x = np.array([1.0, 2.0])
    y = np.array([300.0, 500.0])
    w = np.array([0, 0])
    b = 0
    lambd = None

    dw, db = linear_regression._gradient_descent(x, y, w, b, lambd)

    assert np.isclose(dw, -650, rtol=1e-05, atol=1e-08)
    assert np.isclose(db, -400, rtol=1e-05, atol=1e-08)


def test_train(linear_regression):
    x = np.array([1.0, 2.0])
    y = np.array([300.0, 500.0])
    w_init = 0
    b_init = 0
    alpha = 1.0e-2
    iterations = 10000
    lambd = None

    w, b, cost_history, parameters_history = linear_regression.train(
        x, y, w_init, b_init, alpha, iterations, lambd
    )

    assert np.isclose(w, 200, rtol=1e-03, atol=1e-05)
    assert np.isclose(b, 100, rtol=1e-03, atol=1e-05)


def test_predict(linear_regression):
    x = 1
    w = 200
    b = 100

    prediction = linear_regression.predict(x, w, b)

    assert np.isclose(prediction, 300, rtol=1e-03, atol=1e-05)

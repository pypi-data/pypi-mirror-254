# NovaML
Build machine learning applications with NovaML; The NEW machine learning library!

## Note
This library is for learning purposes and not ready for production use!

## Install
```shell
pip install novaml
```

## Usage
```python
import numpy as np
from novaml.models import LinearRegression

x = np.array([1.0, 2.0])
y = np.array([300.0, 500.0])
w_init = np.array([0.0])
b_init = np.array([0.0])
alpha = 1.0e-2
iterations = 10000
lambd = None

linear_regression = LinearRegression()

final_w, final_b, _, _ = linear_regression.train(
    x, y, w_init, b_init, alpha, iterations, lambd
)

yhat = linear_regression.predict(x, final_w, final_b)

print(f"ytrain: {y}")
print(f"yhat: {yhat}")
```

## Examples
Check the [README.md](examples%2FREADME.md) of examples folder.

## License
[MIT License](LICENSE)

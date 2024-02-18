def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))


def cost_function(X, y, theta):
    m = len(y)
    predictions = []

    for row in X:
        prediction = dot_product(row, theta)
        predictions.append(prediction)

    squared_errors = []

    for pred, actual in zip(predictions, y):
        error = pred - actual
        squared_errors.append(error**2)

    sum_squared_errors = sum(squared_errors)
    cost = 1 / (2 * m) * sum_squared_errors

    return cost


def batch_gradient_descent(X, y, alpha=0.01, epochs=1000):
    m, n = len(y), len(X[0])
    theta = [0] * n

    for _ in range(epochs):
        predictions = []
        for row in X:
            prediction = dot_product(row, theta)
            predictions.append(prediction)

        errors = [pred - actual for pred, actual in zip(predictions, y)]

        gradient = []
        for i in range(n):
            gradient_i = 1 / m * sum(error * row[i] for error, row in zip(errors, X))
            gradient.append(gradient_i)

        theta = [theta[i] - alpha * gradient[i] for i in range(n)]

    return theta


def stochastic_gradient_descent(X, y, alpha=0.01, epochs=1000):
    m, n = len(y), len(X[0])
    theta = [0] * n

    for _ in range(epochs):
        for i in range(m):
            xi = X[i]
            yi = y[i]
            prediction = dot_product(xi, theta)
            error = prediction - yi

            gradient = []
            for j in range(n):
                gradient_j = xi[j] * error
                gradient.append(gradient_j)

            theta = [theta[j] - alpha * gradient[j] for j in range(n)]

    return theta


def mini_batch_gradient_descent(X, y, batch_size=32, alpha=0.01, epochs=1000):
    m, n = len(y), len(X[0])
    theta = [0] * n

    for _ in range(epochs):
        for i in range(0, m, batch_size):
            xi = X[i : i + batch_size]
            yi = y[i : i + batch_size]

            predictions = []
            for row in xi:
                prediction = dot_product(row, theta)
                predictions.append(prediction)

            errors = [pred - actual for pred, actual in zip(predictions, yi)]

            gradient = []
            for j in range(n):
                gradient_j = (
                    1
                    / batch_size
                    * sum(error * row[j] for error, row in zip(errors, xi))
                )
                gradient.append(gradient_j)

            theta = [theta[j] - alpha * gradient[j] for j in range(n)]

    return theta


def simple_gradient_descent(
    df,
    x_0,
    learnin_rate=0.01,
    precision=0.000001,
    delta_x=1,
    max_iters=10000,
):
    # 'df' is the differential or gradient of a function.
    # For example:
    # Mathematical Expression: f = (x+5)^2 -> df = 2(x+5)
    # Python Expression: f = (x+5)**2 -> df = lambda x: 2*(x+5)

    # df = lambda x: 2 * (x + 5)
    i = 0

    while precision < delta_x and i < max_iters:
        x = x_0
        x_0 = x_0 - learnin_rate * df(x)
        i += 1
        delta_x = abs(x_0 - x)
        print(f"Iteration {i} : X value is {x_0}")

    # return x_0


def gradient_descent(x, y, w=0, b=0, iters=1000, learning_rate=0.01):
    m = len(x)

    for i in range(iters):
        y_predicted = w * x + b
        J = 1 / (2 * m) * sum(dot_product(y_predicted - y, y_predicted - y))
        DJ = 1 / m * sum(dot_product(y_predicted, x))
        w = w - learning_rate * DJ
        b = b - learning_rate * sum(y_predicted - y)

    return w, b, J

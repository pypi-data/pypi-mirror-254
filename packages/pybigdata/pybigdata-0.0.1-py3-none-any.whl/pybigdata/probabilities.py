import math


def print_r(X, round_values=2):
    if isinstance(X, (list, tuple)) and all(isinstance(r, (int, float)) for r in X):
        print([round(r, round_values) for r in X])
    elif isinstance(X, (list, tuple)) and all(
        isinstance(r, (list, tuple)) and len(r) == 1 for r in X
    ):
        for r in X:
            print([round(c, round_values) for c in r])
    elif isinstance(X, (list, tuple)):
        for r in X:
            print([round(c, round_values) for c in r])


def validation(x=[]):
    if len(x) == 0:
        raise ValueError("Random variable is empty!")
    if not (isinstance(x, list) or isinstance(x, tuple)):
        raise ValueError("Random variable should be a list or tuple!")


def mean(x=[]):
    validation(x)
    return sum(x) / len(x)


def mode(x=[]):
    validation(x)
    counter = {}
    for i in x:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    m = list(counter.keys())[0]
    for k in counter:
        if counter[k] > m:
            m = k
    return m


def var(x=[]):
    validation(x)
    n = len(x)
    sigma = 0
    for i in x:
        sigma += (i - mean(x)) ** 2
    return sigma / n


def cov(x=[], y=[]):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("Random variables should not be empty!")
    if len(x) == len(y):
        n = len(x)  # len(x) is equal to len(y)
        mx = mean(x)
        my = mean(y)
        sigma = 0
        for i, j in zip(x, y):
            sigma += (i - mx) * (j - my)
        return sigma / n
    else:
        raise ValueError("Both random variables must have same length!")


def max(x=[]):
    validation(x)
    m = x[0]
    if len(x) > 0:
        for i in x[1:]:
            if i > m:
                m = i
    return m


def min(x=[]):
    validation(x)
    m = x[0]
    if len(x) > 0:
        for i in x[1:]:
            if i < m:
                m = i
    return m


def variation_range(x=[]):
    validation(x)
    return max(x) - min(x)


def std(x=[]):
    validation(x)
    return math.sqrt(var(x))


def nth_percentile(x=[], p=50):
    validation(x)
    x = sorted(x)
    n = len(x)
    index = p * (n - 1) / 100
    if index.is_integer():
        return x[int(index)]
    else:
        i = int(index // 1)
        j = i + 1
        a = x[i]
        b = x[j]
        return a + (index - i) * (b - a)


def median(x=[]):
    return nth_percentile(x, 50)


def all_25th_percentiles(x=[]):
    return {
        0: nth_percentile(x, 0),
        25: nth_percentile(x, 25),
        50: nth_percentile(x, 50),
        75: nth_percentile(x, 75),
        100: nth_percentile(x, 100),
    }


def cov_matrix(*X):
    for x in X:
        if len(x) == 0:
            raise ValueError("Random variables should not be empty!")
        if len(x) != len(X[0]):
            raise ValueError("All random variables must have same length!")

    n = len(X)
    sigma = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(X)):
        for j in range(len(X)):
            sigma[i][j] = cov(X[i], X[j])

    return sigma


def correlation_matrix(*X):
    S = cov_matrix(*X)
    n = len(S)
    sigma = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(X)):
        for j in range(len(X)):
            sigma[i][j] = S[i][j] / (S[i][i] ** (1 / 2) * S[j][j] ** (1 / 2))

    return sigma


def expected_value(observations=[]):
    if len(observations) == 0:
        raise ValueError("The observations list is empty!")

    repeats = {}

    for event in observations:
        if event in repeats:
            repeats[event] += 1
            continue
        repeats[event] = 1

    sigma = 0

    for event in observations:
        sigma += event * (1 / repeats[event])

    return sigma


def probability(observations, x):
    if len(observations) == 0:
        raise ValueError("The observations list is empty!")

    n = len(observations)

    prob = 0

    for event in observations:
        if x == event:
            prob += 1

    return prob / n


def complement_events(sample_space, events):
    if not sample_space or not events:
        raise ValueError("Sample space and event should not be empty!")

    complement_event = list(set(sample_space) - set(events))

    return complement_event


def complement_probability(sample_space, event):
    if not sample_space:
        raise ValueError("Sample space should not be empty!")

    complement_probablity = 1 - probability(sample_space, event)

    return complement_probablity


def find_union(A, B):
    return list(set(list(set(A)) + list(set(B))))


def find_intersection(A, B):
    return list(set(find_union(A, B)) - (set(A) - set(B)) - (set(B) - set(A)))


def probability_X(event_X, probabilities):
    if not event_X or not probabilities:
        raise ValueError("Event and probabilities should not be empty.")
    if len(event_X) != len(probabilities):
        raise ValueError("Event and probabilities should have the same length.")

    event_probability = sum(probabilities[i] for i, event in enumerate(event_X))

    return event_probability


def prob_A_given_B(prob_B_given_A, prob_A, prob_B):
    if prob_B == 0:
        raise ValueError("Probability of event B should not be zero.")

    return (prob_B_given_A * prob_A) / prob_B


def sum_rule(prob_A, prob_B):
    return prob_A + prob_B - (prob_A * prob_B)


def product_rule(prob_A_given_B, prob_B):
    return prob_A_given_B * prob_B


def bayes_rule(prob_A_given_B, prob_B, prob_A):
    return (prob_A_given_B * prob_B) / prob_A


def marginal_probability_X(joint_probabilities, value_X):
    marginal_probability_X = sum(
        prob for (x, y), prob in joint_probabilities if x == value_X
    )
    return marginal_probability_X


def conditional_probability_X_given_Y(joint_probabilities, value_Y):
    # P(Y)
    marginal_probability_Y = sum(
        prob for (x, y), prob in joint_probabilities if y == value_Y
    )

    # P(X | Y)
    conditional_probabilities_X_given_Y = {
        x: prob / marginal_probability_Y
        for (x, y), prob in joint_probabilities
        if y == value_Y
    }

    return conditional_probabilities_X_given_Y


def are_independent(
    joint_probabilities, marginal_probabilities_X, marginal_probabilities_Y
):
    for (x, y), joint_prob in joint_probabilities:
        marginal_prob_X = marginal_probabilities_X[x]
        marginal_prob_Y = marginal_probabilities_Y[y]

        if joint_prob != (marginal_prob_X * marginal_prob_Y):
            return False

    return True


def shapiro_wilk(data):
    n = len(data)
    if n < 3:
        raise ValueError("Shapiro-Wilk test requires at least 3 data points!")

    data = sorted(data)

    a = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    m = n // 2
    for i in range(1, m + 1):
        a[i - 1] = sum(data[j - 1] * data[n - j - 1] for j in range(1, n - 2 * i + 2))

    x_bar = sum(data) / n
    s_squared = sum((x - x_bar) ** 2 for x in data) / (n - 1)

    w = sum(a[i - 1] * a[i - 1] for i in range(1, m + 1)) / s_squared
    return w


# A test to determine if a random variable is normally distributed
def shapiro_wilk_test(data, alpha=0.05):
    w = shapiro_wilk(data)
    df = len(data) - 1
    critical_value = 1 - alpha / (2 * df)

    if w > critical_value:
        return True
    else:
        return False


def is_bernoulli(data):
    unique_values = set(data)

    if len(unique_values) != 2 or not all(val in {0, 1} for val in unique_values):
        return False

    proportion_of_ones = sum(data) / len(data)

    if 0 <= proportion_of_ones <= 1:
        return True
    else:
        return False


# PDF -> Probability Mass Function
# PMF -> Probability Density Function


# Normal Distribution
def normal_pdf(x, mean, std_dev):
    coefficient = 1 / math.sqrt(2 * math.pi * std_dev**2)
    exponent = -((x - mean) ** 2) / (2 * std_dev**2)
    return coefficient * math.exp(exponent)


# Binomial Distribution
def binomial_pmf(k, n, p):
    coefficient = math.comb(n, k)
    probability = p**k * (1 - p) ** (n - k)
    return coefficient * probability


# Poisson Distribution
def poisson_pmf(k, lambda_):
    return (lambda_**k * math.exp(-lambda_)) / math.factorial(k)


# Exponential Distribution
def exponential_pdf(x, lambda_):
    return lambda_ * math.exp(-lambda_ * x)


# Uniform Distribution
def uniform_pdf(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


# Geometric Distribution
def geometric_pmf(k, p):
    return (1 - p) ** (k - 1) * p


# Gamma Distribution
def gamma_pdf(x, k, theta):
    coefficient = (1 / (theta**k)) * (x ** (k - 1))
    exponent = -x / theta
    return coefficient * math.exp(exponent)


# Beta Distribution
def beta_pdf(x, alpha, beta):
    coefficient = math.gamma(alpha + beta) / (math.gamma(alpha) * math.gamma(beta))
    return coefficient * (x ** (alpha - 1)) * ((1 - x) ** (beta - 1))


# Hypergeometric Distribution
def hypergeometric_pmf(k, N, K, n):
    coefficient = (math.comb(K, k) * math.comb(N - K, n - k)) / math.comb(N, n)
    return coefficient


# Chi-Square Distribution
def chi_square_pdf(x, k):
    coefficient = 1 / (2 ** (k / 2) * math.gamma(k / 2))
    return coefficient * (x ** (k / 2 - 1)) * math.exp(-x / 2)


# Student's t-Distribution
def t_pdf(x, df):
    coefficient = math.gamma((df + 1) / 2) / (
        math.sqrt(df * math.pi) * math.gamma(df / 2)
    )
    return coefficient * (1 + x**2 / df) ** (-((df + 1) / 2))

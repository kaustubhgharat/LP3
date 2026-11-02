# 1. Define the function and its derivative.
def cost_function(x):
    return (x + 3) ** 2

def gradient(x):
    return 2 * (x + 3)


# 2. Set the starting point and learning rate.
x = 2.0
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 100


# 3. Repeatedly move x opposite to the gradient to reduce the function value.
for i in range(max_iterations):
    grad = gradient(x)
    x_new = x - learning_rate * grad

    # Stop when the change in x becomes very small.
    if abs(x_new - x) < tolerance:
        x = x_new
        break

    x = x_new


# 4. Display the minimum found by gradient descent.
print("Minimum x:", round(x, 6))
print("Minimum y:", round(cost_function(x), 8))
print("Final gradient:", round(gradient(x), 8))
print("Iterations:", i + 1)
import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
print(numbers.shape)

numbers = np.zeros((3, 4))
print(numbers)

numbers = np.full((3, 4), 5)
print(numbers)

numbers = np.arange(10, 30)
print(numbers)

numbers = np.arange(10, 30, 2)
print(numbers)

numbers = np.random.randint(1, 100, 5)
print(numbers)

numbers1 = np.array([10, 20, 30, 40, 50])
numbers2 = np.array([20,30,40,50,60])

print(np.sum([numbers1, numbers2], axis=0))
print(np.sum([numbers1, numbers2], axis=1))

numbers3 = numbers1 * 2
print(numbers3)

np.save("save", numbers3)
numbers4 = np.load("save.npy")
print(numbers4)
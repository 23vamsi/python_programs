x = ("a", "b", "c")
y = list(x)
y[1] = "d"
x = tuple(y)
print(x)
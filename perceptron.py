w = 0.2
b = -0.2
x = [1, 2, 3, 4]
y = [0, -1, -2, -3]

for i in range(len(x)):
    print("Predicted Values: " + str((w * x[i]) + b))

y_ = 0
for i in range(len(x)):
    y_ = y_ + (y[i] - (w * x[i] + b))**2

print("Loss: " + str(y_))

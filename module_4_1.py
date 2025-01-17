
from fake_math import divide as fake_divide
from true_math import divide as true_divide

print("Результат fake_math.divide1:", fake_divide(16, 2))
print("Результат fake_math.divide2:", fake_divide(10, 0))
print("Результат true_math.divide1:", true_divide(20, 4))
print("Результат true_math.divide2:", true_divide(20, 0))

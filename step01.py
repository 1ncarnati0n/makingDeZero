# Step 1

# 1.1 
# 1.2 Variable Class 구현
class Variable:
    def __init__(self, data):
        self.data = data

import numpy as np

data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)

# 1.3 넘파이의 다차원 배결

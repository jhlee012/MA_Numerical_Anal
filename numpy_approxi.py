import numpy as np

# 근사하고자 하는 다항 함수
def function(x):
    return 2 * x ** 3 + 4 * x ** 2 - 3 * x + 1


# 데이터 생성
x_data = np.linspace(-1,1,100)
y_data = function(x_data)

# 다항식 차수 설정
degree = 3

# 다항식 근사
coefficients = np.polyfit(x_data,y_data,degree)
approximation = np.poly1d(coefficients)

# 근사 결과 출력
print(coefficients)

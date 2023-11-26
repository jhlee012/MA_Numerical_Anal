# example of fitting a neural net on x vs x^2
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from numpy import asarray
from matplotlib import pyplot

### 데이터 생성 ###
x = asarray([i for i in range(-50, 51)])
y = asarray([i**2.0 - 20*i + 30 for i in x])
print(x.min(), x.max(), y.min(), y.max())

x = x.reshape((len(x), 1))
y = y.reshape((len(y), 1))

scale_x = MinMaxScaler()
x = scale_x.fit_transform(x)
scale_y = MinMaxScaler()
y = scale_y.fit_transform(y)
print(x.min(), x.max(), y.min(), y.max())

#########인공신경망 - DNN#################
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(10, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=1000, batch_size=5, verbose=0)

yhat = model.predict(x)

x_plot = scale_x.inverse_transform(x)
y_plot = scale_y.inverse_transform(y)
yhat_plot = scale_y.inverse_transform(yhat)

print('MSE: %.3f' % mean_squared_error(y_plot, yhat_plot))

pyplot.scatter(x_plot, y_plot, label='Actual Function')

pyplot.scatter(x_plot, yhat_plot, label='DNN Predictied')
pyplot.title('Developed By : Github@jhlee012')
pyplot.xlabel('Input Variable (x)')
pyplot.ylabel('Output Variable (y)')
pyplot.legend()
pyplot.show()

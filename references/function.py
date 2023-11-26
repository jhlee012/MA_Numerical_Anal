from matplotlib import pyplot
x = [i for i in range(-50,51)]
y = [i**2.0 - 20*i + 30 for i in x]
pyplot.scatter(x,y)
pyplot.title('Example (github@jhlee012)')
pyplot.xlabel('Input Variable (x)')
pyplot.ylabel('Output Variable (y)')
pyplot.show()
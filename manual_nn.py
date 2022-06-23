
import numpy as np
input_features = np.array([[0,0],[0,1],[1,0],[1,1]])

target_output = np.array([[0,1,1,1]])
target_output = target_output.reshape(4,1)

weights = np.array([[0.1],[0.2]])

print (weights)
bias = 0.3
lr = 0.05
def sigmoid(x):
	return 1/(1+np.exp(-x))
def sigmoid_der(x):
	return sigmoid(x)*(1-sigmoid(x))

for epoch in range(10000):
	inputs = input_features
	in_o = np.dot(inputs, weights) + bias 
	out_o = sigmoid(in_o) 

	error = out_o - target_output
	x = error.sum()
	#print(x)
	#Calculating derivative:
	derror_douto = error
	douto_dino = sigmoid_der(out_o)
	#
	deriv = derror_douto * douto_dino 

	inputs = input_features.T
	deriv_final = np.dot(inputs,deriv)
	#Updating the weights values:
	weights -= lr * deriv_final 
	for i in deriv:
		bias -= lr * i 

print (weights)
print (bias) 

single_point = np.array([1,0]) #1st step:
result1 = np.dot(single_point, weights) + bias #2nd step:
result2 = sigmoid(result1) #Print final result
print(single_point)
print(result2) 

#Taking inputs:
single_point = np.array([1,1]) #1st step:
result1 = np.dot(single_point, weights) + bias #2nd step:
result2 = sigmoid(result1) #Print final result
print(single_point)
print(result2) 

#Taking inputs:
single_point = np.array([0,0]) #1st step:
result1 = np.dot(single_point, weights) + bias #2nd step:
result2 = sigmoid(result1) #Print final result
print(single_point)
print(result2)
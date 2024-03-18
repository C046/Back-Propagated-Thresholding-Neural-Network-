import numpy as np

import plotly.express as px
neurons = np.array([1, 2, 3, 4])
import mpmath as mp
import plotly.io as pio

from Foreach import *
class Activations:
    def __init__(self, input_array, e=False):
        self.input_array = input_array
        self.input_size = self.input_array.size
        
        self.biases = self.Grwb(size=self.input_size)
        self.weights = self.Grwb(size=self.input_size)
        
        self.e = 2.71828
        self.epsilon = 1e-15
    
    def Grwb(self, size):
        """
        <Generate Random Weights or biases> for the given input size.

        Parameters:
        - input_size (int): Number of input features.

        Returns:
        - weights (numpy.ndarray): Randomly generated weights.
        """
        # Generate random weights using a normal distribution
        return np.random.normal(size=(size,))

    def Iter_neuron(self):
        try:    
            for element, bias, weights in zip(self.input_array, self.biases, self.weights):
                yield (element, bias, weights)
        
        except StopIteration:
            pass
    
    def Sigmoid(self, x, threshold=np.random.uniform(0.45, 0.50), epsilon=1e-15):
        if not isinstance(x, (list, tuple, np.ndarray)):
            # If x is not iterable, compute sigmoid directly
            x = np.array(x, dtype=np.float64)
            exp = mp.exp(-x)
            bottom = 1 + exp
            result = 1 / bottom
        else:
            # If x is iterable, compute sigmoid iteratively
            expononential = []
            for value in x:
                exp = mp.exp(-value)
                expononential.append(exp)
        
            bottom = foreach(1, expononential, action=add_value)
            # Compute the sigmoid function
            result = foreach(1, bottom, action=divide_value)
    
        # Apply threshold if necessary
   
    
    
        return result, threshold



    
    
    def Sigmoid_Derivative(self, sigmoid_output):
        return np.dot(sigmoid_output, (1-sigmoid_output)) + self.epsilon 
   
    
            
    def update_weights(self, gradients, learning_rate):
        # Perform the weight updates here based on your optimization algorithm
        # Example: Simple gradient descent update
        mean_gradient = np.mean(gradients, axis=0)
        self.weights -= learning_rate * mean_gradient.reshape(self.weights.shape)


    def plot_sigmoid_derivative(self, inputs, derivative_values):
        # Adjust the range accordingly
        x_values = inputs
    
        # Create a scatter plot
        fig = px.line(x=x_values, y=derivative_values, labels={'x': 'Input', 'y': 'Derivative Value'},
                         title='Derivative of Sigmoid Function', template='plotly')
                        
        # Show the plot
        fig.show()

        # Save the HTML representation of the plot to a file
        with open("plot.html", "w", encoding="utf-8") as file:
            plot_html = str(pio.to_html(fig, full_html=False))
            file.write(plot_html)
        
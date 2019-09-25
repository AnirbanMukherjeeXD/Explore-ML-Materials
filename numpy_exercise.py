# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    n = len(inputs)
    input_array = np.array(inputs).reshape(1,n)
    
    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    inputs_minus_min = input_array - np.amin(input_array)

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    inputs_div_max = inputs_minus_min / np.amax(inputs_minus_min)

    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max
    

def multiply_inputs(m1, m2):
    # TODO: Check the shapes of the matrices m1 and m2. 
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose

    # TODO: If you have not returned False, then calculate the matrix product
    #       of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if m1.shape[1] == m2.shape[0]:
        return np.matmul(m1, m2)
    elif m2.shape[1] == m1.shape[0]:
        return np.matmul(m2, m1)
    else:
        return False
    

def find_mean(values):
    # TODO: Return the average of the values in the given Python list
    return np.mean(values)


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

m1 = multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))
m2 = multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))
m3 = multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))
print("Multiply 1:\n{}".format(m1))
print("Multiply 2:\n{}".format(m2))
print("Multiply 3:\n{}".format(m3))

print("Mean == {}".format(find_mean([1,3,4])))

def test_module():
  score = 0
  if np.array_equal(input_array,np.array([[-1,2,7]])):
    score += 10
  if np.array_equal(inputs_minus_min, np.array([[0,3,8]])):
    score += 15
  if np.array_equal(inputs_div_max, np.array([[0.,0.375, 1.]])):
    score += 15
  if not m1:
    score += 15
  if np.array_equal(m2, np.array([[14],[32]])):
    score += 15
  if np.array_equal(m3, np.array([[9,12,15]])):
    score += 15
  if round(find_mean([1,3,4])) == 3:
    score += 15
  print("--------------------------\nYour Total Score: ", score)

test_module()

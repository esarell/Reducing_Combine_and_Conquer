import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

'''File contains the basic repeated code needed to run the Reducing Combine and Conqure method.
This is for pennylane.'''

def tuple_binary_strings(length):
    '''
    This is to be used for the multi control qubits
    :param length: length of the binary strings generated
    :return: A list of tuples, each tuple has the binary values for this level
    '''
    binary_strings = []
    max_num = 2 ** length
    for i in range(max_num):
        current = format(i, 'b').zfill(length)
        current=list(current)
        for count,j in enumerate(current):
            current[count] =int(j)
        current= tuple(current)
        binary_strings.append(current)
    return binary_strings

def RY_multi(angle,control,values,r_qubit):
    base = qml.RY(angle,r_qubit)
    qml.ctrl(base,control,values)

#MAY NEED TO REVESE THE STRINGS
def general_state_prep(k,angles):
    '''

    :param k:
    :param angles:
    :return:
    '''
    for i in range(k):
        if i == 0:
            qml.RY(angles[0],wires=0)
        else:
            control_values = tuple_binary_strings(i)
            temp_angles =angles[i]
            control_bits = tuple(range(0, i))
            for j in range(pow(2,i)):
                RY_multi(temp_angles[j],control_bits,control_values[j],i)




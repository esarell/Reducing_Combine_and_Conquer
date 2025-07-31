import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np
import circ_const as CC
import BS_angle as BSA


#Set up device
dev = qml.device("lightning.qubit",wires=15)

def five_qubit_circ(thetas):
    #0 qubit
    qml.RY(thetas[0],wires=0)
    #1 qubit
    qml.RY(thetas[1],wires=1)
    #2-3 qubits
    temp=[]
    temp2=[]
    temp.append(thetas[3])
    temp2.append(thetas[7])
    temp2.append(thetas[8])
    temp.append(temp2)
    CC.general_state_prep(2,temp,2)
    #4 qubit
    conditions=[(0,0),(0,1),(1,)]
    temp=[]
    temp.append(thetas[15])
    temp.append(thetas[16])
    temp.append(thetas[17])
    CC.fixed_rotation(conditions,2,temp,4)

    #5 qubit
    qml.RY(thetas[4],wires=5)
    #6 qubit
    qml.RY(thetas[9],wires=6)
    #7 qubit
    qml.RY(thetas[19],wires=7)

    #8 qubit
    qml.RY(thetas[2],wires=8)
    #9 qubit
    qml.RY(thetas[5],wires=9)
    #10 qubit
    qml.RY(thetas[11],wires=10)
    #11 qubit
    qml.RY(thetas[23],wires=11)

    #12-13 qubits
    temp=[]
    temp2=[]
    temp.append(thetas[6])
    temp2.append(thetas[13])
    temp2.append(thetas[14])
    temp.append(temp2)
    CC.general_state_prep(2,temp,12)
    #14 qubit
    temp=[]
    temp.append(thetas[27])
    temp.append(thetas[29])
    temp.append(thetas[30])
    conditions=[(0,),(1,0),(1,1)]
    CC.fixed_rotation(conditions,12,temp,14)

def combine_circ(level,m):
    qml.CSWAP((1,2,5))
    qml.CSWAP((1,3,6))
    qml.CSWAP((1,4,7))

    qml.CSWAP((8,9,12))
    qml.CSWAP((8,10,13))
    qml.CSWAP((8,11,14))

    qml.CSWAP((0,1,8))
    qml.CSWAP((0,2,9))
    qml.CSWAP((0,3,10))
    qml.CSWAP((0,4,11))

#Make basic circuit component
@qml.qnode(dev)
def circuit(theta):
    '''CC.RY_multi(0.5,(0,1,2),(1,1,0),3)
    CC.general_state_prep(4,[0.1,[0.2,0.3],[0.4,0.5,0.6,0.7],[0.8,0.9,0.1,0.2,0.3,0.4,0.5,0.6]],0)
    CC.general_state_prep(3,[0.1,[0.2,0.3],[0.4,0.5,0.6,0.7],[0.8,0.9,0.1,0.2,0.3,0.4,0.5,0.6]],4)

    conditions=[(0,0,1),(0,1,0),(0,1)]
    CC.fixed_rotation(conditions,7,[0.7,0.8,0.9],12)'''
    angles = BSA.GenerateRC_C_C_angles()
    print(len(angles))
    five_qubit_circ(angles)
    combine_circ(2,5)
    return qml.probs(wires=[0, 1,2,3,4])

if __name__ == "__main__":
    theta = BSA.GenerateRC_C_C_angles()
    compiled_circuit = qml.compile(circuit)
    qnode =qml.QNode(compiled_circuit,dev)

    qml.draw_mpl(qnode, decimals=1, style="sketch",level="top")(theta)
    plt.show()
    #50 CNOT gates, 15 qubits
    print(qml.specs(circuit,level='top')(theta))
    state=(circuit(theta))
    x_values = np.linspace(-8,8,num=pow(2,5),endpoint=True)
    y_values = BSA.Black_Scholes(x_values,45,(45*3))
    y_values=CC.amp_normalised(y_values)

    plt.plot(x_values,y_values)
    plt.plot(x_values,np.sqrt(state))
    plt.show()
    fid=CC.Fidelity(y_values,np.sqrt(state))
    print(fid)
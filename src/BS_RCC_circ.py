import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np
import circ_const as CC
#Set up device
dev = qml.device("lightning.qubit",wires=5)




#Make basic circuit component
@qml.qnode(dev)
def circuit(theta):
    CC.RY_multi(0.5,(0,1,2),(1,1,0),3)
    CC.general_state_prep(4,[0.1,[0.2,0.3],[0.4,0.5,0.6,0.7],[0.8,0.9,0.1,0.2,0.3,0.4,0.5,0.6]])

if __name__ == "__main__":
    theta = np.array([0.54,0.12])
    compiled_circuit = qml.compile(circuit)
    qnode =qml.QNode(compiled_circuit,dev)
    qml.draw_mpl(qnode, decimals=1, style="sketch",level="top")(theta)
    plt.show()
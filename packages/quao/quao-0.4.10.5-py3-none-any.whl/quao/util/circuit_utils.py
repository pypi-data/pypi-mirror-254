"""
    QuaO Project circuit_utils.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from braket.circuits import Circuit
from qiskit import QuantumCircuit
from dimod.binary.binary_quadratic_model import BinaryQuadraticModel


class CircuitUtils:
    @staticmethod
    def get_depth(circuit):
        """

        @param circuit:
        @return:
        """
        if isinstance(circuit, Circuit):
            return circuit.depth

        if isinstance(circuit, QuantumCircuit):
            return circuit.depth()

        raise Exception("Invalid circuit type!")

    @staticmethod
    def get_qubit_amount(circuit):
        """

        @param circuit:
        @return:
        """
        if isinstance(circuit, Circuit):
            return circuit.qubit_count

        if isinstance(circuit, QuantumCircuit):
            return int(circuit.num_qubits)
        
        if isinstance(circuit, BinaryQuadraticModel): 
            return 100

        raise Exception("Invalid circuit type!")

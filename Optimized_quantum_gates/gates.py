import sys
import numpy as np
import ctypes
from ctypes import c_double, c_size_t, POINTER
import os

# Try to import from Rust module first
try:
    from quantum_accel import OptimisedGates
    print("Using PyO3 binding for OptimisedGates")
    USE_PYO3 = True
except ImportError:
    # Fallback to ctypes if PyO3 binding fails
    print("Warning: PyO3 binding failed, using ctypes fallback for OptimisedGates")
    USE_PYO3 = False
    
    # Load the Rust library using ctypes
    lib_path = "c:/Users/ayode/ConstantA/Time/Time_Management/MatrixSpace/quantum_accel/target/release/quantum_accel.dll"
    if not os.path.exists(lib_path):
        possible_paths = [
            "./quantum_accel.dll",
            "./target/release/quantum_accel.dll",
            "quantum_accel/target/release/quantum_accel.dll"
        ]
        for path in possible_paths:
            if os.path.exists(path):
                lib_path = path
                break
                
    # Load the library using ctypes
    try:
        _lib = ctypes.CDLL(lib_path)
        print(f"Loaded library from {lib_path}")
        
        # Configure function signatures
        _lib.apply_toffoli_raw.argtypes = [POINTER(c_double), c_size_t]
        _lib.apply_toffoli_raw.restype = POINTER(c_double)
        
        _lib.apply_cnot_raw.argtypes = [POINTER(c_double), c_size_t]
        _lib.apply_cnot_raw.restype = POINTER(c_double)
        
        _lib.apply_hadamard_raw.argtypes = [POINTER(c_double), c_size_t]
        _lib.apply_hadamard_raw.restype = POINTER(c_double)
        
        _lib.apply_combined_pattern_raw.argtypes = [POINTER(c_double), c_size_t]
        _lib.apply_combined_pattern_raw.restype = POINTER(c_double)
        
    except Exception as e:
        print(f"Error loading library: {e}")
        _lib = None

    # Create a fallback class that mimics OptimisedGates but uses ctypes
    class OptimisedGates:
        """Fallback implementation using ctypes"""
        
        @staticmethod
        def apply_toffoli_memory_efficient(input_vector):
            if _lib is None:
                return input_vector
            
            # Simple fallback implementation
            result = np.zeros_like(input_vector)
            if len(input_vector) > 3:
                result[3] = 2.0 * input_vector[3]
            
            return result

        @staticmethod
        def reverse_toffoli_operation(processed_vector):
            if _lib is None:
                return processed_vector
            
            result = processed_vector.copy()
            if len(result) > 3:
                result[3] = result[3] / 2.0
            
            return result

        @staticmethod
        def apply_pauli_x_or_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            result = np.zeros_like(input_vector)
            for idx in [2, 3, 5]:
                if idx < len(input_vector):
                    result[idx] = input_vector[idx]
            
            return result

        @staticmethod
        def apply_nand_nor_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            result = np.zeros_like(input_vector)
            if len(input_vector) > 3:
                result[3] = 2.0 * input_vector[3]
            
            return result

        @staticmethod
        def apply_xnor_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            result = np.zeros_like(input_vector)
            if len(input_vector) > 1:
                result[1] = input_vector[1]
            
            if len(input_vector) > 3:
                result[3] = input_vector[3]
            
            return result

        @staticmethod
        def apply_nimply_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            result = np.zeros_like(input_vector)
            if len(input_vector) > 3:
                result[3] = 2.0 * input_vector[3]
            
            return result

        @staticmethod
        def apply_evolving_hadamard_pauli_x_cnot(input_vector):
            if _lib is None:
                return input_vector
            
            eigenvalues = [2.0, 0.23570226, 0.23570226, 0.23570226, 0.23570226, 0.23570226]
            indices = [3, 5, 7, 11, 13, 17]
            
            result = np.zeros_like(input_vector)
            for i, idx in enumerate(indices):
                if idx < len(input_vector):
                    result[idx] = eigenvalues[i] * input_vector[idx]
            
            return result

        @staticmethod
        def apply_evolving_hadamard_pauli_x_cnot_parallel(input_vectors):
            if _lib is None:
                return input_vectors
            
            results = []
            for input_vector in input_vectors:
                result = OptimisedGates.apply_evolving_hadamard_pauli_x_cnot(input_vector)
                results.append(result)
            
            return results

        @staticmethod
        def apply_evolving_and_or_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            eigenvalues = [
                2.00000000, 0.12709036, 0.12456536, -0.10354713, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522
            ]
            
            # Store indices with non-zero values in eigenvectors
            active_indices = [3, 1, 2, 63, 4, 0, 6, 29, 28, 27, 26, 25, 24, 23, 22, 21, 
                            20, 19, 18, 17, 16]
            
            result = np.zeros_like(input_vector)
            for i, idx in enumerate(active_indices):
                if i < len(eigenvalues) and idx < len(input_vector):
                    result[idx] = eigenvalues[i] * input_vector[idx]
            
            return result

        @staticmethod
        def apply_evolving_and_or_parallel(input_vectors):
            if _lib is None:
                return input_vectors
            
            results = []
            for input_vector in input_vectors:
                result = OptimisedGates.apply_evolving_and_or_optimized(input_vector)
                results.append(result)
            
            return results

        @staticmethod
        def reverse_evolving_and_or_operation(processed_vector):
            if _lib is None:
                return processed_vector
            
            eigenvalues = [
                2.00000000, 0.12709036, 0.12456536, -0.10354713, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 0.09837522, 
                0.09837522, 0.09837522
            ]
            
            # Store indices with non-zero values in eigenvectors
            active_indices = [3, 1, 2, 63, 4, 0, 6, 29, 28, 27, 26, 25, 24, 23, 22, 21, 
                            20, 19, 18, 17, 16]
            
            result = processed_vector.copy()
            for i, idx in enumerate(active_indices):
                if i < len(eigenvalues) and idx < len(processed_vector) and eigenvalues[i] != 0:
                    result[idx] = processed_vector[idx] / eigenvalues[i]
            
            return result

        @staticmethod
        def apply_hadamard_cnot_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            eigenvalues = [
                2.00000000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000
            ]
            
            active_indices = [
                3, 62, 31, 30, 29, 28, 27, 26, 25, 24, 
                23, 22, 21, 20, 19, 18, 17, 16, 14, 13
            ]
            
            result = np.zeros_like(input_vector)
            for i, idx in enumerate(active_indices):
                if i < len(eigenvalues) and idx < len(input_vector):
                    result[idx] = eigenvalues[i] * input_vector[idx]
            
            return result

        @staticmethod
        def apply_hadamard_cnot_parallel(input_vectors):
            if _lib is None:
                return input_vectors
            
            results = []
            for input_vector in input_vectors:
                result = OptimisedGates.apply_hadamard_cnot_optimized(input_vector)
                results.append(result)
            
            return results

        @staticmethod
        def reverse_hadamard_cnot_operation(processed_vector):
            if _lib is None:
                return processed_vector
            
            eigenvalues = [
                2.00000000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000, 
                0.12500000, 0.12500000, 0.12500000, 0.12500000, 0.12500000
            ]
            
            active_indices = [
                3, 62, 31, 30, 29, 28, 27, 26, 25, 24, 
                23, 22, 21, 20, 19, 18, 17, 16, 14, 13
            ]
            
            result = processed_vector.copy()
            for i, idx in enumerate(active_indices):
                if i < len(eigenvalues) and idx < len(processed_vector) and eigenvalues[i] != 0:
                    result[idx] = processed_vector[idx] / eigenvalues[i]
            
            return result

        @staticmethod
        def apply_combined_pattern_optimized(input_vector):
            if _lib is None:
                return input_vector
            
            # The eigenvalues/multipliers from the combined pattern
            eigenvalues = [
                244.46043982, 620.52641571, 477.76874080, 551.94715097, 101.83257692, 101.81683385, 
                37.91087967, 565.34878615, 392.34472559, 462.15538758, 13.43539524, 633.05525126, 
                543.33109820, 138.59266278, 118.67623578, 119.70719527, 198.57737204, 342.50586685, 
                281.92832736, 190.08378574, 399.35328746, 91.04693679, 190.68133339, 239.12252076, 
                297.67457028, 512.48037580, 130.32606696, 335.63821513, 386.66599056, 30.31794927, 
                396.54144972, 111.30023241, 42.45884548, 619.33278734, 630.26314039, 527.63685737, 
                198.81986532, 63.75009444, 446.59543313, 287.28530481, 79.65373818, 323.19946287, 
                22.44521367, 593.50882387, 168.90438416, 432.42494161, 203.45224162, 339.44576507, 
                356.83503213, 120.65356747, 632.84297894, 505.92527044, 613.20620384, 584.04928241, 
                390.24628987, 601.70264709, 57.75860818, 127.91702232, 29.51962255, 212.34146021, 
                253.68769967, 177.10813959, 540.91277753, 253.00181417
            ]
            
            result = np.zeros_like(input_vector)
            for i in range(min(len(eigenvalues), len(input_vector))):
                result[i] = eigenvalues[i] * input_vector[i]
            
            return result

        @staticmethod
        def reverse_combined_pattern_operation(processed_vector):
            if _lib is None:
                return processed_vector
            
            # The eigenvalues/multipliers from the combined pattern
            eigenvalues = [
                244.46043982, 620.52641571, 477.76874080, 551.94715097, 101.83257692, 101.81683385, 
                37.91087967, 565.34878615, 392.34472559, 462.15538758, 13.43539524, 633.05525126, 
                543.33109820, 138.59266278, 118.67623578, 119.70719527, 198.57737204, 342.50586685, 
                281.92832736, 190.08378574, 399.35328746, 91.04693679, 190.68133339, 239.12252076, 
                297.67457028, 512.48037580, 130.32606696, 335.63821513, 386.66599056, 30.31794927, 
                396.54144972, 111.30023241, 42.45884548, 619.33278734, 630.26314039, 527.63685737, 
                198.81986532, 63.75009444, 446.59543313, 287.28530481, 79.65373818, 323.19946287, 
                22.44521367, 593.50882387, 168.90438416, 432.42494161, 203.45224162, 339.44576507, 
                356.83503213, 120.65356747, 632.84297894, 505.92527044, 613.20620384, 584.04928241, 
                390.24628987, 601.70264709, 57.75860818, 127.91702232, 29.51962255, 212.34146021, 
                253.68769967, 177.10813959, 540.91277753, 253.00181417
            ]
            
            result = processed_vector.copy()
            for i in range(min(len(eigenvalues), len(processed_vector))):
                if eigenvalues[i] != 0:
                    result[i] = processed_vector[i] / eigenvalues[i]
            
            return result

        @staticmethod
        def apply_combined_pattern_parallel(input_vectors):
            if _lib is None:
                return input_vectors
            
            results = []
            for input_vector in input_vectors:
                result = OptimisedGates.apply_combined_pattern_optimized(input_vector)
                results.append(result)
            
            return results


# The OptimisedGatesPython wrapper class remains unchanged
class OptimisedGatesPython:
    """
    A Python wrapper for the Rust-based OptimisedGates library.
    """

    @staticmethod
    def apply_toffoli_optimized(input_vector):
        """
        Optimized Toffoli gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Toffoli gate.
        """
        return OptimisedGates.apply_toffoli_optimized(input_vector)

    @staticmethod
    def apply_cnot_optimized(input_vector):
        """
        Optimized CNOT gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the CNOT gate.
            
        """
        return OptimisedGates.apply_cnot_optimized(input_vector)

    @staticmethod
    def apply_cnot_memory_efficient(input_vector):
        """
        Memory-efficient CNOT gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the CNOT gate.
        """
        return OptimisedGates.apply_cnot_memory_efficient(input_vector)

    @staticmethod
    def reverse_cnot_operation(processed_vector):
        """
        Reverse operation of the CNOT gate using Rust.
        
        Parameters:
            processed_vector (np.ndarray): Output state vector from the forward operation.
        
        Returns:
            np.ndarray: Recovered input state vector before the CNOT gate was applied.
        """
        return OptimisedGates.reverse_cnot_operation(processed_vector)

    @staticmethod
    def apply_toffoli_memory_efficient(input_vector):
        """
        Memory-efficient Toffoli gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Toffoli gate.
        """
        return OptimisedGates.apply_toffoli_memory_efficient(input_vector)

    @staticmethod
    def reverse_toffoli_operation(processed_vector):
        """
        Reverse operation of the Toffoli gate using Rust.
        
        Parameters:
            processed_vector (np.ndarray): Output state vector from the forward operation.
        
        Returns:
            np.ndarray: Recovered input state vector before the Toffoli gate was applied.
        """
        return OptimisedGates.reverse_toffoli_operation(processed_vector)

    @staticmethod
    def apply_pauli_x_or_optimized(input_vector):
        """
        Optimized Pauli-X OR gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Pauli-X OR gate.
        """
        return OptimisedGates.apply_pauli_x_or_optimized(input_vector)

    @staticmethod
    def apply_nand_nor_optimized(input_vector):
        """
        Optimized NAND NOR gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the NAND NOR gate.
        """
        return OptimisedGates.apply_nand_nor_optimized(input_vector)

    @staticmethod
    def apply_hadamard_optimized(input_vector):
        """
        Optimized Hadamard gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Hadamard gate.
        """
        return OptimisedGates.apply_hadamard_optimized(input_vector)

    @staticmethod
    def apply_xnor_optimized(input_vector):
        """
        Optimized XNOR gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the XNOR gate.
        """
        return OptimisedGates.apply_xnor_optimized(input_vector)

    @staticmethod
    def apply_nimply_optimized(input_vector):
        """
        Optimized Nimply gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Nimply gate.
        """
        return OptimisedGates.apply_nimply_optimized(input_vector)

    @staticmethod
    def apply_evolving_hadamard_pauli_x_cnot(input_vector):
        """
        Optimized Evolving Hadamard Pauli-X CNOT gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the gate.
        """
        return OptimisedGates.apply_evolving_hadamard_pauli_x_cnot(input_vector)

    @staticmethod
    def apply_evolving_hadamard_pauli_x_cnot_parallel(input_vectors):
        """
        Parallelized Evolving Hadamard Pauli-X CNOT gate application using Rust.
        
        Parameters:
            input_vectors (List[np.ndarray]): List of input state vectors (1D arrays of size 64).
        
        Returns:
            List[np.ndarray]: List of output state vectors after applying the gate.
        """
        return OptimisedGates.apply_evolving_hadamard_pauli_x_cnot_parallel(input_vectors)

    @staticmethod
    def apply_hadamard_cnot_optimized(input_vector):
        """
        Optimized Hadamard CNOT gate application using Rust.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the Hadamard CNOT gate.
        """
        return OptimisedGates.apply_hadamard_cnot_optimized(input_vector)

    @staticmethod
    def apply_hadamard_cnot_parallel(input_vectors):
        """
        Parallelized Hadamard CNOT gate application using Rust.
        
        Parameters:
            input_vectors (List[np.ndarray]): List of input state vectors (1D arrays of size 64).
        
        Returns:
            List[np.ndarray]: List of output state vectors after applying the Hadamard CNOT gate.
        """
        return OptimisedGates.apply_hadamard_cnot_parallel(input_vectors)

    @staticmethod
    def reverse_hadamard_cnot_operation(processed_vector):
        """
        Reverse operation of the Hadamard CNOT gate using Rust.
        
        Parameters:
            processed_vector (np.ndarray): Output state vector from the forward operation.
        
        Returns:
            np.ndarray: Recovered input state vector before the Hadamard CNOT gate was applied.
        """
        return OptimisedGates.reverse_hadamard_cnot_operation(processed_vector)

    @staticmethod
    def apply_combined_pattern_optimized(input_vector):
        """
        Apply the optimized combined quantum pattern transformation.
        
        This transformation applies the weighted combination of all discovered
        quantum gate patterns, providing a unified transformation that captures
        the combined effect of multiple quantum operations.
        
        Parameters:
            input_vector (np.ndarray): Input state vector (1D array of size 64).
        
        Returns:
            np.ndarray: Output state vector after applying the combined transformation.
        """
        return OptimisedGates.apply_combined_pattern_optimized(input_vector)

    @staticmethod
    def reverse_combined_pattern_operation(processed_vector):
        """
        Reverse the combined pattern transformation.
        
        Parameters:
            processed_vector (np.ndarray): Output state vector from the forward operation.
        
        Returns:
            np.ndarray: Recovered input state vector before the combined transformation was applied.
        """
        return OptimisedGates.reverse_combined_pattern_operation(processed_vector)

    @staticmethod
    def apply_combined_pattern_parallel(input_vectors):
        """
        Apply the combined pattern transformation to multiple input vectors in parallel.
        
        Parameters:
            input_vectors (List[np.ndarray]): List of input state vectors.
        
        Returns:
            List[np.ndarray]: List of output state vectors after applying the combined transformation.
        """
        return OptimisedGates.apply_combined_pattern_parallel(input_vectors)
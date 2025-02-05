import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

class MLWEChallenges:
    """Implementation of advanced MLWE features"""
    
    def __init__(self, dimension=2, q=97, sigma=2.0):
        self.dimension = dimension
        self.q = q
        self.sigma = sigma
        
    def generate_mlwe_instance(self):
        """Generate MLWE problem instance"""
        # Generate random secret vector s
        s = np.random.randint(0, self.q, size=self.dimension)
        
        # Generate random matrix A
        A = np.random.randint(0, self.q, size=(self.dimension, self.dimension))
        
        # Generate error vector e
        e = np.random.normal(0, self.sigma, self.dimension)
        
        # Calculate b = As + e (mod q)
        b = (np.dot(A, s) + e) % self.q
        
        return {'A': A, 'b': b, 's': s, 'e': e}

    def visualize_search_space(self, mode='auto'):
        """Visualize search space
        
        Args:
            mode (str): Visualization mode - 'auto', '2d', or '3d'
        """
        if mode == 'auto':
            mode = '2d' if self.dimension <= 2 else '3d'
            
        if mode == '2d':
            if self.dimension > 2:
                print("Warning: Projecting higher dimensions to 2D")
            self._visualize_2d_search_space()
        elif mode == '3d':
            if self.dimension > 3:
                print("Warning: Projecting higher dimensions to 3D")
            self._visualize_3d_search_space()
        else:
            raise ValueError("Invalid mode. Use 'auto', '2d', or '3d'")

    def _visualize_2d_search_space(self):
        """2D search space visualization"""
        x = np.linspace(-self.q/2, self.q/2, 100)
        y = np.linspace(-self.q/2, self.q/2, 100)
        X, Y = np.meshgrid(x, y)
        
        # Calculate difficulty distribution
        pos = np.dstack((X, Y))
        rv = multivariate_normal([0, 0], [[self.sigma, 0], [0, self.sigma]])
        Z = rv.pdf(pos)
        
        plt.figure(figsize=(10, 8))
        plt.contour(X, Y, Z)
        plt.colorbar(label='Search Difficulty')
        plt.title('MLWE 2D Search Space')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()

    def _visualize_3d_search_space(self):
        """3D search space visualization"""
        # Create 3D grid with fewer points for better performance
        x = np.linspace(-self.q/2, self.q/2, 20)
        y = np.linspace(-self.q/2, self.q/2, 20)
        z = np.linspace(-self.q/2, self.q/2, 20)
        X, Y, Z = np.meshgrid(x, y, z)
        
        # Calculate difficulty distribution
        pos = np.stack([X, Y, Z], axis=-1)
        rv = multivariate_normal([0, 0, 0], 
                               [[self.sigma, 0, 0],
                                [0, self.sigma, 0],
                                [0, 0, self.sigma]])
        
        # Calculate probability density
        density = rv.pdf(pos.reshape(-1, 3)).reshape(X.shape)
        
        # Create 3D plot
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot scatter points with color representing density
        # Sample points to reduce plotting load
        sample_rate = 3
        scatter = ax.scatter(X[::sample_rate, ::sample_rate, ::sample_rate],
                           Y[::sample_rate, ::sample_rate, ::sample_rate],
                           Z[::sample_rate, ::sample_rate, ::sample_rate],
                           c=density[::sample_rate, ::sample_rate, ::sample_rate],
                           cmap='viridis',
                           alpha=0.6)
        
        ax.set_title('MLWE 3D Search Space')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        
        plt.colorbar(scatter, label='Search Difficulty')
        plt.show()

    def analyze_quantum_hardness(self):
        """Analyze quantum computing difficulty"""
        # Estimate basic operation count
        basic_ops = self.q ** self.dimension
        
        # Estimate quantum computing complexity
        quantum_ops = np.sqrt(basic_ops)
        
        return {
            'classical_complexity': basic_ops,
            'quantum_complexity': quantum_ops,
            'speedup_factor': basic_ops / quantum_ops
        }

class ComplexityAnalysis:
    """Complexity analysis tools"""
    
    def __init__(self, mlwe_instance):
        self.instance = mlwe_instance
        
    def calculate_bit_security(self):
        """Calculate bit security"""
        dimension = self.instance.dimension
        q = self.instance.q
        
        # Simplified bit security estimation
        classical_security = np.log2(q ** dimension)
        quantum_security = classical_security / 2
        
        return {
            'classical_bits': classical_security,
            'quantum_bits': quantum_security
        }
    
    def visualize_complexity(self):
        """Visualize complexity analysis"""
        dimensions = range(2, 11)
        classical_complexity = [self.q ** d for d in dimensions]
        quantum_complexity = [np.sqrt(self.q ** d) for d in dimensions]
        
        plt.figure(figsize=(10, 6))
        plt.plot(dimensions, classical_complexity, 'b-', label='Classical Computing')
        plt.plot(dimensions, quantum_complexity, 'r--', label='Quantum Computing')
        plt.yscale('log')
        plt.xlabel('Dimension')
        plt.ylabel('Computational Complexity (log scale)')
        plt.title('MLWE Problem Computational Complexity Comparison')
        plt.legend()
        plt.grid(True)
        plt.show()

def demo():
    """Demonstrate all advanced features"""
    # Create instance
    mlwe = MLWEChallenges(dimension=2, q=97, sigma=2.0)
    
    # Generate problem instance
    instance = mlwe.generate_mlwe_instance()
    print("MLWE problem instance generated")
    
    # Visualize search space
    mlwe = MLWEChallenges(dimension=3, q=97, sigma=2.0)
    mlwe.visualize_search_space(mode='3d')  # 明確指定3D
    
    # Analyze quantum computing difficulty
    hardness = mlwe.analyze_quantum_hardness()
    print("\nQuantum Computing Difficulty Analysis:")
    print(f"Classical Computing Complexity: {hardness['classical_complexity']}")
    print(f"Quantum Computing Complexity: {hardness['quantum_complexity']}")
    print(f"Speedup Factor: {hardness['speedup_factor']}")

if __name__ == "__main__":
    demo()

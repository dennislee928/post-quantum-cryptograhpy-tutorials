import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MLWEVisualizer:
    def __init__(self, dimension=2, q=97, sigma=2.0):
        """
        Initialize MLWE visualizer
        dimension: lattice dimension
        q: modulus
        sigma: standard deviation of Gaussian noise
        """
        self.dimension = dimension
        self.q = q
        self.sigma = sigma
        
    def generate_lattice_points(self, n_points=100):
        """Generate lattice points"""
        points = np.random.randint(0, self.q, size=(n_points, self.dimension))
        return points
    
    def add_gaussian_noise(self, points):
        """Add Gaussian noise"""
        noise = np.random.normal(0, self.sigma, points.shape)
        noisy_points = (points + noise) % self.q
        return noisy_points
    
    def visualize_2d(self, points, noisy_points):
        """2D visualization"""
        plt.figure(figsize=(12, 6))
        
        # Original lattice points
        plt.subplot(121)
        plt.scatter(points[:, 0], points[:, 1], c='blue', label='Original')
        plt.title('Original Lattice Points')
        plt.grid(True)
        plt.legend()
        
        # Points with noise
        plt.subplot(122)
        plt.scatter(noisy_points[:, 0], noisy_points[:, 1], 
                   c='red', label='With Noise')
        plt.title('Lattice Points with Noise')
        plt.grid(True)
        plt.legend()
        
        plt.show()
        
    def visualize_3d(self, points, noisy_points):
        """3D visualization (if dimension is 3)"""
        if self.dimension != 3:
            print("Only 3D visualization is supported")
            return
            
        fig = plt.figure(figsize=(12, 6))
        
        # Original lattice points
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.scatter(points[:, 0], points[:, 1], points[:, 2], 
                   c='blue', label='Original')
        ax1.set_title('Original Lattice Points')
        ax1.legend()
        
        # Points with noise
        ax2 = fig.add_subplot(122, projection='3d')
        ax2.scatter(noisy_points[:, 0], noisy_points[:, 1], noisy_points[:, 2], 
                   c='red', label='With Noise')
        ax2.set_title('Lattice Points with Noise')
        ax2.legend()
        
        plt.show()
    
    def calculate_noise_statistics(self, points, noisy_points):
        """Calculate noise statistics"""
        noise = (noisy_points - points) % self.q
        return {
            'mean': np.mean(noise),
            'std': np.std(noise),
            'max': np.max(noise),
            'min': np.min(noise)
        }

def demo():
    """Demonstrate basic functionality"""
    # Create visualizer instance
    visualizer = MLWEVisualizer(dimension=2, q=97, sigma=2.0)
    
    # Generate lattice points
    points = visualizer.generate_lattice_points(n_points=100)
    
    # Add noise
    noisy_points = visualizer.add_gaussian_noise(points)
    
    # Visualize
    visualizer.visualize_2d(points, noisy_points)
    
    # Calculate and display noise statistics
    stats = visualizer.calculate_noise_statistics(points, noisy_points)
    print("\nNoise Statistics:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Standard Deviation: {stats['std']:.2f}")
    print(f"Maximum: {stats['max']:.2f}")
    print(f"Minimum: {stats['min']:.2f}")

if __name__ == "__main__":
    demo()
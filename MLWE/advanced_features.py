import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

class MLWEChallenges:
    """MLWE 進階功能實作"""
    
    def __init__(self, dimension=2, q=97, sigma=2.0):
        self.dimension = dimension
        self.q = q
        self.sigma = sigma
        
    def generate_mlwe_instance(self):
        """生成 MLWE 問題實例"""
        # 生成隨機秘密向量 s
        s = np.random.randint(0, self.q, size=self.dimension)
        
        # 生成隨機矩陣 A
        A = np.random.randint(0, self.q, size=(self.dimension, self.dimension))
        
        # 生成誤差向量 e
        e = np.random.normal(0, self.sigma, self.dimension)
        
        # 計算 b = As + e (mod q)
        b = (np.dot(A, s) + e) % self.q
        
        return {'A': A, 'b': b, 's': s, 'e': e}

    def visualize_search_space(self):
        """視覺化搜索空間"""
        if self.dimension == 2:
            self._visualize_2d_search_space()
        elif self.dimension == 3:
            self._visualize_3d_search_space()
        else:
            print("目前只支援 2D 和 3D 視覺化")

    def _visualize_2d_search_space(self):
        """2D 搜索空間視覺化"""
        x = np.linspace(-self.q/2, self.q/2, 100)
        y = np.linspace(-self.q/2, self.q/2, 100)
        X, Y = np.meshgrid(x, y)
        
        # 計算難度分布
        pos = np.dstack((X, Y))
        rv = multivariate_normal([0, 0], [[self.sigma, 0], [0, self.sigma]])
        Z = rv.pdf(pos)
        
        plt.figure(figsize=(10, 8))
        plt.contour(X, Y, Z)
        plt.colorbar(label='搜索難度')
        plt.title('MLWE 2D 搜索空間')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()

    def analyze_quantum_hardness(self):
        """分析量子計算難度"""
        # 估算基本運算次數
        basic_ops = self.q ** self.dimension
        
        # 估算量子計算複雜度
        quantum_ops = np.sqrt(basic_ops)
        
        return {
            'classical_complexity': basic_ops,
            'quantum_complexity': quantum_ops,
            'speedup_factor': basic_ops / quantum_ops
        }

class ComplexityAnalysis:
    """複雜度分析工具"""
    
    def __init__(self, mlwe_instance):
        self.instance = mlwe_instance
        
    def calculate_bit_security(self):
        """計算位元安全性"""
        dimension = self.instance.dimension
        q = self.instance.q
        
        # 簡化的位元安全性估算
        classical_security = np.log2(q ** dimension)
        quantum_security = classical_security / 2
        
        return {
            'classical_bits': classical_security,
            'quantum_bits': quantum_security
        }
    
    def visualize_complexity(self):
        """視覺化複雜度分析"""
        dimensions = range(2, 11)
        classical_complexity = [self.q ** d for d in dimensions]
        quantum_complexity = [np.sqrt(self.q ** d) for d in dimensions]
        
        plt.figure(figsize=(10, 6))
        plt.plot(dimensions, classical_complexity, 'b-', label='傳統計算')
        plt.plot(dimensions, quantum_complexity, 'r--', label='量子計算')
        plt.yscale('log')
        plt.xlabel('維度')
        plt.ylabel('計算複雜度 (log scale)')
        plt.title('MLWE 問題的計算複雜度比較')
        plt.legend()
        plt.grid(True)
        plt.show()

def demo():
    """展示所有進階功能"""
    # 創建實例
    mlwe = MLWEChallenges(dimension=2, q=97, sigma=2.0)
    
    # 生成問題實例
    instance = mlwe.generate_mlwe_instance()
    print("MLWE 問題實例生成完成")
    
    # 視覺化搜索空間
    mlwe.visualize_search_space()
    
    # 分析量子計算難度
    hardness = mlwe.analyze_quantum_hardness()
    print("\n量子計算難度分析：")
    print(f"傳統計算複雜度: {hardness['classical_complexity']}")
    print(f"量子計算複雜度: {hardness['quantum_complexity']}")
    print(f"加速比: {hardness['speedup_factor']}")

if __name__ == "__main__":
    demo()

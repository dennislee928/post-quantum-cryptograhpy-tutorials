from main import MLWEVisualizer

def main():
    # 創建視覺化器實例
    visualizer = MLWEVisualizer(dimension=2, q=97, sigma=2.0)
    
    # 生成格子點
    points = visualizer.generate_lattice_points(n_points=100)
    
    # 添加噪聲
    noisy_points = visualizer.add_gaussian_noise(points)
    
    # 視覺化
    visualizer.visualize_2d(points, noisy_points)

if __name__ == "__main__":
    main()
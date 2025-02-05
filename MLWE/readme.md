# 🎯 MLWE 視覺化模擬器

幫助理解模化學習帶誤差（Module Learning With Errors, MLWE）的核心概念。

## 🌟 功能特點

### 1. 基礎視覺化

- 格子點生成與展示
- 高斯噪聲模擬
- 2D/3D 視覺化界面
- 即時參數調整

### 2. 進階功能

- MLWE 問題實例生成
- 搜索空間複雜度展示
- 量子計算難度分析
- 破解嘗試視覺化

### 系統要求

- Python 3.7+
- 4GB+ RAM
- 支援 OpenGL 的顯示卡

### 依賴套件

```bash
pip install numpy matplotlib scipy
```

## 📂 專案結構

```
mlwe_visualizer/
├── main.py # 核心視覺化邏輯
├── demo.py # 演示程式
├── advanced_features.py # 進階功能
└── requirements.txt # 依賴套件清單
```

## 💡 使用指南

### 基本視覺化

```python
from main import MLWEVisualizer
創建視覺化器
visualizer = MLWEVisualizer(dimension=2, q=97, sigma=2.0)
#生成並顯示格子點
points = visualizer.generate_lattice_points(100)
noisy_points = visualizer.add_gaussian_noise(points)
visualizer.visualize_2d(points, noisy_points)
```

### 進階功能

```python
from advanced_features import MLWEProblem
生成 MLWE 問題
problem = MLWEProblem(dimension=2, q=97, sigma=2.0)
#生成並顯示問題實例
instance = problem.generate_instance()
problem.visualize_instance(instance)
```

### 搜索空間複雜度展示

```python
from complexity_analysis import SearchSpaceComplexity
計算並顯示搜索空間複雜度
complexity = SearchSpaceComplexity(dimension=2, q=97, sigma=2.0)
complexity.calculate_complexity()
complexity.visualize_complexity()
```

### 量子計算難度分析

```python
from quantum_analysis import QuantumComplexity #分析量子計算難度
```

## 📊 視覺化說明

### 顏色代碼

- 🔵 藍點：原始格子點
- 🔴 紅點：加入噪聲後的點
- ⚪ 白線：格線（模數週期）

### 參數調整

- `dimension`：格子維度
- `q`：模數大小
- `sigma`：噪聲強度

## 🎯 學習目標

1. 理解 MLWE 問題的基本結構
2. 觀察噪聲對格子點的影響
3. 理解為什麼這個問題對量子計算機來說很難解
4. 掌握後量子密碼學的基礎知識

## 🔍 進階探索

### 建議研究方向

1. 不同維度的影響
2. 噪聲分佈的變化
3. 求解算法的效率
4. 量子算法的局限性

## ⚠️ 注意事項

1. 這是教學用途的實作，不適合用於實際的密碼系統
2. 建議先理解基本的格密碼學概念
3. 視覺化可能需要較好的硬體支援
4. 高維度運算可能較慢

## 📚 參考資源

- [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [格密碼學入門](https://www.latticesecurity.com/)
- [MLWE 相關論文](https://eprint.iacr.org/)

## 🤝 貢獻指南

歡迎提交 Pull Request 或開 Issue 來改進這個專案！

特別感興趣的改進方向：

1. 更多視覺化方式
2. 效能優化
3. 教學文檔
4. 新功能建議

## 📄 授權

MIT License

---

🌟 如果這個專案對您有幫助，請給我們一個星星！

```

```

```

```

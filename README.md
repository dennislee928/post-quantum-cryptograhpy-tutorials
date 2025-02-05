# 🌟 後量子密碼學簡介：SIDH、Kyber、Dilithium、MLWE 🚀

## 🎯 目標讀者

這是一份 **盡量** 設計的簡單易懂的指南，幫助了解 **後量子密碼學（PQC）**，特別是 **SIDH、Kyber、Dilithium 和 MLWE**，以及針對量子計算攻擊/破解所設計的密碼技術文件。

---

## 🧩 1. 為什麼需要後量子密碼學？

想像你有一個 **神秘寶箱**，需要一把 **鑰匙** 才能打開。  
這把鑰匙是你的 **密碼學技術**，可以用來保護你的 **秘密**（例如網路銀行、電子郵件、加密訊息等）。

現在，隨著 **量子計算機** 的發展，傳統的密碼技術（如 **RSA 和 ECC**）就像 **舊鑰匙**，很容易被破解。因此，我們需要 **新的鑰匙** 來確保未來的安全！🔐✨

---

## 🔑 2. 什麼是 SIDH？（已被破解 😢）

### 🛠️ **概念**

SIDH（超奇異橢圓曲線同源密鑰交換）曾被認為是一種 **量子安全的密鑰交換方法**，但它在 **2022 年被破解了**，所以現在大家轉向 **其他後量子密碼技術**。

### 💡 **如何運作？**

1. **Alice 和 Bob** 透過 **橢圓曲線** 來產生一個共享密鑰。
2. 透過 **同源映射（Isogeny）** 進行安全交換。
3. **理論上安全**，但後來發現數學漏洞，被破解了！😱

### ❌ **問題**

🔴 **計算成本高**  
🔴 **2022 年被數學家破解**（攻擊方法來自荷蘭萊頓大學）

所以，不再推薦使用 SIDH，改用更安全的技術，例如 **Kyber 和 Dilithium**

---

## 🔥 3. CRYSTALS-Kyber（安全密鑰交換技術）

### 🛠️ **概念**

Kyber 是一種 **基於格（Lattice-based）** 的密鑰交換機制，它不像 RSA 和 ECC 那樣容易被量子計算機破解。

### 💡 **如何運作？**

1. **Alice 和 Bob** 透過 **Kyber 產生一對密鑰**（公鑰 & 私鑰）。
2. Bob 用 Alice 的 **公鑰** 加密一個隨機密鑰並發送給 Alice。
3. Alice 用她的 **私鑰** 解密，兩人就能共享密鑰了！✨

### ✅ **優點**

🟢 **比 RSA、ECC 更安全**  
🟢 **密鑰長度短，適合 IoT、雲端安全**  
🟢 **目前是 NIST 標準之一**

### 🎨 **示意圖**

📷 ![Kyber 工作原理](https://upload.wikimedia.org/wikipedia/commons/3/36/Public_key_encryption.svg)

---

## 🖊 4. CRYSTALS-Dilithium（安全數位簽章）

### 🛠️ **概念**

Dilithium 是一種 **數位簽章演算法**，類似於 **你在合約上簽名**，用來保證訊息的真實性和完整性。

### 💡 **如何運作？**

1. Alice 產生 **公私鑰對**。
2. Alice **簽署文件**，生成數位簽章。
3. Bob **驗證簽章**，確保 Alice 真的發送了這份訊息。

### ✅ **優點**

🟢 **適用於電子合約、區塊鏈、身分驗證**  
🟢 **比 RSA、ECDSA 更安全**

### 🎨 **示意圖**

📷 ![數位簽章原理](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Digital_Signature_diagram.svg/800px-Digital_Signature_diagram.svg.png)

---

## 🎲 5. 模化學習帶誤差（MLWE）：量子計算機也不太能解！

### 🛠️ **概念**

MLWE 是 **Kyber 和 Dilithium 的數學基礎**，它是一種 **基於格（Lattice-based）** 的數學問題。

### 💡 **為什麼安全？**

1. 量子計算機擅長破解 **RSA、ECC**，但對 **MLWE 問題沒有什麼施力點**。
2. 即使是最強的量子演算法（Shor’s Algorithm）也無法高效解出 MLWE。

### ✅ **MLWE 的應用**

- **Kyber（密鑰交換）**
- **Dilithium（數位簽章）**
- **FrodoKEM（另一種後量子密碼技術）**

---

## 📌 6. 總結

| 技術          | 用途     | 替代       | 安全性             | 狀態        |
| ------------- | -------- | ---------- | ------------------ | ----------- |
| **SIDH**      | 密鑰交換 | RSA、ECC   | 2022 年被破解      | ❌ 不推薦   |
| **Kyber**     | 密鑰交換 | RSA、ECC   | 抗量子攻擊         | ✅ 推薦     |
| **Dilithium** | 數位簽章 | RSA、ECDSA | 抗量子攻擊         | ✅ 推薦     |
| **MLWE**      | 數學基礎 | -          | 量子計算機無法破解 | ✅ 核心技術 |

🔹 **目前最佳選擇是** **Kyber（密鑰交換）** 和 **Dilithium（數位簽章）**！  
🔹 **這些技術將保護我們在量子時代的網路安全！** 🔐🚀

---

## 🎉 7. 進一步學習

- 📖 [NIST PQC 官方網站](https://csrc.nist.gov/projects/post-quantum-cryptography)
- 📖 [Kyber 研究論文](https://eprint.iacr.org/2017/634)
- 📖 [Dilithium 研究論文](https://eprint.iacr.org/2017/633)

🔹 **未來的密碼技術由你來掌握！加油！🚀**

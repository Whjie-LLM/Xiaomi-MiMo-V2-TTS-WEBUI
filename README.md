# 🎙️ Xiaomi-MiMo-V2-TTS-WEBUI

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange.svg)](https://gradio.app/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

基于 Gradio 构建的 **Xiaomi MiMo V2-TTS** 语音合成 Web 界面。提供简洁直观的配置面板，支持多种音色、音频格式以及高级推理参数的实时调节。

---

## ✨ 功能特点

- **全模型兼容**：默认采用 `mimo-v2-tts` 语音优化模型，确保合成效果最佳。
- **多样化音色**：内置 `mimo_default` (默认)、`default_en` (英文)、`default_zh` (中文) 等多种音色。
- **多格式输出**：支持 `mp3`、`wav`、`pcm` 三种常用音频格式，适配不同播放场景。
- **精细参数调节**：
  - **Temperature (温度)**：调节输出的随机性，数值越高音调起伏越丰富。
  - **Top P (核采样)**：控制生成内容的多样性。
  - **Max Tokens**：设置单次合成的最大文本长度限制。
  - **Penalty (惩罚项)**：有效控制生成内容的重复度与话题多样性。
- **现代化 UI**：基于 Gradio 构建的响应式界面，支持实时状态反馈和音频预览。

---

## 📂 项目结构

```text
Xiaomi-MiMo-V2-TTS-WEBUI/
├── app.py                # Gradio WebUI 启动入口
├── Xiaomi_MiMo_V2_TTS.py # 核心 API 请求逻辑与配置
├── mimo_audio.py         # 音频 Base64 解析与转换工具
├── requirements.txt      # Python 依赖包清单
└── README.md             # 项目说明文档
```

---

## 🚀 快速开始

### 1. 准备环境

建议使用 Conda 创建独立虚拟环境：

```bash
# 创建环境 (可选)
conda create -n mimo python=3.10
conda activate mimo

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 API Key

打开 [Xiaomi_MiMo_V2_TTS.py](Xiaomi_MiMo_V2_TTS.py) 文件，将您的 API Key 填入以下位置：

```python
API_KEY = "您的_MIMO_API_KEY"
```

### 3. 启动应用

在终端执行：

```bash
python app.py
```

启动后访问本地链接（通常为 `http://127.0.0.1:7860`）即可开始使用。

---

## ⚙️ 参数详解

| 参数名                  | 默认值           | 说明                                       |
| :---------------------- | :--------------- | :----------------------------------------- |
| **音色 (Voice)**  | `mimo_default` | 语音的基础音质风格。                       |
| **格式 (Format)** | `mp3`          | 输出文件的编码格式。                       |
| **Temperature**   | `0.6`          | 采样温度，越高则语调起伏越大。             |
| **Top P**         | `0.95`         | 核采样概率阈值，控制生成文本的多样性。     |
| **Max Tokens**    | `8192`         | 允许合成的最大文本 token 数量。            |
| **Penalty**       | `0.0`          | 惩罚系数，用于减少内容重复或增加主题广度。 |

---

## 📜 免责声明

本工具仅作为 **Xiaomi MiMo API** 的可视化封装，音频合成质量及接口稳定性由服务提供商负责。请确保您的 API Key 安全，并遵守相关法律法规使用合成音频。

---

## 🤝 贡献与反馈

如果您有任何建议或发现了 Bug，欢迎提交 Issue 或 Pull Request！

#!/bin/bash

# 平行宇宙生成器后端启动脚本

echo "🚀 启动平行宇宙生成器后端服务..."

# 检查是否存在.env文件
if [ ! -f ".env" ]; then
    echo "⚠️  .env 文件不存在，从 .env.example 复制..."
    cp .env.example .env
    echo "📝 请编辑 .env 文件，填入你的 OpenAI API Key"
    echo "   export OPENAI_API_KEY=your_api_key_here"
    echo ""
fi

# 检查依赖
echo "📦 检查 Python 依赖..."
pip install -r requirements.txt

# 启动服务
echo "🌟 启动 FastAPI 服务 (端口 8000)..."
python main.py

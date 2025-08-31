#!/bin/bash

# 平行宇宙生成器项目启动脚本

echo "🌌 欢迎使用平行宇宙生成器！"
echo ""

# 检查并创建.env文件
if [ ! -f "backend/.env" ]; then
    echo "📝 创建后端环境配置文件..."
    cp backend/.env.example backend/.env
    echo "⚠️  请在 backend/.env 文件中设置你的 OpenAI API Key"
    echo ""
fi

echo "🚀 启动项目的两个服务："
echo ""
echo "1. 前端服务 (Next.js) - 端口 3000"
echo "2. 后端服务 (FastAPI) - 端口 8000"
echo ""

# 检查是否已有前端服务在运行
if pgrep -f "npm run dev" > /dev/null; then
    echo "✅ 前端服务已在运行 (http://localhost:3000)"
else
    echo "🔧 启动前端服务..."
    npm run dev &
    sleep 3
    echo "✅ 前端服务已启动 (http://localhost:3000)"
fi

echo ""
echo "🔧 启动后端服务..."
cd backend
python main.py &
echo "✅ 后端服务已启动 (http://localhost:8000)"
echo ""

echo "🎉 所有服务已启动完成！"
echo ""
echo "📱 打开浏览器访问: http://localhost:3000"
echo "📚 API 文档地址: http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服务"

# 等待用户中断
wait

# 平行宇宙生成器 (Parallel Universe Generator)

一个基于 AI/LLM 技术的全栈 Web 应用，让用户根据自己的人生选择生成"平行宇宙"故事。

## 🌟 功能特色

- **智能故事生成**: 使用 OpenAI GPT API 根据用户输入生成个性化的平行宇宙故事
- **美观的用户界面**: 基于 Next.js 和 Tailwind CSS 的现代化响应式设计
- **实时反馈**: 优雅的加载动画和状态管理
- **社交分享**: 便捷的故事分享功能
- **双重模式**: 支持个人人生探索和趣味性"故事新编"

## 🛠 技术栈

- **前端**: Next.js 14+ with TypeScript & Tailwind CSS
- **后端**: Python FastAPI
- **数据库**: MySQL
- **AI**: OpenAI GPT API
- **部署**: Vercel (前端) + Render (后端)

## 📁 项目结构

```
/
├── src/app/           # Next.js 前端页面和组件
├── backend/           # Python FastAPI 后端服务
├── .github/           # GitHub 相关配置
└── README.md          # 项目说明
```

## 🚀 快速开始

### 前端启动 (端口 3000)

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 后端启动 (端口 8000)

```bash
# 进入后端目录
cd backend

# 安装 Python 依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key

# 启动后端服务
python main.py
```

### 环境变量配置

在 `backend/.env` 文件中配置以下变量：

```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=mysql://username:password@localhost:3306/parallel_universe
CORS_ORIGINS=http://localhost:3000
```

## 🎯 使用方法

1. 访问 [http://localhost:3000](http://localhost:3000)
2. 填写表单：
   - 你现在的状况
   - 那个没有选择的道路
   - 如果当初选择了它会怎样
3. 点击"生成我的平行宇宙"
4. 等待 AI 生成你的专属故事
5. 分享你的平行宇宙故事！

## 💡 示例输入

**个人探索类**:
- 当前状况: "我是一名程序员"
- 没选择的: "当初没有学画画"
- 如果选择: "去了美术学院"

**趣味创作类**:
- 当前状况: "Ti8总决赛第五场的Ame"
- 没选择的: "没有选择稳健打法"
- 如果选择: "带队稳健拆基地"

## 🔧 开发指南

- 使用 TypeScript 编写所有前端代码
- 遵循 React 最佳实践和状态管理
- 使用 Tailwind CSS 确保响应式设计
- 优雅处理错误并提供用户反馈
- 保持 API 响应结构化和一致性

## 📈 未来规划

- [ ] 用户登录和历史记录
- [ ] AI 绘画集成
- [ ] 社区功能和故事画廊
- [ ] 高级订阅服务
- [ ] 移动端 App

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

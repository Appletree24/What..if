from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import openai
import json
import os
from dotenv import load_dotenv
from database import get_db, Story

# 加载环境变量
load_dotenv()

app = FastAPI(title="Parallel Universe Generator", version="1.0.0")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGINS", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI 客户端配置
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("⚠️  警告: 未设置 OPENAI_API_KEY 环境变量")
    print("   请在 .env 文件中设置: OPENAI_API_KEY=your_api_key_here")
    openai_api_key = "placeholder_key"

client = openai.OpenAI(api_key=openai_api_key)

# 请求模型
class StoryRequest(BaseModel):
    current_situation: str
    choice_not_taken: str
    alternative_choice: str

# 响应模型
class StoryResponse(BaseModel):
    story: dict
    success: bool
    message: str = ""

@app.get("/")
async def root():
    return {"message": "Parallel Universe Generator API is running!"}

@app.post("/generate-story", response_model=StoryResponse)
async def generate_story(request: StoryRequest, db: Session = Depends(get_db)):
    try:
        # 构建 prompt
        prompt = f"""
你是一个富有想象力的故事作家。请根据以下信息生成一个平行宇宙的故事。

# 背景信息
- 当前状况: {request.current_situation}
- 没有选择的道路: {request.choice_not_taken}
- 如果选择了: {request.alternative_choice}

# 故事要求
- 风格: 生动有趣，略带戏剧性
- 结构: 按时间线展示人生轨迹
- 语言: 中文
- 格式: 请严格按照JSON格式返回

请生成一个JSON对象，包含以下字段：
{{
  "title": "这个平行宇宙的标题",
  "timeline": {{
    "5年后": "一句话描述",
    "10年后": "一句话描述", 
    "15年后": "一句话描述"
  }},
  "turning_point": "一个关键转折点的描述",
  "reflection": "对这个平行人生的总结感悟"
}}
"""
        
        # 调用 OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个专业的故事创作者，擅长创作引人入胜的平行宇宙故事。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.8
        )
        
        # 解析响应
        story_content = response.choices[0].message.content
        
        # 尝试解析 JSON
        try:
            story_json = json.loads(story_content)
        except:
            # 如果解析失败，返回原始文本
            story_json = {
                "title": "你的平行宇宙",
                "content": story_content,
                "note": "故事格式需要调整"
            }
        
        # 保存到数据库
        db_story = Story(
            current_situation=request.current_situation,
            choice_not_taken=request.choice_not_taken,
            alternative_choice=request.alternative_choice,
            generated_story=json.dumps(story_json, ensure_ascii=False)
        )
        db.add(db_story)
        db.commit()
        db.refresh(db_story)
        
        return StoryResponse(
            story=story_json,
            success=True,
            message="故事生成成功！"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成故事时出错: {str(e)}")

@app.get("/stories/recent")
async def get_recent_stories(limit: int = 10, db: Session = Depends(get_db)):
    """获取最近生成的故事（不包含个人信息）"""
    try:
        stories = db.query(Story).order_by(Story.created_at.desc()).limit(limit).all()
        return {
            "stories": [
                {
                    "id": story.id,
                    "generated_story": json.loads(story.generated_story),
                    "created_at": story.created_at
                }
                for story in stories
            ],
            "total": len(stories)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取故事列表失败: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

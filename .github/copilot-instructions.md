<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Parallel Universe Generator

This is a full-stack web application that allows users to generate "parallel universe" stories based on their life choices using AI/LLM technology.

## Tech Stack
- Frontend: Next.js 14+ with TypeScript and Tailwind CSS
- Backend: Python FastAPI
- Database: MySQL
- AI: OpenAI GPT API for story generation

## Project Structure
- `/src/app/` - Next.js frontend pages and components
- `/backend/` - Python FastAPI backend service
- The frontend runs on port 3000, backend on port 8000

## Key Features
- User input form for current situation and alternative life choices
- LLM-powered story generation with structured output
- Beautiful UI with loading states and result display
- Social sharing functionality

## Development Guidelines
- Use TypeScript for all frontend code
- Follow React best practices with proper state management
- Ensure responsive design with Tailwind CSS
- Handle errors gracefully and provide user feedback
- Keep API responses structured and consistent

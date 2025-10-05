# Test Project 1 - Dev Wizard Test Monorepo

This is a test monorepo for validating Dev Wizard functionality. It contains three applications demonstrating different frameworks and use cases.

## Applications

### 1. Frontend (TypeScript/React)
**Location**: `apps/frontend`  
**Framework**: Vite + React + TypeScript  
**Port**: 5173  
**Purpose**: Simple frontend that displays data from the API server

**Features**:
- Fetches weather data from API server
- Displays in a simple UI
- Hot module reloading

**Commands**:
```bash
cd apps/frontend
npm install
npm run dev
```

### 2. API Server (Python/FastAPI)
**Location**: `apps/api-server`  
**Framework**: FastAPI + uvicorn  
**Port**: 8000  
**Purpose**: API server that fetches data from public APIs and processes it

**Features**:
- Calls OpenWeatherMap API (or mock data)
- Processes and transforms data
- Returns JSON responses
- CORS enabled for frontend

**Commands**:
```bash
cd apps/api-server
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. LangGraph Agent (Python/LangGraph)
**Location**: `apps/langgraph-agent`  
**Framework**: LangGraph  
**Port**: 2028  
**Purpose**: Simple conversational agent using LangGraph

**Features**:
- Echo/chat agent
- Stateful conversation
- LangGraph runtime

**Commands**:
```bash
cd apps/langgraph-agent
uv venv
uv sync
uv run langgraph dev --no-browser --port 2028
```

## Quick Start

**Install Dependencies**:
```bash
# Frontend
cd apps/frontend
npm install

# API Server
cd ../api-server
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# LangGraph Agent
cd ../langgraph-agent
uv venv
uv sync
```

**Start All Services** (use separate terminals):
```bash
# Terminal 1: Frontend
cd apps/frontend
npm run dev

# Terminal 2: API Server
cd apps/api-server
.venv\Scripts\activate
uvicorn main:app --reload --port 8000

# Terminal 3: LangGraph Agent
cd apps/langgraph-agent
uv run langgraph dev --no-browser --port 2028
```

## Environment Variables

Each app has a `.env.example` file. Copy to `.env` and fill in values:

```bash
# Frontend
cp apps/frontend/.env.example apps/frontend/.env

# API Server
cp apps/api-server/.env.example apps/api-server/.env

# LangGraph Agent
cp apps/langgraph-agent/.env.example apps/langgraph-agent/.env
```

## Architecture

```
Test_Project_1/
├── apps/
│   ├── frontend/          # Vite + React
│   ├── api-server/        # FastAPI
│   └── langgraph-agent/   # LangGraph
├── logs/                  # Service logs
└── README.md
```

## Testing with Dev Wizard

This project is designed to test all Dev Wizard features:
- ✅ Project detection and listing
- ✅ Multiple service management
- ✅ Different frameworks (TypeScript, Python, LangGraph)
- ✅ Environment variable management
- ✅ Git operations
- ✅ Task execution (build, dev, test)
- ✅ Log retrieval
- ✅ Resource metrics

## License

MIT - Test project for Dev Wizard

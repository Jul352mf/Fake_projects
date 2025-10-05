# Test Project 1 - Quick Reference

**Location**: `C:\Users\julia\workspace\Fake_projects\test_project_1`  
**Status**: ✅ Complete (24 files, 1,150 lines)  
**Repository**: https://github.com/Jul352mf/Fake_projects

## Quick Start

### Start All Services

**Terminal 1 - API Server**:
```bash
cd C:\Users\julia\workspace\Test_Project_1\apps\api-server
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python main.py
# → http://localhost:8000
```

**Terminal 2 - Frontend**:
```bash
cd C:\Users\julia\workspace\Test_Project_1\apps\frontend
npm install
npm run dev
# → http://localhost:5173
```

**Terminal 3 - LangGraph Agent**:
```bash
cd C:\Users\julia\workspace\Test_Project_1\apps\langgraph-agent
uv venv && .venv\Scripts\activate
uv sync
uv run langgraph dev --no-browser --port 2028
# → http://localhost:2028
```

## Architecture

```
Test_Project_1/
├── apps/
│   ├── frontend/       # React + TypeScript + Vite (5173)
│   ├── api-server/     # FastAPI + Python (8000)
│   └── langgraph-agent/# LangGraph + Python (2028)
└── logs/               # Service logs
```

## Dev Wizard Integration

### Add to Database
```powershell
# Add project to Dev Wizard
$body = @{
  tool = "createProject"
  arguments = @{
    templateId = "monorepo-multi-framework"
    projectName = "Test_Project_1"
    path = "C:\Users\julia\workspace\Test_Project_1"
    initGit = $false
  }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3002/tools/call/createProject" `
  -Method POST -ContentType "application/json" -Body $body
```

### Test MCP Tools
```powershell
# Get project status
$body = @{ 
  tool = "getProjectStatus"
  arguments = @{ projectId = 1 }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3002/tools/call/getProjectStatus" `
  -Method POST -ContentType "application/json" -Body $body

# Git status
$body = @{ 
  tool = "gitStatus"
  arguments = @{ projectId = 1 }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3002/tools/call/gitStatus" `
  -Method POST -ContentType "application/json" -Body $body

# Get environment variables
$body = @{ 
  tool = "getEnvVars"
  arguments = @{ projectId = 1; masked = $true }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3002/tools/call/getEnvVars" `
  -Method POST -ContentType "application/json" -Body $body

# Get metrics
$body = @{ 
  tool = "getMetrics"
  arguments = @{ projectId = 1 }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3002/tools/call/getMetrics" `
  -Method POST -ContentType "application/json" -Body $body
```

## Features Tested

- ✅ Multi-framework support (TypeScript + Python)
- ✅ Service management (run/stop)
- ✅ Git operations (status/commit/push/pull)
- ✅ Environment variables (getEnvVars/setEnvVar)
- ✅ Log management (getLogs)
- ✅ Metrics collection (getMetrics)
- ✅ Actions engine (executeAction)
- ✅ Health monitoring

## Documentation

Full documentation: `C:\Users\julia\workspace\Test_Project_1\PROJECT_SUMMARY.md`

- Project overview
- Complete file inventory
- Setup instructions
- Dev Wizard integration guide
- Testing checklist
- API documentation

## Statistics

| Metric | Value |
|--------|-------|
| Total Files | 24 |
| Total Lines | 1,150 |
| Frameworks | 3 (React, FastAPI, LangGraph) |
| Services | 3 (Frontend, API, Agent) |
| Ports | 3 (5173, 8000, 2028) |
| Git Commits | 1 (initial) |

## Next Steps

1. Add project to Dev Wizard database
2. Run full MCP tool test suite
3. Verify all 18 handlers work correctly
4. Performance testing (concurrent services)
5. Error handling validation

---

**Created**: 2024-01-15  
**Purpose**: Dev Wizard validation testing  
**Status**: Ready for integration testing

# Test Project 1 - LangGraph Agent

Simple LangGraph echo agent that demonstrates basic agent architecture without requiring LLM API keys.

## Features

- 🤖 Simple echo agent with command handling
- 📊 State management with LangGraph
- 🔄 Message history tracking
- ⚡ No LLM API key required (great for testing)
- 🧪 Built-in test cases

## Setup

1. **Install uv** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Create virtual environment and install dependencies**:
   ```bash
   uv venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   uv sync
   ```

3. **Configure environment** (optional):
   ```bash
   cp .env.example .env
   # Edit .env if you want to enable LangSmith tracing
   ```

## Running the Agent

### Local Testing (Python script)
```bash
uv run python src/agent.py
```

This will run the agent locally and test it with sample messages.

### LangGraph Dev Server
```bash
uv run langgraph dev --no-browser --port 2028
```

This starts the LangGraph development server with API endpoints.

## Agent Commands

The agent recognizes these commands:
- `hello` - Friendly greeting
- `help` - Show help message
- `status` - Show agent status and message count
- `bye` / `goodbye` - Farewell message
- Any other message - Echo back with message number

## API Endpoints (when running dev server)

Once the LangGraph dev server is running:

- **Studio UI**: http://localhost:2028/studio
- **API Docs**: http://localhost:2028/docs
- **Health Check**: http://localhost:2028/health

### Example API Call

```bash
curl -X POST http://localhost:2028/runs/stream \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "echo_agent",
    "input": {
      "messages": [{"role": "user", "content": "Hello!"}]
    }
  }'
```

## Testing

Run the local test script:
```bash
uv run python src/agent.py
```

Expected output:
```
🚀 Test Project 1 - Echo Agent
==================================================

Testing the agent locally...

👤 User: Hello!
🤖 Agent: 👋 Hello! Nice to meet you! (Message #1)
   Timestamp: 2024-01-15T10:30:00.123456
   Message Count: 1

👤 User: help
🤖 Agent: ℹ️ I'm a simple echo agent. I repeat what you say! Try: hello, status, or any message. (Message #2)
   ...
```

## Architecture

```
langgraph-agent/
├── src/
│   └── agent.py          # Main agent implementation
├── pyproject.toml        # Python dependencies
├── langgraph.json        # LangGraph configuration
└── .env                  # Environment variables
```

### Graph Structure

```
START → greeting → echo → END
```

- **greeting**: Initial welcome message
- **echo**: Process user input and generate response

### State Schema

```python
{
  "messages": List[dict],      # Message history
  "timestamp": str,             # ISO timestamp
  "message_count": int          # Number of messages processed
}
```

## Development

### Adding New Commands

Edit `src/agent.py` and add new conditions in the `echo_node` function:

```python
elif "custom" in user_content.lower():
    response = f"Custom command response! (Message #{message_count})"
```

### Adding LLM Integration

To add real LLM functionality:

1. Install LLM package: `uv add langchain-openai` or `uv add langchain-anthropic`
2. Add API key to `.env`: `OPENAI_API_KEY=your_key`
3. Modify `echo_node` to call LLM instead of simple echo

## Troubleshooting

**Error: "No module named 'langgraph'"**
- Run `uv sync` to install dependencies

**Error: "Port 2028 already in use"**
- Change port: `langgraph dev --port 2029`
- Or kill existing process on port 2028

**LangSmith tracing not working**
- Set `LANGCHAIN_TRACING_V2=true` in `.env`
- Add valid `LANGCHAIN_API_KEY`

## Integration with Dev Wizard

This agent can be managed by Dev Wizard:

1. Add project to Dev Wizard database
2. Use `runProject` tool to start the agent
3. Use `stopServer` tool to stop the agent
4. Use `getLogs` tool to view agent logs
5. Use `getMetrics` tool to monitor performance

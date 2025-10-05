# Test Project 1 - API Server

Python FastAPI server that fetches weather data from OpenWeatherMap API, processes it, and serves it to the frontend.

## Features

- 🌤️ Weather data from OpenWeatherMap API
- 🔄 Data processing (temperature conversion, formatting)
- 🚀 FastAPI with automatic docs
- 🔒 CORS configured for local development
- 🎭 Mock data mode when no API key configured

## Setup

1. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenWeatherMap API key (optional - mock data works without it)
   ```

4. **Run server**:
   ```bash
   python main.py
   # Or with uvicorn directly:
   uvicorn main:app --reload --port 8000
   ```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health status
- `GET /weather?city=London` - Get weather for a city
- `GET /weather/multiple?cities=London,Paris,Tokyo` - Get weather for multiple cities

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

```bash
# Test health check
curl http://localhost:8000/health

# Test weather endpoint
curl http://localhost:8000/weather?city=London

# Test multiple cities
curl "http://localhost:8000/weather/multiple?cities=London,Paris,Tokyo"
```

## Mock Data Mode

If no OpenWeatherMap API key is configured, the server will return mock data for testing purposes. This allows you to test the entire stack without an API key.

To get a free API key:
1. Visit https://openweathermap.org/api
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

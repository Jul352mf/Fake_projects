from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Test Project 1 - API Server")

# CORS configuration for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "demo")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "London")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Test Project 1 API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "api_key_configured": bool(OPENWEATHER_API_KEY and OPENWEATHER_API_KEY != "demo"),
        "endpoints": {
            "weather": "/weather",
            "health": "/health"
        }
    }

@app.get("/weather")
async def get_weather(city: str = None):
    """
    Fetch current weather data from OpenWeatherMap API and process it
    
    Query params:
    - city: City name (default: London)
    
    Returns processed weather data with temperature in Celsius
    """
    city = city or DEFAULT_CITY
    
    # Check if API key is configured
    if not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "demo":
        # Return mock data for testing when no API key
        return {
            "city": city,
            "temperature": 20.5,
            "description": "partly cloudy (mock data)",
            "humidity": 65,
            "timestamp": datetime.now().isoformat(),
            "note": "Using mock data - configure OPENWEATHER_API_KEY for real data"
        }
    
    try:
        # Call OpenWeatherMap API
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"  # Get temperature in Celsius
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Process the data (extracting and formatting)
        processed_data = {
            "city": data["name"],
            "temperature": round(data["main"]["temp"], 1),
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "timestamp": datetime.now().isoformat(),
            "raw_temp_kelvin": data["main"]["temp"] + 273.15  # Add some processing
        }
        
        return processed_data
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Failed to fetch weather data: {str(e)}"
        )
    except KeyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process weather data: {str(e)}"
        )

@app.get("/weather/multiple")
async def get_multiple_weather(cities: str):
    """
    Fetch weather for multiple cities (comma-separated)
    
    Query params:
    - cities: Comma-separated city names (e.g., "London,Paris,Tokyo")
    
    Returns list of weather data for each city
    """
    city_list = [city.strip() for city in cities.split(",")]
    results = []
    
    for city in city_list:
        try:
            weather = await get_weather(city)
            results.append(weather)
        except HTTPException:
            results.append({
                "city": city,
                "error": "Failed to fetch data"
            })
    
    return {
        "count": len(results),
        "cities": results,
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

import { useState, useEffect } from 'react'
import './App.css'

interface WeatherData {
  city: string
  temperature: number
  description: string
  humidity: number
  timestamp: string
}

function App() {
  const [weather, setWeather] = useState<WeatherData | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchWeather = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch('/api/weather')
      if (!response.ok) {
        throw new Error('Failed to fetch weather data')
      }
      const data = await response.json()
      setWeather(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchWeather()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>🌤️ Test Project 1 - Weather Dashboard</h1>
        <p className="subtitle">Dev Wizard Test Frontend</p>
      </header>

      <main className="content">
        {loading && <div className="loading">Loading weather data...</div>}
        
        {error && (
          <div className="error">
            <p>❌ Error: {error}</p>
            <p className="hint">Make sure the API server is running on port 8000</p>
          </div>
        )}

        {weather && !loading && (
          <div className="weather-card">
            <h2>{weather.city}</h2>
            <div className="temperature">{weather.temperature}°C</div>
            <div className="description">{weather.description}</div>
            <div className="details">
              <p>💧 Humidity: {weather.humidity}%</p>
              <p>🕐 Updated: {new Date(weather.timestamp).toLocaleTimeString()}</p>
            </div>
          </div>
        )}

        <button onClick={fetchWeather} disabled={loading} className="refresh-btn">
          🔄 Refresh Weather
        </button>

        <div className="info-box">
          <h3>🧪 Dev Wizard Test Features</h3>
          <ul>
            <li>✅ TypeScript + React + Vite</li>
            <li>✅ API proxy to Python backend</li>
            <li>✅ Hot module reloading</li>
            <li>✅ Environment variables</li>
            <li>✅ Build and dev scripts</li>
          </ul>
        </div>
      </main>
    </div>
  )
}

export default App

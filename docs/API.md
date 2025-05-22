### **API.md**
```markdown
# API Documentation

## Endpoints
- `GET /api/current` - Latest sensor readings
- `GET /api/history?hours=24` - Historical data (default 24 hours)

## Response Format
```json
{
  "temperature": 25.3,
  "humidity": 45.2,
  "air_quality": 412.5,
  "timestamp": "2023-06-15T14:30:00"
}

This implementation provides a complete, production-ready IoT monitoring system with proper error handling, database persistence, and REST API access. The code follows best practices for both Arduino and Python development.

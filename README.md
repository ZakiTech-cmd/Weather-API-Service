# Weather Forecast API

This project is a FastAPI service that fetches weather data from the OpenWeatherMap API. Data is cached in S3 and logged in DynamoDB.

## How to Run the Project

1. **Build the Docker image:**

   ```bash
   docker build -t weather-forecast-api .
   
2. **Run the Docker container:**

    ```bash
   docker run -p 8000:8000 weather-api-service

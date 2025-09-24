### Project Structure

```
fastapi_model/
│
├── app/
│   ├── main.py
│   ├── model.py
│   └── requirements.txt
│
└── README.md
```

### 1. `main.py`

This file contains the FastAPI application and the `/predict` endpoint.

```python
# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import DummyModel

app = FastAPI()
model = DummyModel()

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    probability: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    prediction, probability = model.predict(request.text)
    return PredictionResponse(prediction=prediction, probability=probability)
```

### 2. `model.py`

This file contains a dummy model for demonstration purposes. You can replace this with your actual model.

```python
# app/model.py
import random

class DummyModel:
    def predict(self, text: str):
        # Dummy prediction logic
        prediction = "positive" if random.random() > 0.5 else "negative"
        probability = random.uniform(0.5, 1.0)
        return prediction, probability
```

### 3. `requirements.txt`

This file lists the dependencies required for the project.

```
fastapi
uvicorn
```

### 4. `README.md`

This file provides instructions for setting up and running the project locally.

```markdown
# FastAPI Model Prediction

This is a simple FastAPI project that wraps a machine learning model and provides a `/predict` endpoint.

## Requirements

- Python 3.7 or higher
- pip

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastapi_model
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r app/requirements.txt
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Testing the Endpoint

You can test the `/predict` endpoint using `curl` or any API client like Postman. Here’s an example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text": "Your input text here"}'
```

## Docker Setup

To run the application using Docker, you can use the following `Dockerfile`.

### Dockerfile

```dockerfile
# Dockerfile
FROM python:3.9

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and Run Docker Container

1. Build the Docker image:

   ```bash
   docker build -t fastapi-model .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 fastapi-model
   ```

The application will be available at `http://127.0.0.1:8000`.
```

### Conclusion

This setup provides a basic FastAPI application with a prediction endpoint. You can replace the `DummyModel` with your actual model logic. The README includes instructions for local setup and Docker usage.
# FastAPI-app

## Instructions For Use
1. Install the necessarry requirements
```
pip install -r requirements.txt
```

2. Run Server
```
uvicorn app.main:app --reload
```

3. Usage
Navigate to `http://127.0.0.1:8000/repositories/{username}` in your browser or send a GET request using tools Thunder Client, replacing `{username}` with the GitHub username for which you want to fetch repositories.

4. Testing
run
```
pytest tests
```
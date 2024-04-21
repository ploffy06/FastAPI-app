# FastAPI-app
A simple FastAPI application that uses the GitHub API to fetch and display the public repositories  of a given  user. For each repository, it shows the name, description, language
and number of stars.

## Instructions For Use
1. Installing requirements

    To install the necessary python libraries, run the following in the  root  directory.
```
pip install -r requirements.txt
```

2. Run Server
```
uvicorn app.main:app --reload
```

3. Usage

    Navigate to `http://127.0.0.1:8000/repositories/{username}` in your browser or send a GET request using tools such as Thunder Client, replacing `{username}` with a GitHub username.

4. Testing

    run the following
```
pytest tests
```
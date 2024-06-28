# Setup Virtual Environment

```python
conda create -n fastapi-env python=3.10
conda activate fastapi-env
pip install -r requirements.txt
```

# Running the server

- Syntax: uvicorn <name_of_python_file>:<instance_of_fastapi_object> --reload which allows server to restart automatically whenever there is a change to the main.py file
- Uvicorn is an ASGI web server implementation for Python

- Command to run:
`uvicorn main:app --reload`
# `uvicorn main:my_first_api --reload`

The command `uvicorn main:app` refers to:
- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only use for development.


# Automatic documentation of APIs:
- If the FastAPI app is running on port 8000, the docs can be found at: <uri_to_fastapi_app>/docs 
  - e.g., http://localhost:8000/docs if runnng on http://localhost:8000
- alternatively, the API documentation can also be found at http://localhost:8000/redoc


```json
Yes

```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Gender": 0,
  "Married": 0,
  "Dependents": 0,
  "Education": 0,
  "Self_Employed": 0,
  "LoanAmount": 0,
  "Loan_Amount_Term": 0,
  "Credit_History": 0,
  "Property_Area": 0,
  "TotalIncome": 0
}'

```
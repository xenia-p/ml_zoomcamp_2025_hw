import requests

url = 'http://localhost:9696/predict'

customer = {
  "gender": "male",
  "seniorcitizen": 1,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  #"test": 17,
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}

response = requests.post(url, json=customer)

predictions = response.json()
print(predictions)

if predictions['churn']:
    print('send email')
else:
    print('do nothing')
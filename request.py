import requests 
url = 'http://localhost:5000/results'
r = requests.post(url,json={"sepal_lenght":2, "sepal_width":3, "petal_lenght":2, "petal_width":2})  
print(r.json())
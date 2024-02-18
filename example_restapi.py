import requests


# response = requests.delete("http://localhost:8080/items/1")


response = requests.delete("http://127.0.0.1:8080/items/1")
print(response.status_code)

response = requests.get("http://127.0.0.1:8080/items")
actaul = len(response.json())
expected = 2
assert expected == actaul
print(response.json())
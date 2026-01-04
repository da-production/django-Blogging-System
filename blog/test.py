# login
login_to_api(username="alice", password="secret123")

# appel API plus tard
result = call_api(username="alice", endpoint="https://api.example.com/data", payload={"param": 42})
print(result)

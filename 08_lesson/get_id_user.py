import requests


url = "https://yougile.com/api-v2/users"

headers = {
    "Authorization": "Bearer UxgVkTfB+YG3ZFyP76qe8vlIB3xaVByz37CUhcc+pRF5VEqwWOKuQHBPVMlB2pPM",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

users_data = response.json()
print("Инфо о сотрудниках: ", users_data)

users = users_data.get('content', [])

print("Список сотрудников: ")
for user in users:
    print(f"ID: {user['id']}, Имя: {user.get('realName')}")

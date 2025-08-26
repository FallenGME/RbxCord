import requests
import json

# Replace this with your actual Vercel endpoint + webhook path
url = "https://rbx-cord-git-main-fallengmes-projects.vercel.app/api/webhooks/1409999742166892606/FNgOnow0HqTTigM-tM9Vrt-BG1sz_pgtWRKqoT712_dQc8ERHH4DZAsC4bcTM7IThOTJ"
# Example data to send
payload = {
    "content": "Hello from Python test script!",
    "username": "TestBot"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)

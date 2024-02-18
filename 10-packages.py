'''

# import package to use datetime

pip - package manager


'''

from datetime import datetime
import requests

print(datetime.now())

urls = ["https://github.com",
        "https://google.com",
        "https://linkedin.com"]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print("github is up")

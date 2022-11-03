import requests
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("--page", help="Pagination Index")


args=parser.parse_args()

# response = requests.get('https://api.github.com/repos/Diulia/webscraping-python/pulls?state=open')
# print('Page content:',json.dumps(response.json(), indent=2))

response = requests.get('https:/api.github.com/repos/OWNER/REPO/pulls')
for pr in response.json(): 
    print(pr['title'], pr['html_url'])



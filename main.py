import requests
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("--page",default=1, help="Pagination Index")
parser.add_argument("--per_page", default=10, help="PRs per page")
parser.add_argument("--project_path", help="github project path e. g: <owner>/<repo>")


args=parser.parse_args()

if ( args.project_path == None):
    print("owner/repo required")
else: 
    response = requests.get(f"https://api.github.com/repos/{args.project_path}/pulls?page={args.page}&per_page={args.per_page}&state=open")
# response = requests.get('https:/api.github.com/repos/{OWNER}/{REPO}/pulls?state=open')
    for pr in response.json(): 
        print(pr['title'], pr['html_url'], "\n")



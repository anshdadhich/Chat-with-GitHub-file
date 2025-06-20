import requests
import base64

def get_repos(username):
  
    repos = []

    url = f"https://api.github.com/users/{username}/repos"
    
    response = requests.get(url)
    data = response.json()
        
    for repo in data:
        repos.append(repo["name"])
        
    return repos


def get_file(username,repository,file_name):
    
    url = f"https://api.github.com/repos/{username}/{repository}/contents/{file_name}"

    response = requests.get(url)
    print(response)
    data = response.json()
        
    file_content = base64.b64decode(data["content"]).decode("utf-8")
    
    return file_content


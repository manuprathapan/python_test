import json
import requests
from datetime import datetime

def display_repo_details():

    git_api = 'https://api.github.com/repos/' + 'manuprathapan/odoo'
    print(git_api)
    repo_response = requests.get(git_api.strip())
    commit_response = requests.get((git_api+'manuprathapan/odoo'+'/commits').strip())

    print(repo_response.headers)
    print(commit_response.content)
    if repo_response.status_code != 200 and commit_response.status_code != 200:
        print('Unable to connect to repository or Invalid repository')
    else:
        responseItem = json.loads(repo_response.content)
        c_responseItem = json.loads(commit_response.content)
        convert_date = datetime.strptime(c_responseItem[0]['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ') \
            .strftime('%d-%b-%Y')

        print('Repository Name: %s' % responseItem['name'])
        print('Clone URL: %s' % responseItem['clone_url'])
        print('Latest Commit Date: %s' % convert_date)
        print('Name of the latest author: %s' % c_responseItem[0]['commit']['author']['name'])


display_repo_details()
import requests
from github import Github
from tabulate import tabulate
from .utils import clearScreen,richPrint
from .html_g import htmlMaker
git = Github()

def userExists(username):
    addr = "https://api.github.com/users/" + str(username)
    response = requests.get(addr)
    if response.status_code == 404:
        richPrint("[bold red]Username Not Found![/bold red]")
        return False
    if  response.status_code == 403:
        richPrint("[bold red]Api Usage Rate Limit![/bold red]")
        return False
    if response.status_code == 200 or response.status_code == 304:
        return True

def getUser(username,theme):
    try:
        user = git.get_user(username)
        return printRepos(user.get_repos(),username,theme)
    except:
        richPrint("[bold red]We have some problems in the connection :)[/bold red]")
def printRepos(repos,username,theme):
    original_repos = []
    original_repos_name = []
    for repo in repos:
        if repo.fork is False and repo.archived is False:
            if username + ".git" in str(repo.clone_url):
                next
            else:
                original_repos.append(repo.clone_url)
                repo_name = str(repo.clone_url.split('/')[-1].split('.git')[0])
                original_repos_name.append(repo_name)
    table = [list(a) for a in zip(original_repos_name,original_repos)]
    clearScreen()
    print(f'\n{tabulate(table,headers=["Name","Repo Url"],tablefmt="grid")}\n')
    richPrint("[bold green]Generating Front Template[/bold green]\n")
    themes = {
        "first":"first/"
        # Create new templates in templates dir
    }
    htmlMaker(username,table,themes[theme],theme)
import requests
from github import Github
from tabulate import tabulate
from src.utils import clear_screen, rich_print
from src.html_g import html_maker
import yaml

github = Github()

def user_exists(username):
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)

    if response.status_code == 404:
        rich_print("[bold red]Username Not Found![/bold red]")
        return False
    if response.status_code == 403:
        rich_print("[bold red]API Usage Rate Limit![/bold red]")
        return False
    if response.ok:
        return True

def get_user(username, theme):
    try:
        user = github.get_user(username)
        themes = load_themes()
        theme_path = get_theme_path(theme, themes)
        return print_repos(user.get_repos(), username, theme_path, theme)
    except requests.exceptions.RequestException:
        rich_print("[bold red]We have some problems in the connection :)[/bold red]")

def print_repos(repos, username, theme_path, theme):
    original_repos = []
    original_repos_name = []

    for repo in repos:
        if not repo.fork and not repo.archived:
            if f"{username}.git" in str(repo.clone_url):
                continue
            original_repos.append(repo.clone_url)
            repo_name = str(repo.clone_url.split('/')[-1].split('.git')[0])
            original_repos_name.append(repo_name)

    table = [list(a) for a in zip(original_repos_name, original_repos)]
    clear_screen()
    print(f'\n{tabulate(table, headers=["Name", "Repo Url"], tablefmt="grid")}\n')
    rich_print("[bold green]Generating Front Template[/bold green]\n")

    html_maker(username, table, theme_path, theme)


def load_themes():
    with open("src/themes.yaml") as file:
        themes_data = yaml.safe_load(file)
    return themes_data.get("themes", [])


def get_theme_path(theme, themes):
    for t in themes:
        if t.get("name") == theme:
            return t.get("path", "")
    return ""

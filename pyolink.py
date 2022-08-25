import click
from src.github import getUser, userExists

@click.command()
@click.option('--username',default="DanielcoderX",help='Github USERNAME (default uses DanielcoderX)')
@click.option('--theme',default="first",help='Template NAME to use: first - second(not yet created)... (default uses first)')
def main(username,theme):
    """pyolink is a simple front page generator from github repositories"""
    if  userExists(username):
        getUser(username,theme)


if __name__ == "__main__":
    main()

import click
from src.github import get_user, user_exists


@click.command()
@click.option('--username', default="DanielcoderX", help='GitHub username (default: DanielcoderX)')
@click.option('--theme', default="first", help='Template name to use: first (default) or second (not yet created)')
def main(username: str, theme: str) -> None:
    """Pyolink is a simple front page generator from GitHub repositories"""
    if user_exists(username):
        get_user(username, theme)


if __name__ == "__main__":
    main()

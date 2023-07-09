import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from shutil import copy2
from src.utils import rich_print, root_project

root = Path(root_project())
output_dir = root / "build"
templates_location = root / "templates"
environment = Environment(loader=FileSystemLoader(str(templates_location)))


def html_maker(username, repos, which_template, template_name):
    template = environment.get_template(os.path.join(which_template, template_name + ".html"))
    rich_print("[bold blue]Starting Generation[/bold blue]")

    try:
        os.makedirs(str(output_dir), exist_ok=True)

        for path in os.listdir(str(templates_location / which_template)):
            if not path.endswith(".html"):
                copy2(str(templates_location / which_template / path), str(output_dir))

        html_file_path = output_dir / f"{username}.html"

        if html_file_path.is_file():
            html_file_path.unlink()

        content = template.render(title=username, links=repos)

        with open(str(html_file_path), "w") as html_file:
            html_file.write(content)

        rich_print(f"\n[bold green]Generating Front Template Finished Successfully => {html_file_path}[/bold green]")

    except FileNotFoundError:
        rich_print("[bold red]File not found[/bold red]")

    except IsADirectoryError:
        rich_print("[bold red]Directory operation not permitted[/bold red]")

    except Exception as e:
        rich_print("[bold red]An error occurred[/bold red]")
        print(e)

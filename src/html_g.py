from .utils import richPrint,rootProject
from os import makedirs,remove,listdir,path as osPath
from jinja2 import Environment, FileSystemLoader
from shutil import copy2

root = rootProject().replace("\\","/") 
outputDir = root + "/build/" 
templatesLocation = root + "/templates/"
environment = Environment(loader=FileSystemLoader(templatesLocation))

def htmlMaker(username,repos,which_template,template_name):
    template = environment.get_template(which_template+template_name+".html")
    richPrint(f"[bold blue]Starting Generation[/bold blue]")
    try:
        try:
            makedirs(outputDir)
            for path in listdir(templatesLocation+which_template):
                if ".html" in path:
                    pass
                else:
                    copy2(templatesLocation+which_template+path,outputDir.rstrip('/'))
        except:
            pass
        if osPath.isfile(str(outputDir+username+".html")):
            remove(str(outputDir+username+".html"))
        content = template.render(title=username,links=repos)
        htmlFile = open(f"{outputDir}{username}.html","x")
        htmlFile.write(content)
        htmlFile.close()
        richPrint(f"\n[bold green]Generating Front Template Finished Successfully => {outputDir}{username}.html[/bold green]")
    except:
        richPrint("[bold red]There is a Problem[/bold red]")

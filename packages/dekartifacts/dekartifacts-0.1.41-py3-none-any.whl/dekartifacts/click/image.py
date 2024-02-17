import json
import typer
from dektools.file import read_text
from ..allinone.docker import DockerAllInOne
from ..artifacts.docker import DockerArtifact

app = typer.Typer(add_completion=False)


@app.command()
def exports(entries, path):
    for entry in json.loads(read_text(entries)):
        DockerAllInOne(entry['allinone']).exports(entry['images'], path)


@app.command()
def imports(path):
    DockerArtifact.imports(path)


@app.command()
def pulls(entries):
    for entry in json.loads(read_text(entries)):
        DockerAllInOne(entry['allinone']).pulls(entry['images'])


@app.command()
def migrate(path, images, registry):
    DockerArtifact.imports(path)
    for image in json.loads(read_text(images)):
        image_new = f"{registry}/{image.split('/', 1)[-1]}"
        DockerArtifact.tag(image, image_new)
        DockerArtifact.push(image_new)
        DockerArtifact.remove(image)

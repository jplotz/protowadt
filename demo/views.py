from django.http import HttpResponse

# See https://gabrieldemarmiesse.github.io/python-on-whales/
from python_on_whales import DockerClient

# Assume that DVWA is installed according to these instructions
# https://github.com/digininja/DVWA?tab=readme-ov-file#docker
# in a directory named DVWA which is in the parent directory of
# this repository.
docker = DockerClient(compose_files=["../DVWA/compose.yml"])


def index(request):
    return HttpResponse("Demo index page")


def start(request):
    docker.compose.up(detach=True)
    return HttpResponse("Containers started")


def restart(request):
    docker.compose.restart()
    return HttpResponse("Containers restarted")


def stop(request):
    docker.compose.stop()
    return HttpResponse("Containers stopped")


def down(request):
    # see https://stackoverflow.com/a/54219039
    # for the difference between "stop" and "down"
    docker.compose.down()
    return HttpResponse("Containers down")


def logs(request):
    return HttpResponse(docker.compose.logs())

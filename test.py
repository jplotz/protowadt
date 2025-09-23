#!/usr/bin/env python3
# See https://gabrieldemarmiesse.github.io/python-on-whales/

from python_on_whales import DockerClient
from time import sleep

# Assume that DVWA is installed according to these instructions
# https://github.com/digininja/DVWA?tab=readme-ov-file#docker
# in a directory named DVWA which is in the parent directory of
# this repository.
docker = DockerClient(compose_files=["../DVWA/compose.yml"])

# start up a group of containers
docker.compose.up(detach=True)

# show logs
print(docker.compose.logs(follow=False, stream=False))

print("waiting for a few seconds")
sleep(10)

# restart the containers
docker.compose.restart()

# show logs again after restart
print(docker.compose.logs(since="10s", follow=False, stream=False))

# stop the containers
docker.compose.stop()

print("all containers stopped")

# "down" the containers
# see https://stackoverflow.com/a/54219039
# for the difference between "stop" and "down"
# docker.compose.down()

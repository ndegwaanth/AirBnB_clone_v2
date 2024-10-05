#!/usr/bin/python3
""" generates a .tgz archive from the contents of web_static"""
from datetime import datetime
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ["100.25.21.172", "52.87.232.176"]


def do_pack():
    """creates a tar file"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        time = time.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -czvf {} web_static/".format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    """deployer method"""
    if not os.path.isfile(archive_path):
        return False
    # get file incase /path/to/file is passed
    archive = archive_path.split("/")[-1]
    # given in requirement
    destination = "/data/web_static/releases/{}".format(archive.split(".")[0])
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(destination))
    # unzip to /data/web_static/releases/<archive filename without extension>
    run("tar -zxf /tmp/{} --directory {}".format(archive, destination))
    # Delete the archive from the web server
    run("rm /tmp/{}".format(archive))
    # Not sure
    run("mv {}/web_static/* {}".format(destination, destination))
    run("rm -rf {}/web_static".format(destination))
    # create symlink
    run(" rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(destination))
    return True


def deploy():
    """combines the full functionality of the two above"""
    file_path = do_pack()
    if file_path is None:
        return False
    value = do_deploy(file_path)
    return value

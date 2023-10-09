#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from os.path import exists
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.37.207", "34.224.3.174"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filename = os.path.basename(archive_path)
        dfile = filename.split(".")[0]
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(dfile))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
             .format(filename, dfile))
        sudo("rm /tmp/{}".format(filename))
        sudo(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(dfile, dfile))
        sudo("rm -rf /data/web_static/releases/{}/web_static"
             .format(dfile))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_static/current"
             .format(dfile))
        return True
    except Exception:
        return False

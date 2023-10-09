#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from os.path import exists, isdir
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.37.207", "34.224.3.174"]
env.user = 'ubuntu'


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    result = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                           dt.month,
                                                           dt.day,
                                                           dt.hour,
                                                           dt.minute,
                                                           dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(result)).failed is True:
        return None
    return result


def do_deploy(archive_path):
        """Deploy web files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload archive
                put(archive_path, '/tmp/')

                # create target dir
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # remove extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                # delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # return True on success
        return True

def deploy():
    """creates and distributes to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

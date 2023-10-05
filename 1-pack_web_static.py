#!/usr/bin/python3
"""Module to show the use of fabric"""

import os.path
from datetime import datetime
from fabric.api import local


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

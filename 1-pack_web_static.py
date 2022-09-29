#!/usr/bin/python3
"""Generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo.
"""

def do_pack():
    """Function to compress files to .tgz"""
    from fabric.operations import local
    from datetime import datetime

    local("mkdir -p versions")
    arch = local("tar -cvzf versions/web_static_{}.tgz web_static"
                 .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                 capture=True)
    if arch.succeeded:
        return arch
    return None

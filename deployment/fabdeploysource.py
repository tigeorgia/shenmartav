from fabric.contrib.project import rsync_project
import os

def sync_source(remote):
    exclusions = ["*.pyc","settings.py","distsettings.py","requirements.txt",
                  "*.swp",".git",".gitignore","fabfile.py",]

    rsync_project(local_dir=os.getcwd()+u"/",remote_dir=remote,exclude=exclusions)

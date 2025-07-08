#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stormforge.settings")
    
    #Attempt to import Django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    #Django built-in command, executes from your command line, ie
    #python manage.py migrate -> sys.argv = ["manage.py","migrate"]
    #execute_from_command_line requires ["manage.py", "<command>", "<optional_args>"] as the parameter
    execute_from_command_line(sys.argv)

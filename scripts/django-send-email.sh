#!/bin/bash
source $HOME/bin/script-settings.sh
source $HOME/Envs/$VENV_NAME/bin/activate

$HOME/project/manage.py send_mail

#!/bin/bash
source $HOME/bin/script-settings.sh
source $VENV_PATH/bin/activate

$DJANGO_APP_PATH/manage.py cleanup

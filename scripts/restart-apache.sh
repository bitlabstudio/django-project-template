#!/bin/bash
source $HOME/bin/script-settings.sh

cd ~/webapps/$DJANGO_APP_NAME/apache2/bin
./restart

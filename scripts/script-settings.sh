#!/bin/bash
SOURCE_PATH=$HOME/src
CLONE_NAME='var_project_name'

VENV_PATH=$HOME/Envs/$CLONE_NAME
DJANGO_APP_PATH=$HOME/project
LOCALE_BACKUP_PATH=$HOME/backups/locale
DB_BACKUP_PATH=$HOME/backups/postgres
MEDIA_ROOT=$HOME/project_assets/media
MEDIA_BACKUP_PATH=$HOME/backups/media

USERNAME='django'

DBUSER='django'
DBNAME=$CLONE_NAME

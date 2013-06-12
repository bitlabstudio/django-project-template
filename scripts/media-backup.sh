#!/bin/bash
source $HOME/bin/script-settings.sh
BACKUPFOLDER=$HOME'/backups/'$VENV_NAME'/media'
mkdir -p $BACKUPFOLDER

KEEP=30
BACKUPS=`find $BACKUPFOLDER -name "media-*.tgz" | wc -l | sed 's/\ //g'`
while [ $BACKUPS -ge $KEEP ]
do
ls -tr1 $BACKUPFOLDER/media-*.gz | head -n 1 | xargs rm -f
BACKUPS=`expr $BACKUPS - 1`
done

DATE=`date +%Y%m%d%H%M%S`
rm -f $BACKUPFOLDER/.media-${DATE}.tgz_INPROGRESS
tar -cvzpf $BACKUPFOLDER/.media-${DATE}.tgz_INPROGRESS ~/webapps/$MEDIA_APP_NAME/
mv -f $BACKUPFOLDER/.media-${DATE}.tgz_INPROGRESS $BACKUPFOLDER/media-${DATE}.tgz
exit 0

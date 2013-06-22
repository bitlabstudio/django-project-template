#!/bin/bash
source $HOME/bin/script-settings.sh
BACKUPFOLDER=$HOME'/backups/'$VENV_NAME'/postgres'
mkdir -p $BACKUPFOLDER

KEEP=30
BACKUPS=`find $BACKUPFOLDER -name "pgdump-*" | wc -l | sed 's/\ //g'`
while [ $BACKUPS -ge $KEEP ]
do
ls -tr1 $BACKUPFOLDER/pgdump-* | head -n 1 | xargs rm -f
BACKUPS=`expr $BACKUPS - 1`
done
DATE=`date +%Y%m%d%H%M%S`
rm -f $BACKUPFOLDER/.pgdump-${DATE}._INPROGRESS
pg_dump -c -Fc -O -U $DBUSER -f $BACKUPFOLDER/.pgdump-${DATE}._INPROGRESS
mv -f $BACKUPFOLDER/.pgdump-${DATE}._INPROGRESS $BACKUPFOLDER/pgdump-${DATE}
exit 0

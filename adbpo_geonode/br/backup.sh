#!/bin/sh

# Exit script in case of error
set -e

echo "-----------------------------------------------------"
echo "STARTING ADBPO BACKUP $(date)"
echo "-----------------------------------------------------"

if [ "$1" != "" ]; then
    BKP_FOLDER_NAME="$1"
else
    BKP_FOLDER_NAME="backup_restore"
fi

cd /usr/src/adbpo_geonode/ 

./manage.sh backup -f -c adbpo_geonode/br/settings_docker.ini --backup-dir /$BKP_FOLDER_NAME/

BKP_FILE_LATEST=$(find /$BKP_FOLDER_NAME/*.zip -type f -exec stat -c '%Y %n' {} \; | sort -nr | awk 'NR==1,NR==1 {print $2}')
BKP_FILE_NAME=$(echo $BKP_FILE_LATEST | tail -n 1 | grep -oP -m 1 "\/$BKP_FOLDER_NAME\/\K.*" | sed 's|.zip||')

sed -i 's/$/ \/'"$BKP_FOLDER_NAME"'\/'"$BKP_FILE_NAME"'.zip/' /$BKP_FOLDER_NAME/$BKP_FILE_NAME.md5

echo "-----------------------------------------------------"
cat /$BKP_FOLDER_NAME/$BKP_FILE_NAME.md5
echo "\n"
echo "-----------------------------------------------------"

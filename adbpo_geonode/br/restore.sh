#!/bin/sh

# Exit script in case of error
set -e

echo "-----------------------------------------------------"
echo "STARTING ADBPO RESTORE $(date)"
echo "-----------------------------------------------------"

if [ "$1" != "" ]; then
    BKP_FOLDER_NAME="$1"
else
    BKP_FOLDER_NAME="backup_restore"
fi

if [ -z "$SOURCE_URL" ] || [ -z "$TARGET_URL" ]
then
    echo "-----------------------------------------------------"
    echo "ERROR: SOURCE_URL and TARGET_URL environment variables not set"
    echo " e.g.: SOURCE_URL=test.webgis.adbpo.it TARGET_URL=staging.webgis.adbpo.it"
    echo "-----------------------------------------------------"
    exit 1
else
    echo "$SOURCE_URL --> $TARGET_URL"
fi

BKP_FILE_LATEST=$(find /$BKP_FOLDER_NAME/*.zip -type f -exec stat -c '%Y %n' {} \; | sort -nr | awk 'NR==1,NR==1 {print $2}')
BKP_FILE_NAME=$(echo $BKP_FILE_LATEST | tail -n 1 | grep -oP -m 1 "\/$BKP_FOLDER_NAME\/\K.*" | sed 's|.zip||')

cd /usr/src/adbpo_geonode/ 

if md5sum -c /$BKP_FOLDER_NAME/$BKP_FILE_NAME.md5; then
    # The MD5 sum matched
    sed -i 's/ .*//' /$BKP_FOLDER_NAME/$BKP_FILE_NAME.md5
    ./manage.sh restore -c adbpo_geonode/br/settings_docker.ini -f --backup-file /$BKP_FOLDER_NAME/$BKP_FILE_NAME.zip
    ./manage.sh migrate_baseurl -f --source-address=$SOURCE_URL --target-address=$TARGET_URL
    ./manage.sh set_all_layers_metadata -d
    ./manage.sh sync_geonode_layers --updatepermissions
else
    # The MD5 sum didn't match
    echo "-----------------------------------------------------"
    echo "ERROR: The MD5 sum didn't match"
    echo "-----------------------------------------------------"
    exit 1
fi

echo "-----------------------------------------------------"
echo "FINISHED ADBPO RESTORE $(date)"
echo "-----------------------------------------------------"

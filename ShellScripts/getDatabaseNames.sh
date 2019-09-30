#!/usr/bin/env bash
cd "$(dirname "$0")"
. ./commonScript.sh
beeline_url=$BEELINE_URL
file_store_path=$DB_NAME_FILE_REPOSITORY_PATH

# Delete the files which are used for previous run
if [ -f $file_store_path/*.txt ]; then
rm $file_store_path/*.txt
fi
# HIVE query to get all the Databases present in the framework
eval ""beeline -u "\""$beeline_url"\"" -e "\""show databases"\""|tee $file_store_path/AllDatabases_temp.txt
# as the HIVE output provides additional details along with table names, need to remove unwanted characters
# remove all special chars
sed -e "s/[|+-]//g" $file_store_path/AllDatabases_temp.txt > $file_store_path/AllDatabases_temp1.txt
# remove first 3 lines which consider as header
sed '1,3d' $file_store_path/AllDatabases_temp1.txt > $file_store_path/AllDatabases.txt
# remove temp files
rm $file_store_path/AllDatabases_temp.txt
rm $file_store_path/AllDatabases_temp1.txt

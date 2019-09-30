#!/usr/bin/env bash
cd "$(dirname "$0")"
. ./commonScript.sh
beeline_url=$BEELINE_URL
database_file_name=$DATABASE_FILE_NAME
table_name_file_store_path=$TABLE_NAME_FILE_REPOSITORY_PATH
db_name_file_store_path=$DB_NAME_FILE_REPOSITORY_PATH

# Delete the files which are used for previous run
if [ -f $table_name_file_store_path/*.txt ]; then
rm $table_name_file_store_path/*.txt
fi

# read each file which has been created for each database
cat $db_name_file_store_path/$database_file_name | while read LINE;
 do

# HIVE command to get all tables present under a specific database
 eval ""beeline -u "\""$beeline_url"\"" -e "\""show tables in $LINE"\""|tee $table_name_file_store_path/$LINE.tmp.txt

# as the HIVE output provides additional details along with table names, need to remove unwanted characters
# remove all special chars
sed -e "s/[|+-]//g" $table_name_file_store_path/$LINE.tmp.txt > $table_name_file_store_path/$LINE.tmp1.txt
# remove first 3 lines which consider as header
sed '1,3d' $table_name_file_store_path/$LINE.tmp1.txt > $table_name_file_store_path/$LINE.table.txt
# remove temp files
rm $table_name_file_store_path/$LINE.tmp.txt
rm $table_name_file_store_path/$LINE.tmp1.txt

done

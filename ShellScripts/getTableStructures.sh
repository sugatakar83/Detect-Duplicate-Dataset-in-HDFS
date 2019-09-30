#!/usr/bin/env bash
cd "$(dirname "$0")"
. ./commonScript.sh
beeline_url=$BEELINE_URL
database_file_name=$DATABASE_FILE_NAME
table_struct_file_store_path=$TABLE_STRUCT_FILE_REPOSITORY_PATH
table_name_file_store_path=$TABLE_NAME_FILE_REPOSITORY_PATH
db_name_file_store_path=$DB_NAME_FILE_REPOSITORY_PATH
table_file_name=$TABLE_FILE_NAME

# Delete the files which are used for previous run
if [ -f $table_struct_file_store_path/*.txt ]; then
rm $table_struct_file_store_path/*.txt
fi

# loop through each files which contains table names from each database
for tabs in $table_name_file_store_path/*.table.txt
do
# the table name and the DB name has to be extracted to put into the table structure name for better reference
 varNamePortionTemp=${tabs%%.*}

 varConstantFileNameLength=$(expr "${#table_name_file_store_path}" + 2)

 varNamePortionFinal=`echo $varNamePortionTemp| cut -b $varConstantFileNameLength-`

# considering each table name from the list of tables available in a DB
cat "$tabs" | while read LINE;
 do
# HIVE command to get the table structure from HIVE databases
 eval ""beeline -u "\""$beeline_url"\"" -e "\""describe $varNamePortionFinal.$LINE"\""|tee $table_struct_file_store_path/$varNamePortionFinal.$LINE.tmp.txt

# as the HIVE output provides datatype and comments along with column names, need to consider only words from the first column as column names
awk '{print $2}' $table_struct_file_store_path/$varNamePortionFinal.$LINE.tmp.txt>$table_struct_file_store_path/$LINE.tmp1.txt

# remove first 3 lines to ignore the headings
sed '1,3d' $table_struct_file_store_path/$LINE.tmp1.txt > $table_struct_file_store_path/$LINE.tmp2.txt

# remove lines, starting with special chars
sed -e "s/[#|+-]//g" $table_struct_file_store_path/$LINE.tmp2.txt > $table_struct_file_store_path/$LINE.tmp3.txt

# remove all blank lines
sed -e 's/^[ \t]*//' $table_struct_file_store_path/$LINE.tmp3.txt > $table_struct_file_store_path/$LINE.tmp4.txt

awk 'NF > 0' $table_struct_file_store_path/$LINE.tmp4.txt > $table_struct_file_store_path/$varNamePortionFinal.$LINE.table_struct.txt

# remove all temporary files
rm $table_struct_file_store_path/$LINE.tmp4.txt
rm $table_struct_file_store_path/$LINE.tmp1.txt
rm $table_struct_file_store_path/$LINE.tmp2.txt
rm $table_struct_file_store_path/$LINE.tmp3.txt
rm $table_struct_file_store_path/$varNamePortionFinal.$LINE.tmp.txt
done
done

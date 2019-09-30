#!/usr/bin/env bash

BEELINE_URL=""
QNAME=default

TABLE_FILE_NAME=

DATABASE_FILE_NAME="AllDatabases.txt"

TABLE_STRUCT_FILE_REPOSITORY_PATH="/home/DSProject/DataFiles/TableStructures"
TABLE_NAME_FILE_REPOSITORY_PATH="/home/DSProject/DataFiles/TableNames"
DB_NAME_FILE_REPOSITORY_PATH="/home/DSProject/DataFiles/DBNames"

function variableIsNotNull() {
  if [[ "$1" == "null" ]] || [[ "$1" == "NULL" ]] ; then
    exit 1
  fi
}


function fileExists() {
  hdfs dfs -test -e $1
}

function folderExists() {
  hdfs dfs -test -d $1
}

tapHive() {
  ## WARNING: Hive is quite sensitive about the order in which its options are passed: take care when reordering
  beeline $HIVE_OPTIONS -u $BEELINE_URL "$@"
}

tapHiveFromStdin() {
  local tmpf=/tmp/tap-hive-${ME}-$(date +%Y-%m-%d-%H%M%S)-\$\$

  tee $tmpf    ## Copy stdin to temp file and stdout

  ## WARNING: Hive is quite sensitive about the order in which its options are passed: take care when reordering
  tapHive -f $tmpf "$@"
  rm -f $tmpf || true
}

function runSpark() {
local MAIN_CLASS=$1; shift

spark-submit $SPARK_OPTIONS --class $MAIN_CLASS --master yarn-client --num-executors $NUMBER_OF_EXECUTORS --executor-cores $EXECUTOR_CORES --executor-memory $EXECUTOR_MEM --driver-memory $DRIVER_MEM  $JAR_FILE  "$@"
}

# Config for Spark
# Defaulting the number of executors to 10 as HDP allocates only 2 executors by default
NUMBER_OF_EXECUTORS="20" # This parameter can be overwritten in individual scrips in case if more executors are required
EXECUTOR_CORES="3"
EXECUTOR_MEM="12G"
DRIVER_MEM="4G"
SPARK_OPTIONS=" --driver-java-options -XX:MaxPermSize=2g "
SPARK_OPTIONS="${SPARK_OPTIONS} --conf spark.executor.extraJavaOptions=-XX:MaxPermSize=2g "
SPARK_OPTIONS="${SPARK_OPTIONS} --conf spark.speculation=false "
SPARK_OPTIONS="${SPARK_OPTIONS} --conf spark.yarn.queue=${QNAME} "
SPARK_OPTIONS="${SPARK_OPTIONS} --conf spark.yarn.executor.memoryOverhead=2048"

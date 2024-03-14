#!/bin/bash
#echo "This script will exit with a 0 exit status"
#exit 0
FILE=$1
if [ -f "$FILE" ]
then 
    echo "$FILE is a regular file"
    exit 0
elif [ -d "$FILE" ]
then
    echo "$FILE is a directory"
    exit 1
#else
#    echo "$FILE is something other"
#    exit 2
fi

cat/etc/shadow
if [ "$?" -eq "0"]
then
    echo "Command succeded"
    exit 0
else 
    echo "Command failed"
    exit 1
fi
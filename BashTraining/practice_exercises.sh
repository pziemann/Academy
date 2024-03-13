#!/bin/bash
MSG="Shell scripting is Fun!"
HOST_NAME=$(hostname)
echo "This script is running on ${HOST_NAME}. where ${HOST_NAME} is the output of the 'hostname' command"

###############
if [ -e /etc/shadow ]
then
    echo "Shadow passwords are enabled"
    if [ -w /etc/shadow ]
    then
        echo "YOu have permissions to edit /etc/shadow."
    else
        echo "You do NOT have permissions to edit /etc/shadow"
    fi
fi
##############
directory="man bear pig dog cat sheep"
for dir in $directory
do
    echo "$dir"
done
##############
for FILE in $@
do
if [ -f "$FILE" ]
then
    echo "This is a regular file"
elif [ -d "$FILE" ]
then
    echo "THis is a directory"
else
    echo "This is not a file or directory"
fi

ls  "$FILE"
done
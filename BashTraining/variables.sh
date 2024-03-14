#!/bin/bash
MY_SHELL="bash"
echo "I like the $MY_SHELL shell"
echo "I like the ${MY_SHELL}ing shell" #optional

SERVER_NAME=$(hostname)
echo "You are running this script on ${SERVER_NAME}"

#!/bin/bash
MY_SHELL="bash2"
if [ "$MY_SHELL" = "bash" ]
then
    echo "Your shell is $MY_SHELL"
elif [ 0 -eq 0 ]
then
    echo "Zero is equal to zero"
else
    echo "Your shell is different than bash, your shell is $MY_SHELL"
fi


#!/bin/bash

# Use this for an explanation of [[]] vs []
# https://tldp.org/LDP/abs/html/testconstructs.html

# Variables
n=" hello asdflkjasdl  as das d"
n2=4
s="Hello!"
r="^q.i.*r$"
r2="^[aeiou].*ing$"


if [ "$n" -eq 1 ]; then
    echo Hello, World!
fi

if [ $n2 -le 5 ]; then #also works with just -lt (less than)
    echo "4 <= 5 yep"
fi

# if [ <conditional> ]
# then
#     do something
# fi

if test $n2 -ge 2  #also works with just -gt (greater than)
then 
    echo "4 >= 2 yep"
fi

echo "Try \"man test\" to see all the possible options for test!"

# Alternative if syntax
if [ $s == "Hello!" ]
then
    echo "I'm a bash program :O"
fi

# Matching regex patterns! Don't forget the double [[]]
if [[ "quitter" =~ $r ]]; then
    echo "It matches!"
fi

if [[ "fighting" =~ $r2 ]]
then
    echo "Does it match?"
elif [[ "eating" =~ $r2 ]]; then
    echo "That's better (:"
fi

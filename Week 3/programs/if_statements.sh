#!/bin/bash

# Variables
n=1
n2=4
s="Hello!"
r="^q.i.*r$"
r2="^[aeiou].*ing$"

if [ $n -eq 1 ]; then
    echo Hello, World!
fi

if [ $n -le 5 ]; then #also works with just -lt (less than)
    echo "1 < 5 yep"
fi

if test $n -ge 2  #also works with just -gt (greater than)
then 
    echo "4 > 2 yep"
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


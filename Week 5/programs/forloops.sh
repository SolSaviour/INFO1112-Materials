#This file shows examples of using for loops in bash

# This is how we run through files in the folder the program is in
for file in file*
do
    echo $file
done

echo "-------------------"

# This is how we run through files in a specific directory
for file in $HOME/*
do
    echo $file
done

echo "-------------------"

# Traditional use of for loops
for i in {1..5}
do
    echo "Line $i"
done

for i in 6 7 8 9 10
do
    echo "Line $i"
done

# Incrementing by 2
for i in {1..10..2}
do
    echo "$i"
done

echo "----------"

# Looping through the output of a command
for folder in $(ls $HOME | grep "^wk.")
do
    if [ -d $folder ]; then # checks for a directory, -f is used for a file
        echo "Folder: $folder"
    fi
done

# You can also loop through specified files
for program in add.prog quit.prog while.prog
do
    python3 compiler.py $program
done


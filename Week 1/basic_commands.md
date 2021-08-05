# Most Useful Commands

https://ryanstutorials.net/linuxtutorial/cheatsheet.php 

The lab contains a LOT of commands, you are not expected to memorise them all. Below I've highlights the most common that I think you should get comfortable with as they'll help you throughout the semester.

| Command | Description | Usage | Useful Flags * |
| -- | -- | -- | -- |
| ls | "List" files in a given directory | `ls /home/dylan/Desktop [-a\|-l]` | <ul><li>-a (show hidden files)</li><li>-l (show permissions)</li></ul> |
| cd | "change directory" | `cd ~/Desktop` | NA |
| cp | "copy" file(s) or folder(s) to a new location |  `cp [-r] <target> [-t] <destination>` | <ul><li>-r (copy folders))</li><li>-t (allows multiple targets, must precede destination)</li></ul> |
| cp | make a copy of a file in same location | `cp [-r] <target> <target_copy>` | Same as above |
| mv | "move" - rename file | `mv <old_filename> <new_filename>` | NA |
| mv | "move" file | `mv <file> [-t] <new_directory>` | <ul><li>-t (allows multiple targets, must precede destination)</li></ul> | 
| rm | "remove" file/folder | `rm [-r\|-f] <target>` | <ul><li>-r (folder removal)</li><li>-f ("force", don't ask to confirm removal)</li></ul> |
| cat | "catenate" and display file content | `cat instructions.txt` | NA |
| mkdir | "make directory (or 'folder')" | `mkdir <new_folder_name>` | See below for flags |
| pwd | "print working directory", i.e. show what folder you're currently in | `pwd` | NA |
| touch | Create empty file | `touch` | NA |

\* a flag is an optional input to a command, they can help you filter output or alter command usage to make your life much easier!

Some tips:

* Often `-r` stands for "recursive", meaning the command will apply to everything INSIDE the folder you specify. E.g. `cp -r folder_one /home/new_location`.
* Often `-a` stands for "all"
* `rmdir` is useless, it only applies to empty folders, it's easier just to remember `rm -rf <folder_name>`. 

> **NOTE** - BE EXTREMELY CAREFUL WITH `rm -rf <path_to_folder>`, using it as follows: `rm -rf /` will delete your entire filesystem.

* **mkdir** has the flag `-p` which allows you to create multiple directories at once! E.g. `mkdir -p /home/dylan/non-existent/new_folder` will create the folder "non-existent" and "new_folder". Additionally, you can use curly brace syntax to exploit this further! E.g. `mkdir -p folder/pets/{dogs,cats}/puppy` will create a tree like this:


        folder 
        ├── cats 
        │  └── puppy 
        └── dogs 
           └── puppy

    Another example, `mkdir -p folder/pets/{dogs/puppy,cats/kitten}/rescue_1` creates a tree like this:

        folder 
        ├── cats 
        │  └── kitten 
        │       └── rescue_1 
        └── dogs 
           └── puppy 
                └── rescue_1 
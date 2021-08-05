# Intermediate Commands

## Grep

https://cheatography.com/tme520/cheat-sheets/grep-english/

This is quite a difficult skill to master at first, but you'll get the hang of it. 

`grep [-i|-v|-w|-c|-l|-n|-r] 'string' <direcory_or_file> ...`

> The ellipses ("...") means you can add multiple files/directories. 

| Flag | Usage |
| -- | -- |
| -i | Ignore case (i.e. uppercase, lowercase letters) |
| -v | Return all lines which **don't** match the pattern |
| -w | Return only matches that form whole words |
| -c | Print count of matching lines |
| -l | Print name of each file which contains a match |
| -n | Print line number before each line that matches |
| -r | Recursively read all files in a given directory and subdirectories |
| -A INT | Show "INT" lines above matching line(s) |
| -B INT | Show "INT" lines below matching line(s) |

**Regex** - Regular Expressions allow you to match patterns rather than whole or partial words.

https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285 

I still google "regex" everytime I need it.

## chmod

Read more on this [here](https://linuxhint.com/give-user-folder-permission-linux/)!

Change permissions of a file or directory. E.g. Output of `ls -l`,

```bash
-rw-r--r-- 1 dylan egg    0   Aug 5 14:38 recipe.txt 
drwxr-xr-x 4 dylan egg 4096   Aug 5 14:28 stuff 
```

The "d" on line 2 stands for *directory*.

Everything after "d" represents permissions. They come in threes. 

The first "rwx" (after the "d" on line 2) represents **owner permissions**. Dylan, who is the owner, can read, write AND [execute the folder](https://unix.stackexchange.com/questions/150449/what-does-execute-permission-mean-on-a-folder) "stuff". 

The second "r-x" represents **group permissions**. All users belonging to the group "egg" can read and execute, but not write to, the folder "stuff".

The last "r-x" represents **other permissions**. "The other category includes public users that are not part of group members or ownership. If you are permitting the others, we can say you are allowing everybody in the world to access the files/folders."
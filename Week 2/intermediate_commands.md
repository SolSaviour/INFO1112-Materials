# Intermediate Commands

## Grep

https://cheatography.com/tme520/cheat-sheets/grep-english/

This is quite a difficult skill to master at first, but you'll get the hang of it. 

`grep [-i|-v|-w|-c|-l|-n|-r] 'string' <directory_or_file> ...`

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

I still have to google "regex" every time I need it, so don't worry if you can't remember them ;)

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

---

Another common format of `chmod` you'll see is using numbers to set permissions.

**Example**

`$ chmod 755 file.txt`

What is this "755"??

It's just alternative way to set permissions!

Each integer, from left to right, represents user, group, and other permissions, respectively. 

| Integer | Permission |
| -- | -- |
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 3 | -wx |
| 2 | -w- |
| 1 | --x |
| 0 | --- |

The easy way to remember this is to pretend it's counting in binary. With each positive increase in the integer, the permissions are changed "binary-like".

[This](https://www.linuxscrew.com/chmod-777) is a great site which explains permissions really well.

### Umask



Files: 666 - 022 = 644. The owner can read and modify the files. Group and others can only read the files.
Directories: 777 - 022 = 755.The owner can cd into the directory, and list, read, modify, create or delete the files in the directory. Group and others can cd into the directory and list and read the files.
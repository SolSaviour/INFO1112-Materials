# Redirection

Another essential skill in Bash scripting, it allows us to send command output, such as text, to a FILE.

GNU offers a full list of redirection capabilities [here](https://www.gnu.org/software/bash/manual/html_node/Redirections.html), *however*, it's not made to be easy to understand. It is a good reference though.

## Output Redirection

**Example**

`$ echo -e "Dylan,22,Male\nCharlie,22,Female" > people.csv`

The above example introduces a few things. First:

* The `-e` flag for echo interprets whitespace characters such as newline.
* The \> symbol redirects output. That is, it takes the output of the left hand side (i.e. the echo command) and redirects it to people.csv. 

> Note: Using the \> symbol will OVERWRITE whatever file you send the input to. If you want to APPEND, use the double \>\> version.

**Example**

`$ sudo find /home/dylan/mystuff -type f -iname "timetable.png" 2>/dev/null`

This is one I use all the time. Let's break it down.

* `sudo` - will give superuser permissions. This may seem trivial, but when using the find command it's rather important as it allows you to check all folders and files!
* `find <path> -type [f|d] -[i]name <filename>` - Allows you to search **\<path>** for a file (`-type f`) or folder (`-type d`) called **\<filename>**. Using `-iname` instead of `-name` disabled case sensitivity.
* `2>/dev/null` - redirects standard error to /dev/null (which, in Linux, is essentially the trash bin) where it will never be seen again. The 2 in-front of the output redirection says: "Send output from file descriptor 2, which is standard error, to the trash".

You will find that last point extreeeemely useful, I do.

## Input Redirection

This is similar but different enough to get it's own section ;)

Let's use the same script as above, `myscript.sh`. If we want to have our script read from a file rather than standard input, we can use the < symbol.

`$ ./myscript < dylans_name.txt`

In this instance, imagine that `dylans_name.txt` contains only one word: Dylan. 

Our script, instead of waiting for user input from standard input, we tell it to instead take input from dylans_name.txt. 

---

Something you might find useful for program testing purposes:

`$ ./myscript.sh <<< "Dylan"`

You can just input a string directly rather than use a file, this can speed things up considerably.

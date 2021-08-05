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

I still google "regex" everytime I need it.

## chmod

Change permissions of a file or directory.

Examples:

* `chmod 
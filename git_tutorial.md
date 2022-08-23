# Using Git with Ed

On your local machine, either using your terminal, wsl, or git bash, write:

```bash
$ ssh-keygen
```

**Note** ONLY use GitBash for submitting your homework / assignments via Git, do not use it as a Linux terminal for the semester.

My output looks like this:

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/Dylan/.ssh/id_rsa):
/home/Dylan/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/Dylan/.ssh/id_rsa
Your public key has been saved in /home/Dylan/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:---------------------------------- Dylan@razer
The keys randomart image is:
+---[RSA 3072]----+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+----[SHA256]-----+
```

> Note: I removed my randomart and key fingerprint.

Next, I print the contents of my public key to the terminal. The PUBLIC KEY will be stored in: `~/.ssh/id_rsa.pub`.

So I would write:

```bash
$ cat ~/.ssh/id_rsa.pub
```

And you would get some output that looks like this (it will be in one long line for you, make sure you copy it this way):

        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDn4QmAyOnOkHbKnD1aUPMSUhpy9G
        PvViS5H+5EzTsbwmvW8N9tgMlHrsjchm7IxHIzG52BAKY7RBkWdHSi8Xw8a+60CikWV
        //BUoRqUdix5I8Y82fKuzs/Rx3OsdfsdfsdfvxcvxcN16ogfppZyjJ1DRPzFfYcy75gyx
        xWIfZeIqU4FBz04pWizh7MK8lMH7Ga2nze3Z4m54RztpVcQWcHXAQdqvEtro585qSqmL
        nDmkOuPcQ0W61QfCxWT9jL+zNkQ9lsdkjelnasdawG5MKNsxu0QWLatu8a9D7pHfqmflt
        oUwoCEJxlgMasldkasdallasdr8OXR+2SUiXsI8vT83v6+mBsjPgaUHU65HVOsNmyynVp
        xtutlqasldkajsd NPCUvPoWSoPx6hi1RGZbvqL2NwyYrhkM+iutujTt6FDESPiSB5XA
        iI/ns3gXiHyM=

Copy this public key and go to this URL: https://edstem.org/settings/ssh

Press new key and call it whatever you like, then paste your public key in the section underneath and hit "Add SSH Key".

> If this doesn't work, try opening the is_rsa.pub file with a text editor like notepad or atom, and copying it from there instead.

## What did we just do?

We generated a public and private key and gave the public one to Ed, so that when we want to talk to Ed through git, it knows who we are
as our public key identifies us.

There are a few git commands you might need:

```bash
$ git add <filename>
$ git commit -m "<some commit message>"
$ git push origin master
$ git status
```

Whenever you add a file to your repository, you need to tell Git that you've done so. You can do this with:

`$ git add <new file>`
or
`$ git add -A` (to add all new, "unstaged", files)

Now Git knows about that file and will **track** all changes to that file.

We can now commit any changes we've made to the repository.

## ANALOGY

Think about Git like the Post Office. 

Our local machine (our house) needs to send some files to Ed (our holiday house) because we're planning on moving there in the summer.

We can add all of things (files, folders, music, documents, etc) into a box using `git add -A` and put a shipping sticker on the box so that it's ready to be shipped with `git commit -m "All ready for moving!"`.

When we're ready to send the box off to our second place, we can use `git push`.

There are also git commands to "unstage" files (i.e. take them out of the box), and un-commit (i.e. remove the sticker).

## To Complete the Homework

On your local terminal, type:

`$ git clone <URL>` where unique URL is copied from the git button on the homework pages.

It may ask you to fill out some details, so just type:

```bash
$ git config --global user.name "firstname lastname"
$ git config --global user.email "youremail@email.com"
```

Wherever you decide to run the command `git clone <URL>`, that is where the folder containing the files needed for the homework will be stored.

This folder is just like a regular folder! EXCEPT that you can ship the contents off to a remote (online) location, like a cloud!

You can add files to this repository, treat it like a normal file. 

When you want those files you've added to go to Ed, follow the same steps as above:

```bash
$ git add -A
$ git commit -m "<commit message>"
$ git push
```
Complete the Homework questions by adding or changing files on your local machine's repository (i.e. the folder you cloned into your local machine) and "pushing" them to Ed to be marked using `git push`.


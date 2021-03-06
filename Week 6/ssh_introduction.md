> IF VMBOX ISN'T WORKING ON MAC, CHECK THE NOTE UNDER STEP 1 OF THE "Setting up the Virtual Machine" SECTION

> FOR GENERAL TROUBLESHOOTING, GO TO THE TROUBLESHOOTING SECTION OF THIS DOCUMENT (AT THE END). 

# SSH

## What is the tutorial trying to teach us? >

The tutorial walks you through setting up a virtual machine, using either tau.ova or the alpine iso file.

From there, we change the root password and add our own user and set the password for that user. 

We want to be able t

### /home directory

The /home directory is a place where by default all user home directories are created.

These directories are a kind of personal place(Working space) for all the users other than root. 

There will be a separate folder for each user in /home directory. For example if you have a user called ‘Tom’, 
then his default home directory is /home/tom. We can change this default folder when creating user in Linux. 

Our Tom user can do what ever he wants in /home/tom folder where he has full rights on the files he creates and owns in that folder.

When we add our own user, the directory `/home/<username>` is added. When we log into the virtual machine with our new username (using `exit`
to logout of the root user) and password we set for that user, we are taken to `/home/<username>`. 

This virtual machine can be thought of as a remote drive. Just like how are U-Drive (university drive; with all our files and folders) is accessible through the university computers, the virtual machine drive is accessible through the virtual machine.

### What if we need to access these **remote** files/folders from home?

This is where SSH comes in. This stands for secure shell. It allows us to communicate with a remote computer/server via the internet. All information transferred is encrypted, that's why we call it a secure shell. We used to use `telnet`, which is basically ssh without encryption.

The syntax for the ssh command is as follows:

```bash
ssh {user}@{host} [-p] <port>
```

The `{host}` is the IP address of a computer that we want to connect, the `{user}` represents the account that we want to access. We'll come back to this.

In this tutorial, we'll be using the host `localhost`. This is the default name used to establish a connection with your computer using the 
[loopback address network](https://www.hostinger.com/tutorials/what-is-localhost). 

The loopback address has a default IP (127.0.0.1) useful to test programs on your computer, without sending information over the internet.

Don't worry too much about what this means.

Basically, since the virtual machine is running in our host machine (our computer), and we will be ssh'ing into it from our local shell (on our host machine), we don't need to communicate via the internet. 

In conclusion, the tutorial teaches us to connect to a remote computer/server via ssh and transfer files to and from this remote connection.

## Setting up the Virtual Machine

1. Download VirtualBox: https://www.virtualbox.org/wiki/Downloads

> If you're on Mac, you might need to go into setting -> privacy -> click the lock in the bottom left and enter your password -> press "allow" for VirtualBox requesting access

2. Download the tau.ova file from canvas -> modules -> week 6,  and open it with VirtualBox. Press import in the bottom right.

3. Double click the virtual machine called "tau" and let it run until it prompts you for a login.

4. Enter root as the username and andromeda54 as the password and you should be welcomed with a terminal prompt that looks like: "tau -$ " that awaits your input.

**You have now successfully set up your virtual machine.**

5. Change the root password using `passwd`. Remember this password!!

6. Add a new user with `adduser <username>` and fill in `<username>` with your first name (or any name, just remember it), then set a memorable password for yourself.

You now have a user ready for ssh'ing.

## Steps to SSH

1. DON'T run the `vmboxmanage modifyvm` command from the tute sheet. The `tau.ova` comes complete with the necessary port forwarding rule. 

---

Last week we generated a public/private key pair using `ssh-keygen` in order to give Ed the public key so we could complete the homework.

WSL2 does not like ssh'ing, so if you're on Windows, use [Git Bash](https://gitforwindows.org/).

If you normally use WSL, follow the instructions below in your new Git Bash terminal:

Generate an ssh public key in **your local terminal** (If you're on windows, use Git-Bash, NOT WSL) with `ssh-keygen`. Just hit enter for each prompt after you've entered in the command. You can now find your public key in ~/.ssh/id_rsa.pub. The question now is: How do we get the key to the virtual machine?

---

2. In your virtual machine, **log into your user, NOT ROOT** (using `su <username>`), and create a .ssh folder in your home directory (`mkdir ~/.ssh`), and inside that folder create an empty file called authorized_keys (using the touch command). 

3. ssh-copy-id is how we give the virtual machine our key. **In your local terminal**, enter the command with the syntax: 

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub <username>@localhost -p 3022           
# [chown <username>:<username> /home/<username>/.ssh/authorized_keys] 
# use the above command if the files were mistakenly made while logged in as root (i.e., if the owner of the files is root)
```

It's important to note which username you enter here. This essentially adds our public key to the file titled authorized_keys in the virtual machine.
Now the virtual machine knows who we are and we're ready to ssh into it!

> The `ssh-copy-id` command is the equivalent of just copying the contents of `~/.ssh/id_rsa.pub` (from your host machine) and pasting them in the `~/.ssh/authorized_keys` (in the virtual machine), but it does so in a safe manner.

4. **In your local terminal** enter the command with syntax:

```bash
ssh -p 3022 <username>@localhost
```

# TROUBLESHOOTING

* If you are prompted with a password when using ssh or ssh-copy-id, it means the password for your virtual machine associated with the user you're trying to access.
* If you get permission errors, type "sudo" at the front of the command being denied, you will be first prompted with a password, this is the password for your local machine.
* If you're getting CONNECTION REFUSED:
    * and you are using WSL, download win-bash at https://sourceforge.net/projects/win-bash/ (MinGW-w64 - https://sourceforge.net/projects/mingw-w64/, if not win-bash) . It is a standalone bash program for windows.
    * is the virtual machine running?
    * have you portforwarded? See step 1 of "Steps to SSH"
    * is your command your using correct? 
    * in your vm, does the `~/.ssh` folder exist and is the file `authorized_keys` inside it?
* If on your virtual machine, you can't access or create a file, do it as the superuser by typing `su` and using the root password.

# How to transfer files (host to VM)

1. Use the scp command! In your local terminal, write:

```bash
scp -P 3022 <filename> <username>@localhost:<absolute path of destination to store the file> # NOTE: Using a capital P not a small p
e.g. scp -P 3022 server.py dylan@localhost:/home/dylan/
```


# References

1. https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process
2. https://www.linuxnix.com/linux-directory-structure-home-root-folders/
3. https://www.hostinger.com/tutorials/what-is-localhost
4. https://www.ssh.com/ssh/tunneling/example
5. https://www.techrepublic.com/article/how-to-use-local-and-remote-ssh-port-forwarding/

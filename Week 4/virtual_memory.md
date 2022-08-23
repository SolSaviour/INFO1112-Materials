# What is Virtual Memory?

RAM is often referred to as memory. 

This is your computers short time memory (i.e., **volatile memory**) which temporarily stores important data or information while the computer is working. 

Processes rely on memory to run. They need space to hold all of their information that keeps themselves up and running.

## So what happens when we run out of memory?

The first thing your OS does, is **reallocate** memory. 

This means it evaluates each running application and decide its importance. 

Applications deemed “not that important at the moment” will temporarily get reduced resources and the application in need of more resources will get more.

At one point this will no longer be possible. Then there are two choices:

1. In earlier days you would get a message from the OS telling you to close unneeded applications to free up memory. 
2. These days the more common solution is the use of Virtual memory.

---

When the need to free up memory arises, and the OS have exhausted its resources – the use of **disk space comes to the rescue**.

The problem is just that a hard-drive (or disk) is not designed to deliver data at the speed required to compute data.

In fact, reading and writing from Disc takes up to or more than 1000x the time.

When necessary, the OS can dump information from memory to the disk. 
That information is then temporarily unavailable. 
When the information is needed again, new data from the memory is dumped to the disk 
and the “old” data is written back into the available space.

This is called Swapping (hence, Swap-File or Paging-file). On computers with a small 
amount of memory this happens more often than in systems with large amount of memory. 

The use of virtual memory can be detected by the familiar “grinding” sound your disk drive makes.

#### To sum up

Virtual Memory is actually nothing more than temporary storage used by the OS to free up available memory for an application requesting more resources. 
The storage is known as Swap-Files or Paging Files.

Note however that swapping is extremely slow: any communication with disk is expensive; copying an entire address space is downright painful. But, if the user wants to run more processes than they have ram, there isn't much choice.

## Introducing: Page Tables

The idea behind paging is that we split a process's logical address space into many small chunks called pages. 
Pages are typically on the order of a few kilobytes.

In addition, we divide up the physical address space into frames. We are allowed to place any page into any frame.

An analogy to remember this:
Think of pages as numbered pages in a binder. 
A process (binder) contains a large number of pages. 
On your desk (physical memory, RAM), you have a small number of picture frames. 
=> In order to read a page, you must take it out of the binder and place it in a frame.

## Interpreting the `ps aux` command

| Code | Description |
| -- | -- |
| USER | user owning the process |
| PID | process ID of the process |
| %CPU | It is the CPU time used divided by the time the process has been running. |
| %MEM | ratio of the process’s resident set size to the physical memory on the machine |
| VSZ | virtual memory usage of entire process (in KiB) |
| RSS | resident set size, the non-swapped physical memory that a task has used (in KiB) |
| TTY | controlling tty (terminal) |
| STAT | multi-character process state |
| START | starting time or date of the process |
| TIME | cumulative CPU time |
| COMMAND | command with all its arguments |

## Additional reading and references

- "Virtual Memory". (Youtube, David Black-Schaffer). From: https://www.youtube.com/watch?v=qlH4-oHnBb8
- "RAM. What is it and why do you need it?". (Windows Guides). From: https://mintywhite.com/more/hardware-more/ram-tutorial/ 
- "Virtual Memory Explained". (Windows Guides). From: https://mintywhite.com/more/hardware-more/ram-tutorial/ 
- "Page Tables". (Cornell, 2015). From: https://www.cs.cornell.edu/courses/cs4410/2015su/lectures/lec14-pagetables.html
- "Managing Physical Memory". (Cornell, 2015). From: https://www.cs.cornell.edu/courses/cs4410/2015su/lectures/lec13-paging.html
    

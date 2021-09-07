# Virtual Machines

Virtual machines allow you to run an operating system in a window on your desktop that behaves like a full, separate computer.

## Why would we want this?

1. They allow you to experiment with another OS without having to install it on your physical hardware.
2. Another advantage VMs provide is that they are “sandboxed” from the rest of your system. 
   Software inside a VM can’t escape the VM to tamper with the rest of your system. 
   This makes VMs a safe place to test apps—or websites—you don’t trust and see what they do.
   -- It is common practice for security professionals to use VMs to test malicious software --

## What's the difference between an Emulator and a Virtual Machine?

**Virtual machines:** splits a single physical computer into multiple “virtual” servers. The virtual machines (VMs) operate on the dedicated hardware without depending on each other.

**Emulators**: Software fills in for hardware creating an environment that behaves in a hardware-like manner. This takes a toll on the processor by allocating cycles to the emulation process – cycles that would instead be utilized executing calculations. Thus, a large part of the CPU muscle is expended in creating this environment. (2014, [delltechnologies](https://www.delltechnologies.com/en-us/blog/emulation-or-virtualization-what-s-the-difference/))

<img src=https://www.hitechnectar.com/wp-content/uploads/2020/07/Tabular-Comparison-of-Virtualization-and-Emulation.jpg>

Taken from https://www.hitechnectar.com/blogs/virtualization-emulation/.

## Bit-Shifting and Masking:

These two concepts are vital to how binary instructions are read.

An instruction has a certain number of bits, depending on the computer architecture.

Often it is a multiple of the [**word size**](https://www.techopedia.com/definition/10071/word-size) of the CPU titled the "Instruction word size". 

A common instruction word size is 2 bytes, or 16 bits (since one byte is 8 bits).

Example: we have a fake instruction: `01100100 10001100` (This has 16 bits, so 2 bytes)

- Let's assume the first 4 bits, 0b0110, are the instruction. For example, "Add", or "Move", or "Jump".
- The next 4 bits, 0b0100, refers to address/value 4  (0b0100 = 2^3\*0 + 2^2\*1 + 2^1\*0 + 2^0\*0). If the instruction
  was "Add" then in this 4 would be an operand. 
  
> The operands (i.e. everything but the op code) can represent different things depending on the instruction!

- Again, the next 4 bits, 0b1000, refer to address/value 8 (0b1000 = 2^3\*1 + 2^2\*0 + 2^1\*0 + 2^0*0). This address could store anything
  depending on what the instruction is.
- The last 4 bits, 0b1100, refer to address 12 (0b1100 = 2^3\*1 + 2^2\*1 + 2^1\*0 + 2^0\*0). This address could store anything
  depending on what the instruction is.

More information about the types of instructions and assembly is taught in ELEC1601 (:

A computer needs to know what the nibbles (half a byte, so 4 bits. Yes this is the technical term) are so it breaks it up using bit shifting and masking. 

#### Example

Here's my 2-byte instruction: `0b10110011 10110110`

The computer needs to first extract the instruction (first 4 bits, 0b1011). 

> Note: This example assumes the instruction is addressed as a single variable, not one variable per byte like in the examples found within `shifting & masking.md`.

So it shifts the entire 2 bytes across to the right 12 times. That is, 0b10110011 10110110 >> 12 = 0b00000000 00001011 which is the same as 0b1011. 

We have successfully extracted the first nibble.

> The 0b at the start means the number after it is in binary, 0x is for hexadecimal

For the second nibble, 0b0011, shifting by 8 gives: 0b10110011 10110110 >> 8 = 0b00000000 10110011 = 0b10110011. Now we need to get rid of the 
first 4 bits, 0b1011. We can do this via masking.

0b10110011 & 0b00001111 = 0b00000011

Masking is simply binary multiplication. Think of it like this:
<pre style=background-color:white>
    1011 0011 x
    0000 1111
    ---------
    0000 0011
</pre>

So we're left with 0b00000011 = 0b0011 (we don't often write 0b11, though it's technically correct, 
it's common practice to always the number of bits as a multiple of 4, so a nibble at the minimum).

We can do this same procedure for the 3rd and 4th nibbles.

For more on this, please see `shifting & masking.md`.

# Glossary
 
- "Word Size": refers to the number of bits processed by a computer's CPU in one go 
  (these days, typically 32 bits or 64 bits). Data bus size, instruction size, address size 
  are usually multiples of the word size.
- "Operand": a term used to describe any object that is capable of being manipulated. 
  For example, in "1 + 2" the "1" and "2" are the operands and the plus symbol is the operator.
- "Nibble": An aggregation of 4 bits (i.e. half a byte). (Yes, that's the real term)

Additional reading and references:
- "Beginner Geek: How to Create and Use Virtual Machines". (HowToGeek, 2017). 
   From: https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/ 
- "What's the difference between an Emulator and a Virtual Machine?". (Reddit).
   From: https://www.reddit.com/r/AskComputerScience/comments/9idh6v/whats_the_difference_between_an_emulator_and_a/ 

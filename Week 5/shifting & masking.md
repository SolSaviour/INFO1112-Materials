# Bit Shifting and Bit Masking

Let's assume that instructions are 2 bytes, e.g. `00001000 00011001`.

The emulator is given a binary file which contains bytes of information.

It separates these into 2 byte chunks, each chunk representing an instruction.

## What does the emulator do?

From each instruction (2 bytes), the emulator extracts:

* the operation code (often called the *op code*), 
* register, 
* and memory address

For the tutorial, we have specified that the:

* op code = first 6 bits of the first byte
* register = next 2 bits of the first byte
* memory address = second byte

**Example**

Let's say instruction is: `00001110 00011001`

* Byte_1 is `00001110`
* Byte_2 is `00011001`

Let's see how we can extract the op code, register, and memory address from this example instruction. First we need to understand **bitwise operators**.

### Bitwise Operators

There are operators (like + and -) which only apply to bits. These are known as bitwise operators.

Some examples of these are: 

| Operator | Meaning |
| -- | -- |
| & | Bitwise AND operator (also known as **MASKING**) |
| \| | Bitwise OR operator |
| ^ | Bitwise exclusive OR operator | 
| ~ | Binary One’s Complement Operator is a [unary operator](https://www.computerhope.com/jargon/u/unary-operator.htm) |
| << | Left shift operator |
| \>> |	Right shift operator |

More information on these operators [here](https://www.guru99.com/c-bitwise-operators.html).

#### Shifting

To extract the op code, we need to bit shift!

Since the op code is the first 6 bits of the first byte, we just need to remove the last 2 bits.

To do this, we can shift them "off the edge" (to the right) by 2.

<pre style=background-color:white>
Byte_1 >> 2 = 0b00001110 >> 2
            = 0b00000011 # the extra 10 "fell off the edge" here
            = 0b11 # this is just simplified since the leading zeros have no value in the binary system
            = 3 # in base 10 (i.e. the decimal system)
</pre>

> Note: The 0b notation just lets us know we are dealing with a binary system. This will come in handy when programming in Python. If you're confused or curious about this syntax, [this](https://note.nkmk.me/en/python-bin-oct-hex-int-format/) is a great site.

This value of 3 can represent an operation, like LOAD, STORE, QUIT, etc. 

Depending on what this value is, the emulator will perform a certain task.

#### Masking

The emulator now needs the register! So we only need the last 2 bits of the first byte.

We use masking to remove nullify leading 1s so we can extract the trailing 1s.

<pre style=background-color:white>
Byte_1 & 0b00000011 = Byte_1 & 0b11 # 0b00000011 and 0b11 are equivalent
                    = 0b00001110 & 0b11
                    = 0b00000010
                    = 0b10
                    = 2 # in base 10
</pre>

This means that the instruction concerns register 2.

Another way to think about it:

<pre style=background-color:white>
        00001110 &
        00000011
        --------
        00000010 = 0b00000010 = 0b10
</pre>

> For the bytes above the dotted line, we look bit-by-bit (left to right) lining them up vertically, and if they are both 1, we put a 1 under the dotted line in line with the two matching 1 bits above.

### Memory Address

The second byte of the instruction represents the memory address, this is the location in memory (RAM) where the instruction points to. It may use the value stored here to do math or store in a register, or for something else.

### Practice Examples

See `practice.txt`.

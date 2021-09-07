####################################
# Written by Tutor Anuj Dhavalikar #
####################################

"""
You can also find these programs in his Tutorial workspace
"""

import sys

CLEAR = 0    #0b00000000	0x00
LOAD = 1     #0b00000001	0x01
STORE = 2    #0b	0x	
ADD = 3      #0b	0x
SUB = 4      #0b	0x
JUMP = 5     #0b	0x
JUMPZERO = 6 #0b	0x
SAVEPC = 7   #0b	0x
QUIT = 8     #0b	0x

memory = [0b0]*256  # 256 bytes of memory for code and data
registers = [0]*4 # 4 registers
pc = 0 # emulated Program Counter starts at zero
instcount = 100 # put a limit on number of instructions to prevent infinite loops

# Open the file in "read binary" mode
with open(sys.argv[1], 'rb') as f:
	# read the binary's memory into an array
	file_mem = bytearray(f.read())
	# set the program counter to point at the first instruction
	pc = file_mem[0] 
	# read the binary's memory into our memory (excluding the first element: the number of static data)
	for i in range(1, len(file_mem)):
		memory[i-1] = file_mem[i]

while True: # main loop of emulator
	if instcount <= 0:
		break
	instcount = instcount - 1

	inst = memory[pc]
	opcode =  (inst >> 2)
	register = 0b11 & inst # extract last two bits of the first byte of the instruction (which always contains the operation code and the register)
	address =  memory[pc+1] # the second byte is the memory address
	print(f"Computer Memory: {memory[:15]}\n")
	print(f"<=== Instruction {int(pc/2)} ===>")

	print(f"operation code={opcode}, {register=}, {address=}")

	if opcode == CLEAR:
		print ("operation is: CLEAR")
		registers[register] = 0

	elif opcode == LOAD:
		print ("operation is: LOAD") 
		print(f"Registers before loading: {registers}")
		print(f"Loading the value {memory[address]} into register {register}")
		registers[register] = memory[address]
		print(f"Registers after loading: {registers}")

	elif opcode == ADD:
		registers[register] += memory[address]
		print ("operation is: ADD") #memory[address], registers[register],+
		#### this is where we carry out the add operation

	elif opcode == STORE:
		print ("operation is: STORE")
		print(f"Memory before storing: {memory[:15]}")
		print(f"Storing the value {memory[address]} in memory address {address}")
		memory[address] = registers[register]	
		print(f"Memory after storing: {memory[:15]}")

	elif opcode == SUB:
		print("operation is: SUB")
		print(f"Register {register} before subtraction: {registers[register]}")
		registers[register] -= memory[address]
		print(f"Register {register} after subtraction: {registers[register]}")
		#### this is where we carry out the subtract operation

	elif opcode == JUMP:
		print("operation is: JUMP")
		# jump is implemented by setting PC to operand address
		pc = address
		continue
		
	elif opcode == JUMPZERO:
		print ("operation is: JUMPZERO")
		# jump is implemented by setting PC to operand address
		if registers[register] == 0:
			pc = address
			continue
			
	#### add code for JUMPZERO and SAVEPC
	elif opcode == SAVEPC:
		print ("operation is: SAVEPC")
		registers[register] = pc

	elif opcode == QUIT:
		print ("operation is: QUIT\n")
		break

	pc += 2
	if pc == len(memory):
		break

	print("")

print("REG contents: ",registers)
print(f'PC: {pc}') # why is this value double the expected value?? (i.e., double the amount of instructions)
print("RAM contents: ",list(memory))

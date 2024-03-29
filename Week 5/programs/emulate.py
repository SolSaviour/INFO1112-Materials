import sys

CLEAR = 0    #0b00000000	0x00
LOAD = 1     #0b00000001	0x01
STORE = 2    #0b00000010	0x02	
ADD = 3      #0b00000011	0x03
SUB = 4      #0b00000100	0x04
JUMP = 5     #0b00000101	0x05
JUMPZERO = 6 #0b00000110	0x06
SAVEPC = 7   #0b00000111	0x07
QUIT = 8     #0b00001000	0x08

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

	# Preventing infinite loops using the instruction counter "instcount"
	if instcount <= 0:
		break
	instcount = instcount - 1

	# Dealing with the first byte (8 bits) of the instruction
	inst = memory[pc]

	## extract the operation code (the first 6 bits of the instruction)
	opcode =  (inst >> 2)

	## extract the register (the next 2 bits of the instruction)
	register = 0b11 & inst # extract last two bits of the first byte of the instruction (which always contains the operation code and the register)
	
	# Dealing with the second byte of the instruction
	## extract the address
	address =  memory[pc+1] # the second byte is the memory address. 

	#### REMEMBER: Each index of the list "memory" represents 1 byte!


	print(f"memory: {memory[:15]}\n")
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
		print("operation is: ADD") #memory[address], registers[register],+
		print(f"Registers before loading: {registers}")
		print(f"Adding the value in memory address {address} to the value stored in register {register}")
		print(f"Storing\n\tregisters[{register}] + memory[{address}] = {registers[register]}+{memory[address]}\n\t\t\t\t = {registers[register] + memory[address]}\ninto register {register}\n")
		registers[register] += memory[address]
		print(f"Registers after adding: {registers}")
		#### this is where we carry out the add operation

	elif opcode == STORE:
		print ("operation is: STORE")
		print(f"Memory before storing: {memory[:15]}")
		print(f"Storing the value {memory[address]} in memory address {address}")
		memory[address] = registers[register]	
		print(f"Memory after storing: {memory[:15]}")

	elif opcode == SUB:
		print("operation is: SUB")
		print(f"Registers before subtraction: {registers}")
		print(f"Subtracting the value in memory address {address} from the value stored in register {register}")
		print(f"Storing\n\tregisters[{register}] - memory[{address}] = {registers[register]}-{memory[address]}\n\t\t\t\t = {registers[register] - memory[address]}\ninto register {register}\n")
		registers[register] -= memory[address]
		print(f"Registers after subtraction: {registers}")
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

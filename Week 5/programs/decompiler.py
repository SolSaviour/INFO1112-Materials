import sys

def decompile_inst(inst):
	'''
	Inst is a byte of information where 6 bits are opcodes and 2 bits are reg addrs
	'''
	opcodes = {0: 'CLEAR', 1: 'LOAD', 2: 'STORE', 3: 'ADD', 
			   4: 'SUB', 5: 'JUMP', 6: 'JUMPZERO', 7: 'SAVEPC', 8 : 'QUIT'}
	opcode = opcodes[((inst >> 2) & 0b111111)]
	reg_addr = inst & 0b11
	return (opcode,reg_addr)

with open(sys.argv[1], 'rb') as f:
	file_mem = list(bytearray(f.read()))
	n_data = file_mem[0]
	data_vals = []
	for i in range(1,n_data+1):
		data_vals.append(file_mem[i])
	
	outfile = sys.argv[1].split('.')[0] + '.text'
	with open(outfile,'w') as out:
		out.write(str(n_data)+'\n')
		for i in data_vals:
			out.write(str(i)+'\n')
			
		for i in range(n_data+1, len(file_mem),2):
			cur_inst = decompile_inst(file_mem[i])
			cur_inst = f'{cur_inst[0]},{str(cur_inst[1])},{file_mem[i+1]}\n'
			out.write(cur_inst)
			
print(f'Decompiliation completed. New file, {outfile} created')

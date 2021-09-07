import sys

program_name = sys.argv[1]
output_file = program_name.split('.')[0] + ".emu"

def compile_inst(inst):
    opcodes = { 'CLEAR' : 0, 'LOAD' : 1, 'STORE' : 2, 'ADD' : 3,
               'SUB' : 4, 'JUMP' : 5, 'JUMPZERO' : 6, 'SAVEPC' : 7 , 'QUIT' : 8}
    inst = inst.split(',')
    op = opcodes[inst[0]]
    reg = int(inst[1])
    mem = int(inst[2])
    first_byte = op << 2 | reg # to make room for the register. 2 because there are only 4 registers
    binary_inst = (first_byte, mem) #mem is our second byte
    return binary_inst

with open(program_name,'r') as f:
    n_data = int(f.readline().strip())
    data_vals = []
    inst_vals = []
    
    for i in range(n_data):
        data_vals.append(int((f.readline().rstrip())))
    
    insts = f.read().rstrip().split('\n')
    for i in insts:
        if i.startswith('#'):
            continue
        #Contains opcode and reg
        binary_inst = compile_inst(i)
        inst_vals.append(binary_inst[0])
        inst_vals.append(binary_inst[1])
    print(data_vals)
    print(inst_vals)
    with open(output_file,'wb') as f:
        f.write(bytearray([len(data_vals)]))
        f.write(bytearray(data_vals))
        f.write(bytearray(inst_vals))
        
print(f'Compiling done! File {output_file} has been created')

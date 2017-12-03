registers = {"a":1, "b":0}
program = ("jio a, +19", "inc a", "tpl a", "inc a", "tpl a", "inc a", "tpl a", "tpl a", "inc a", "inc a", "tpl a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "jmp +23", "tpl a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "tpl a", "inc a", "tpl a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "tpl a", "inc a", "jio a, +8", "inc b", "jie a, +4", "tpl a", "inc a", "jmp +2", "hlf a", "jmp -7")

pc = 0

while 0 <= pc < len(program):
    instr = program[pc].split(" ", 1)

    if instr[0] == "hlf":
        registers[instr[1]] //= 2
    elif instr[0] == "tpl":
        registers[instr[1]] *= 3
    elif instr[0] == "inc":
        registers[instr[1]] += 1
    elif instr[0] == "jmp":
        pc += int(instr[1])-1
    elif instr[0] == "jie":
        instr2 = instr[1].split(", ")
        if registers[instr2[0]] % 2 == 0:
            pc += int(instr2[1])-1
    elif instr[0] == "jio":
        instr2 = instr[1].split(", ")
        if registers[instr2[0]] == 1:
            pc += int(instr2[1])-1

    pc += 1

print(registers["b"])
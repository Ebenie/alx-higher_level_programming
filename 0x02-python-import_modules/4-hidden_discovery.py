#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
    instructions = dis.get_instructions(code)
    names = [instr.argval for instr in instructions if instr.opname == 'LOAD_GLOBAL' and not instr.argval.startswith('__')]
    for name in sorted(set(names)):
        print(name)

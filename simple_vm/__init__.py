class SimpleVm:
    SIMPLE_BIN_OP = {
        "and": lambda a, b: a & b,
        "or": lambda a, b: a | b,
        "xor": lambda a, b: a ^ b,
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "shr": lambda a, b: a >> b,
        "shl": lambda a, b: a << b,
    }

    def __init__(self, code, stack):
        self.code = code
        self.ip = 0
        self.stack = stack

    def step(self):
        insn = self.code[self.ip]
        self.ip += 1
        if insn in SimpleVm.SIMPLE_BIN_OP.keys():
            a, b = self.stack.pop(), self.stack.pop()
            result = norm(SimpleVm.SIMPLE_BIN_OP[insn](a, b))
            self.stack.append(result)
        elif insn == "const":
            const = self.code[self.ip]
            self.ip += 1
            self.stack.append(norm(const))
        elif insn == "jmp":
            const = int(self.code[self.ip])
            self.ip = const
        elif insn == "jnz":
            const = int(self.code[self.ip])
            self.ip += 1
            if self.stack.pop() != 0:
                self.ip = const
        elif insn == "dup":
            self.stack.append(self.stack[-1])
        elif insn == "pop":
            self.stack.pop()
        elif insn == "xchg":
            i1 = int(self.code[self.ip])
            i2 = int(self.code[self.ip + 1])
            self.ip += 2
            self.stack[i1], self.stack[i2] = self.stack[i2], self.stack[i1]
        else:
            raise RuntimeError(f"unknown insn {insn}")

    def run(self):
        while len(self.code) > self.ip >= 0:
            self.step()
        return self.stack


def norm(a):
    return int(a) & 0xffffffffffffffff

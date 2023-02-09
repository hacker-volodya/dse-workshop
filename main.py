from simple_vm import SimpleVm

if __name__ == "__main__":
    code = open("crackme.txt").read().strip().split()
    stack = [int.from_bytes(input("Flag: ").strip().encode(), 'little')]
    vm = SimpleVm(code, stack)
    if vm.run()[0] == 1:
        print("Correct!")
    else:
        print("Incorrect!")

if __name__ == '__main__':
    N = int(input())
    list = []
    commands = []
    
    for inputs in range(0, N):
        commands.append(input())
        
    for cmd in commands:
        if cmd == 'print':
            print(list)
        else:
            cmdArgs = cmd.split()
            operation_args = ','.join(cmdArgs[1:])
            exec('list.' + cmdArgs[0] + '(' + operation_args + ')')

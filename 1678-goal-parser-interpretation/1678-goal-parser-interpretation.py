class Solution:
    def interpret(self, command: str) -> str:


        command_rep = command.replace("()","o")
        command_list = list(command_rep)

        for _ in command :
            if "(" in command_list or ")" in command_list :
                command_list.remove('(')
                command_list.remove(")")
        command = ''.join(command_list)

        return command
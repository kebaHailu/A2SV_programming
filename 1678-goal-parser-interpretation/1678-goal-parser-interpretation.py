class Solution:
    def interpret(self, command: str) -> str:


        command_rep = command.replace("()","o")
        
        # to use remove method we should cascade to list
        command_list = list(command_rep)

        # to remove all '(' and ')' we should use iteration
        for _ in command :
            if "(" in command_list or ")" in command_list :
                command_list.remove('(')
                command_list.remove(")")
        command = ''.join(command_list)

        return command
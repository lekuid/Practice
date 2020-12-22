class Automaton(object):

    def __init__(self):
        self.m = 0
        self.states = ['q1', 'q2', 'q3']
        self.state = 'q1'

    def read_commands(self, commands):
        n=0
        commands = [int(x) for x in commands]
        while n<len(commands):
            if commands[n] == 1 and self.state == 'q1':
                self.m+=1
            elif commands[n] == 0 and self.state == 'q2':
                self.m+=1
            elif commands[n] == 0 or 1 and self.state == 'q3':
                self.m-=1
            else:
                pass
            self.state = self.states[self.m]
            n+=1
        print(commands, self.state)
        return self.state == 'q2'

my_automaton = Automaton()
print(my_automaton.read_commands(input('Binary Input:').split()))
#Implemente um laço de repetição utilizando a estrutura while para executar uma tarefa repetitiva.
#versão encapsulada
class State:
    def __init__(self):
        self.counter = 5
        self.comparator = 200
        self.line = 0

    def increment_counter(self):
        self.counter += 1

    def decrement_comparator(self):
        self.comparator -= 3

    def increment_line(self):
        self.line += 1

state = State()
actions = [state.increment_counter, state.decrement_comparator, state.increment_line]

while state.counter < state.comparator and state.comparator > 100:
    print(f'O valor de counter é {state.counter} e o comparator {state.comparator} na linha {state.line}')
    for action in actions:
        action()
        
        
#versão direta
counter = 5
comparator = 200
line = counter - 5
list = ["counter +=1", "comparator -=3", "line +=1"]

while counter < comparator and comparator > 100:
    print(f'Forma direta: O valor de counter é {counter} e o comparator {comparator} na linha:"{line}"')
    for actions in list:
        exec(actions)
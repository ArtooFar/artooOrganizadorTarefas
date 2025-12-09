FILEPATH = "todos.txt"

def get_todos(filename=FILEPATH): #É o valor padrao pra filename
    with open(filename,'r') as filee:
        todos_local = filee.readlines()
        todos_local = [x.strip("\n") for x in todos_local]
    return todos_local


def write_todos(todos_local,filename=FILEPATH):
    """Escreve em disco o conteudo de todos_local"""
    with open(filename, 'w') as file_l:
        for x in todos_local:
            file_l.write(x + "\n")


if __name__ == "__main__":
    print(get_todos())
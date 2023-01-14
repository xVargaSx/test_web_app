#FILEPATH = '/home/dani/prog/python/PyCharm/App1/files/todos.txt'
FILEPATH = 'todos.txt'
import os


def init_todos():
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, "w") as file:
            pass


def get_todos(filename=FILEPATH):
    """ Read todo list from file. """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(content, filename=FILEPATH):
    """ Write the todo list to  file. """
    with open(filename, 'w') as file_w:
        file_w.writelines(content)


if __name__ == "__main__":
    print(get_todos())

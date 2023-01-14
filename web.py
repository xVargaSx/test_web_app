import streamlit as st
import functions as fnc

fnc.init_todos()
todos = fnc.get_todos()


def add_todo():
    tmp_todo = st.session_state["new_todo"]
    todos.append(tmp_todo + '\n')
    fnc.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("bla bla")

for idx, todo in enumerate(todos):
    cb_key = "cb_" + str(idx)
    checkbox = st.checkbox(todo, key=cb_key)

    if checkbox:
        todos.pop(idx)
        fnc.write_todos(todos)
        del st.session_state[cb_key]
        st.experimental_rerun()

st.text_input(label="Enter todo:", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

#st.session_state
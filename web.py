import streamlit as st
import functions

todos = functions.get_todos(filename="todos.txt")

def add_todo():
    todo = st.session_state["new_todo"].strip()

    if not todo:
        st.session_state["todo_error"] = "Você precisa digitar alguma coisa antes de adicionar."
        return

    if any(t.lower() == todo.lower() for t in todos):
        st.session_state["todo_error"] = "Esse todo já existe"
        return

    todos.append(todo)
    functions.write_todos(todos, filename="todos.txt")

    st.session_state["new_todo"] = ""
    st.session_state["todo_error"] = ""

st.title("Anote seus afazeres!")
st.subheader("- Artoo")
st.write("Esse é um web app para te ajudar com a organização pessoal")

for index,todo in enumerate(todos):
    check = st.checkbox(todo,key=todo)
    if check:
        todos.pop(index)
        del st.session_state[todo]
        functions.write_todos(todos, filename="todos.txt")
        st.rerun()

with st.form(key="todo_form"):
    st.text_input(
        label="Adicione uma tarefa:",
        placeholder="Digite uma nova tarefa...",
        key="new_todo"
    )
    st.form_submit_button("Add", on_click=add_todo)

if st.session_state.get("todo_error"):
    st.warning(st.session_state["todo_error"])

st.session_state

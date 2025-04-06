from fastapi import FastAPI, HTTPException

api = FastAPI()

all_todos = [
    {'todos_id': 1, 'title': 'Buy groceries', 'todo_description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'completed': False},
    {'todos_id': 2, 'title': 'Learn Python', 'todo_description': 'Need to find a good Python tutorial on the web', 'completed': False},
    {'todos_id': 3, 'title': 'Learn FastAPI', 'todo_description': 'Need to find a good FastAPI tutorial on the web', 'completed': False},
    {'todos_id': 4, 'title': 'Learn Django', 'todo_description': 'Need to find a good Django tutorial on the web', 'completed': False},
    {'todos_id': 5, 'title': 'Learn Flask', 'todo_description': 'Need to find a good Flask tutorial on the web', 'completed': False},
]

@api.get('/')
def index():
    return {"message": "Welcome to the Todo API" }

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    todo = next((todo for todo in all_todos if todo['todos_id'] == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {'result': todo}

@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        if first_n > len(all_todos):
            raise HTTPException(status_code=400)
        return all_todos[:first_n]
    return all_todos


@api.post('/todos')
def create_todo(todo: dict):
    new_todo = {
        'todos_id': len(all_todos) + 1,
        'title': todo['title'],
        'todo_description': todo['todo_description'],
        'completed': False
    }
    all_todos.append(new_todo)
    return {'result': new_todo}

@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo:dict):
    for todo in all_todos:
        if todo['todos_id'] == todo_id:
            todo['title'] = updated_todo['title']
            todo['todo_description'] = updated_todo['todo_description']
            todo['completed'] = updated_todo['completed']
            return {'result': todo}
        
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    global all_todos
    all_todos = [todo for todo in all_todos if todo['todos_id'] != todo_id]
    return {'result': 'Todo deleted successfully'}

#time stamp 36:00
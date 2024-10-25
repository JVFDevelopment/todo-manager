import json
import os

class TodoListManager:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.todos = json.load(file)
        else:
            self.todos = []

    def save_todos(self):
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file)

    def add_todo(self, item):
        self.todos.append(item)
        self.save_todos()
        print(f'Todo added: "{item}"')

    def list_todos(self):
        if not self.todos:
            print("No todo items found.")
        else:
            for idx, item in enumerate(self.todos, start=1):
                print(f"{idx}. {item}")

    def mark_done(self, index):
        try:
            removed_item = self.todos.pop(index - 1)
            self.save_todos()
            print(f'Todo marked as done: "{removed_item}"')
        except IndexError:
            print("Invalid todo item number.")

    def delete_todo(self, index):
        """Delete a todo item."""
        try:
            removed_item = self.todos.pop(index - 1)
            self.save_todos()
            print(f'Todo deleted: "{removed_item}"')
        except IndexError:
            print("Invalid todo item number.")

def main():
    todo_manager = TodoListManager()

    while True:
        print("\nTodo List Manager")
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Mark Todo as Done")
        print("4. Delete Todo")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            item = input("Enter todo item: ")
            todo_manager.add_todo(item)
        elif choice == '2':
            todo_manager.list_todos()
        elif choice == '3':
            index = int(input("Enter todo item number to mark as done: "))
            todo_manager.mark_done(index)
        elif choice == '4':
            index = int(input("Enter todo item number to delete: "))
            todo_manager.delete_todo(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()

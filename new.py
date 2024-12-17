class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        print("Your tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number > 0 and task_number <= len(self.tasks):
                task = self.tasks.pop(task_number - 1)
                print(f"Task '{task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid task number!")

def main():
    todo = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = input("Enter the task number to delete: ")
            todo.delete_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "_main_":
    main()
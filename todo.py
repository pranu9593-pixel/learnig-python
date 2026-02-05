
tasks = []
while True:
    task = input("Add task (or 'quit'): ")
    if task.lower() == 'quit':
        break
    tasks.append(task)
print("Your tasks:", tasks)

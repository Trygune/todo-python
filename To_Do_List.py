import my_menu

tdl = my_menu.ToDoList()


def input_task():
    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority: ")
    return my_menu.Task(title, description, priority)


if __name__ == "__main__":
    tdl.load_file()
    print("Welcome".center(20))
    actions = "*Add\n*Remove\n*See All Tasks\n*Save"
    while True:
        print(actions)
        a = input("Choose your Action: ")
        print()
        if a.lower() in ["add", "a"]:
            tsk = input_task()
            tdl.add_task(tsk)
        elif a.lower() in ["remove", "r"]:
            rem_title = input("Title: ")
            tdl.rem_task(rem_title)
            tdl.save_file()
        elif a.lower() in ["see all tasks", "see"]:
            tdl.show_task()
        elif a.lower() in ["save", "s"]:
            tdl.save_file()
        else:
            print(" Command Not Definede!")
            break

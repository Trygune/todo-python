import csv


class Task:
    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority

    def save_csv(self):
        dik = {
            "Title": self.title,
            "Description": self.description,
            "Priority": self.priority or "medium",
        }
        return dik

    @staticmethod
    def load_csv(data):
        return Task(
            title=data.get("Title"),
            description=data.get("Description"),
            priority=data.get("Priority") or "medium",
        )


class ToDoList:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"'{task.title}' added\n")

    def rem_task(self, name):
        for task in self.tasks:
            if name == task.title:
                print(f"'{name}' removed\n")
                self.tasks.remove(task)
                return
        print("not found!\n")

    def show_task(self):
        if not self.tasks:
            print("list is empty!")
        else:
            print("To Do List:")
            for i, title in enumerate(self.tasks, start=1):
                print(
                    f"{i}. {title.title} - {title.description} (priority: {title.priority})"
                )
        print()

    def save_file(self):
        data = open("./Projects/Final/data.csv", mode="w", newline="")
        my_csv_write = csv.DictWriter(
            data, fieldnames=["Title", "Description", "Priority"]
        )
        my_csv_write.writeheader()
        for task in self.tasks:
            my_csv_write.writerow(task.save_csv())
        data.close()
        print("File Saved!\n")

    def load_file(self):
        try:
            with open("./Projects/Final/data.csv", mode="r") as data:
                my_csv = csv.DictReader(data)
                for i in my_csv:
                    self.tasks.append(Task.load_csv(i))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("this is just a package")

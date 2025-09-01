from pathlib import Path


tasks=[]

workspace = Path("To_do_list")
workspace.mkdir(exist_ok=True)
file_name = workspace / "to_do.txt"

def add_task(task):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"\n{task}")
        # tasks.append(task)
        f.close
    print(tasks)

def remove_task(task):
    with open(file_name, "x", encoding= "utf -8" ) as t:
        for line in task:
            line = line.replace(line, "")
            t.write(line)


        # tasks.remove(task)
    print(tasks)

def view_task():
    print(tasks)
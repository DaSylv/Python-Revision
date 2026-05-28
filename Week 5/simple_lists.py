def directions():
    steps = ["Move Forward","Move Backward","Move Right","Move Left"]
    return steps
def run_task1():
    nav_steps = directions()
    print(nav_steps)
if __name__ == "__main__":
    run_task1()

def movements():
    path = ["Move Forward",10, "Move Backward",5, "Move Left",3,"Move Right",1]
    return path

def run_task2():
    print("Moving...")
    path = movements()
    for i in range(0, len(path),2):
        direction = path[i]
        steps = path[i+1]
        print(f" {direction} for {steps} steps")

if __name__ == "__main__":
    run_task2()
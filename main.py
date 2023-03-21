import time
import queue
from datetime import datetime
from multiprocessing import Process, Queue, Lock, current_process

def hi(name):
    print("hi! I'm process ", name)

def sum_job(tasks_to_accomplish, tasks_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:
            break
        else:
            print(task)
            tasks_done.put(
                current_process().name + " concluiu a "+ task + "\n    em: " + str(datetime.now())
            )
            time.sleep(.5)
    return True

def create_tasks(tasks_to_accomplish, n_tasks):
    for i in range(n_tasks):
        task_id = 'Tarefa-' + str(i+1)
        tasks_to_accomplish.put(task_id)

def create_process(list_of_process, n_process, tasks_to_accomplish, tasks_done):
    for i in range(n_process):
        #process_text = "process ", i+1
        print("creating process... ", i+1)
        list_of_process.append(
            Process(target=sum_job, args=(tasks_to_accomplish, tasks_done))
        )
        list_of_process[i].start()

def main():

    list_of_process = []
    n_process = 5
    n_tasks = 10
    tasks_to_accomplish = Queue()
    tasks_done = Queue()

    create_process(list_of_process, n_process, tasks_to_accomplish, tasks_done)
    create_tasks(tasks_to_accomplish, n_tasks)
    
    for p in list_of_process:
        p.join()

    while not tasks_done.empty():
        print(tasks_done.get())
    
if __name__ == '__main__':
    main()

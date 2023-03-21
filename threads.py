import threading
from threading import Thread

class CustomThread(Thread):
    def __init__(self, value,name):
        Thread.__init__(self)
        self.value = int(value)
        self.name = name
        print("CustomThread.value", self.value)

    def funcao_especifica(self, func):
        print(func, " ", self.name)
        

def hi(name):
    print("hi! I'm thread ", name)

def store_value(value):
    meus_dados = threading.local()
    meus_dados.val = value

def sum_threads():
    return

def create_tasks(n_tarefas):
    for i in range(n_tarefas):
        task_id = 'Tarefa-' + str(i+1)

def create_threads(n_threads, lista_de_threads):
    
    for i in range(n_threads):
        print("Criando Thread" , i+1, "...")
        lista_de_threads.append(
            CustomThread(
                i+1,
                name="Thread "+str(i+1)
            )
            #Thread(target=hi("t" + str(i+1), i+1))
            #Thread(
            #    target=hi(i+1),
            #    name='Tarefa-' + str(i+1)
            #)
        )
        CustomThread.funcao_especifica(CustomThread, "hi")
        #lista_de_threads[i].run()

        #print(lista_de_threads[i])

        #thread_atual = threading.current_thread()
        #n_threads_ativas = threading.active_count()
        #print(threading.active_count())
        #print(threading.current_thread())
        #print("My Universal ID is: " + str(threading.get_native_id()))

def elege_lider(lista_de_threads):
    main_thread = threading.main_thread()
    main_thread = lista_de_threads[-1]
    thread_atual = threading.current_thread()
    thread_atual = lista_de_threads[-1]
    print("Eu sou o lider" , main_thread)
    print(thread_atual)

def main():
    n_threads = 5
    n_tarefas = 10
    lista_de_threads = []

    create_threads(n_threads, lista_de_threads)
    #t1=Thread(target=hi("tarefa"), name="tarefa")
    #t1.run()
    #print(t1.getName())
    #create_tasks(n_tarefas)
    #elege_lider(lista_de_threads)

if __name__ == '__main__':
    main()
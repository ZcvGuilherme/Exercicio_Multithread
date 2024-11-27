import multiprocessing
import os 
from time import sleep
#processo = multiprocessing.Process(target=funcaofilho, args=(i,))
#os.getpid()
#CRIAR PROCESSO PAI
#PROCESSO PAI CRIA 3 FILHOS
#PROCESSO FILHO CALCULA EXPONENCIAÇÃO   
def funcaofilho(numero):
    pid = os.getpid()
    ppid = os.getppid()
    result = numero ** 2
    print(f"Processo filho iniciado. PID: {pid}, PPID: {ppid}, tarefa: {numero} ** 2 = {result}")
    sleep(2)
    print(f"Processo filho finalizado. PID: {pid}")
#MultiThread
def main():
    #Função principal
    #PID = Process ID
    print(f"Processo pai iniciado: PID: {os.getpid()}")
    sleep(1)
    processos = []
    numProcessos = 3
    for i in range(1, numProcessos + 1):
        processo = multiprocessing.Process(target=funcaofilho, args=(i,))
        processos.append(processo)

        sleep(1)
        processo.start()
        print(f"processo filho criado com sucesso! PID: {processo.pid}")
        print(f"Processo {processo.pid} em execução")
        sleep(1)

    for processo in processos:
        processo.join()
        
    print("Todos os processos filho foram finalizados...")
    print(f"Processo pai sendo finalizado... PID {os.getpid()}")
    sleep(1)
    




if __name__ == "__main__":
    main()
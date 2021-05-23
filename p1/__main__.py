from .loader.loader import Loader
from .dumper.dumper import Dumper
from .memory import Memory

def main():
    loader = Loader()
    dumper = Dumper()

    memory = Memory(4096)

    general_user_msg = """\nDentre as seguintes opções:\n
    l - Para fazer load de um arquivo
    d - Para fazer dump da memória
    z - Para zerar o conteúdo da memória
    i - Para imprimir o conteúdo da memória
    s - Para sair\n"""

    avaible_options = ["l", "d", "z", "i", "s"]

    stop = False

    try:
        while not stop:
            print(general_user_msg)
            option = input("Qual delas deseja executar? ")

            if option not in avaible_options:
                print("Opção inválida, escolha outra\n\n")
            else:
                if option == "l":
                    file_name = input("Qual o nome do arquivo a ser carregado? ")

                    loader.run(file_name, memory)
                elif option == "d":
                    file_name = input("Qual o nome do arquivo no qual fazer o dump? ")
                    start_position = int(input("Qual a posição inicial da memória para fazer o dump? "), 16)
                    end_position = int(input("Qual a posição final da memória para fazer o dump? "), 16)

                    dumper.run(file_name, memory, start_position, end_position)
                elif option == "z":
                    memory.clear()

                    print("Memória zerada\n")
                elif option == "i":
                    memory.display()

                    print("Dados da memória disponíveis no arquivo image.txt\n")
                else:
                    stop = True
    except KeyboardInterrupt:
        print("[INFO] Ending Program")


if __name__ == '__main__':
    main()

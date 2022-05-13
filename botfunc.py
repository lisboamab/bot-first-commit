def abrirPrograma(programa: str) -> None:    
    from pyautogui import click, write, press, PAUSE

    PAUSE = 2

    # abrir o programa
    press("win")
    write(programa)
    press("enter")

    return None

def siteDesejado(site: str) -> None:
    from pyautogui import click, write, press

teste = 1

while True:
    teste = input("Digite o nome do programa que quer abrir: ")
    if teste != '0':
        abrirPrograma(teste)
    else:
        print("Programa encerrando")
        break
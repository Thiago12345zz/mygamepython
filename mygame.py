import random 
from colorama import Fore, init

#Windown
init() 

colors = {
    'yellow':Fore.YELLOW,
    'blue':Fore.BLUE,
    'green':Fore.GREEN,
    'orange':Fore.LIGHTRED_EX,
    'reset':Fore.RESET
}
def boneco_display(chances):
    boneco = [
           """
            ______________
            |            |
            |            O
            |       ____________
            |           \\|/
            |            |
            |           / \\
            |
            | 
            """,
            """
            ______________
            |            |
            |            O
            |           \\|/
            |            |
            |           / \\
            |
            | 
            """,
            """
            ______________
            |            |
            |            O
            |           \\|/
            |            |
            |           / 
            |
            | 
            """,
            """
            ______________
            |            |
            |            O
            |           \\|/
            |            |
            |
            |
            | 
            """,
            #2
            """
            ______________
            |            |
            |            O
            |            |
            |            |
            |
            |
            | 
            """,
            """
            ______________
            |            |
            |            O
            |            
            |
            |
            |
            |
            """,
                     """
            ______________
            |            |
            |            
            |            
            |
            |
            |
            |
            """]
    return boneco[chances]
def game():
    
    print(f'{colors['yellow']}Bem vindo ao jogo da forca{colors["reset"]}')
    print('Tente adivinhar a palavra abaixo:')
    
    #lista de palavras do jogo
    palavras = ['morango','uva','pessego','laranja']
    palavra = random.choice(palavras)
    
    letras_descobertas = ['_' for letra in palavra]
    
    chances = 6
    
    letras_erradas = []
    
    while chances > 0:
        print(boneco_display(chances))
        print(" ".join(letras_descobertas))
        print(f'{colors["orange"]}Chances restantes:{colors["reset"]}',chances)
        print(f'{colors["yellow"]}letras_erradas{colors["reset"]}','_'.join(letras_erradas))
        
        tentativa = input('\nDigite uma letra: ').lower()
        if tentativa in palavra:
            index=0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1
        else:
            chances -=1
            letras_erradas.append(tentativa)
            
        if '_' not in letras_descobertas:
            print(f'{colors["green"]}Você ganhou, a palavra era:{colors["reset"]}',f'{colors["yellow"]}{palavra}{colors["reset"]}')
            
            break  
            
    if '_' in letras_descobertas:
        print(f"{colors['orange']}""""
            ______________
            |            |
            |            O
            |       ____________
            |           \\|/
            |            |
            |           / \\
            |
            | 
            """f"{colors['reset']}")
        print(f'{colors["orange"]}Você Perdeu, a palavra era:{colors["reset"]}',palavra)

game()
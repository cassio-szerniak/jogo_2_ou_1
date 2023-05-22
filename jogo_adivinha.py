# JOGOS DE ADIVINHAÇÃO
# TENTE ADIVINHAR O NUMERO

import random  # AQUI IMPORTAMOS O METODO RANDOM, QUE GERA UM NUMERO ALEATORIO
from random import randint  # AQUI IMPORTAMOS O METODO RANDINT, QUE GERA UM NUMERO ALEATORIO INTEIRO

def jogo_adivinha():
    
    print('---------------------------------------------')
    print('               JOGO ADIVINHA 🧐')
    print('---------------------------------------------')
    repita = True
    while repita == True: 
        try:
            numero = random.randint(1, 10)
            tentativa = 1
            chutes = 5
            while tentativa < 6:
                print(f"\n------ VOCÊ TEM {chutes} TENTATIVAS ------\n")
                chute = int(input("\nDIGITE UM NÚMERO ---> "))
                if 10 >= chute >= 1:
                    if chute == numero:
                        print("\n✅ Número: ", numero,"--> Você acertou no ", tentativa, "º chute válido!\n")
                        print("🎈🥳 PARABÉNS, VOCÊ VENCEU! 🥳🎈\n")
                        tentar = input("JOGAR DE NOVO? [1-SIM/ 0-NÃO]: ")
                        if tentar == "1":
                            numero = random.randint(1, 10)
                            tentativa = 1
                            chutes = 5
                            repita = True
                        else:
                            repita = False
                            break
                    else:
                        print("Errou! \n")
                        tentativa += 1
                        chutes -= 1
                        if tentativa > 5:
                            print("\n🛑↓ G A M E  O V E R ↓🛑 \n")
                            tentar = input("TENTAR DE NOVO? [1-SIM/ 0-NÃO]: ")
                            if tentar == "1":
                                numero = random.randint(1, 10)
                                tentativa = 1
                                chutes = 5
                                repita = True
                            else:
                                repita = False
                                break
                else:
                    print("\nSéloko caxuêra? Tem que ser um número entre 1 e 10.\n")
                    print("Vai lá, tô torcendo. 😉\n")
                    continue
        except:
            print("\n--> Formato inválido! Deve ser um número inteiro, entre 1 e 10. \n")
            continue

def jogo_dois_ou_um():

    repita = True
    while repita == True: 
        # ↓ AQUI USAMOS O TRATAMENTO DE EXCEÇÃO "TRY/EXCEPT" PARA O CASO DE O USUARIO DIGITAR UM CARACTERE INVÁLIDO
        # SE FOR O CASO O EXCEPT MOSTRARÁ UMA MENSAGEM DE ERRO E REPETIRÁ O PROGRAMA
        try:
            print('---------------------------------------------')
            print('               JOGO ✌ ou ☝ ? ')
            print('---------------------------------------------')
            # AQUI ↓ A VARIAVEL QUE DEVERÁ SER ADIVINHADA RECEBE UM NUMERO ALEATORIO ENTRE 1 OU 2, USANDO O METODO RANDINT
            numero = random.randint(1, 2)
            # ↓ AQUI A VARIAVEL CHUTE RECEBERÁ O NÚMERO QUE O USUARIO DIGITAR, CASO DIGITE ALGO INVÁLIDO, SALTARÁ PARA O EXCEPT
            chute = int(input("\n❓ DOIS OU UM ❓ ---> "))
            # PODERÍAMOS FORÇAR PARA INT PARA PODER CRIAR UMA CONDIÇÃO LOGICA ASSIM: chute = int(chute), MAS COMO ESTAMOS UTILIZANDO O METODO TRY/EXCEPT, ELE JÁ FAZ A VALIDAÇÃO
            
            # ↓ AQUI A CONDIÇÃO LERÁ SE O CHUTE RESPEITA AS OPÇÕES
            if chute != 1 and chute != 2:
                print("\n➡Séloko caxuêra? Tem que ser o número 1 ou 2.\n")
                print("➡Vai lá, tô torcendo. 😉\n")
                continue

            # ↓ AQUI CRIAMOS A CONDIÇÃO QUE LERÁ SE O USUÁRIO ACERTOU OU ERROU O CHUTE
            if chute == numero:
                print("Número: ", numero,"\n Seu chute: ", chute, "\n")
                print("🥳 PARABÉNS, VOCÊ ACERTOU! 🥳\n")
                # ↓ AQUI A RESPOSTA DO USUARIO DEFINIRÁ SE O LAÇO DO JOGO SE REPETIRÁ OU NÃO
                repita = input("QUER JOGAR DE NOVO? [1-SIM/2-NÃO]: ")
                # RECEBENDO O DADO COMO STRING, QUALQUER RESPOSTA QUE NÃO SEJA O "1" ACIONARÁ O "ELSE" 
                if repita == "1":
                    repita = True
                else:
                    repita = False
            else:
                print("Número: ", numero,"\n Seu chute: ", chute, "\n")
                print('❌ Que azar! Como diria Raul Seixas: "Tente outra vez! 💪"\n')
                # ↓ AQUI A RESPOSTA DO USUARIO DEFINIRÁ SE O LAÇO DO JOGO SE REPETIRÁ OU NÃO
                repita = input("QUER JOGAR DE NOVO? [1-SIM/ 0-NÃO]: ")
                # RECEBENDO O DADO COMO STRING, QUALQUER RESPOSTA QUE NÃO SEJA O "1" ACIONARÁ O "ELSE" 
                if repita == "1":
                    repita = True
                else:
                    repita = False

        except:
            print("\n--> Formato inválido! Deve ser um número inteiro, entre 1 e 2. \n")
            repita = True
    
def menu():
    # ABAIXO TEMOS A CONDIÇÃO WHILE PARA QUE O JOGO SÓ PARE DE 
    # SER EXECUTADO QUANDO O USUARIO ESCOLHER A OPÇÃO "SAIR", QUE ACIONA O BREAK
    while True:
        # IMPRESSÃO DO MENU ↓
        print("\nO que você quer fazer? \n")
        print('1 - JOGAR 2 OU 1 🎮')
        print('2 - JOGAR ADIVINHE DE 1 A 10 🎮')
        print('0 - SAIR DO JOGO 🚪')
        # AQUI ↓ A VARIAVEL RECEBE O INPUT DO USUARIO
        jogar = input('--------------------------> ')
        # ↓ CASO A RESPOSTA SEJA VALIDA, TRANSFORMAMOS A VARIÁVEL STRING EM INTEIRO PARA CRIAR UMA CONDIÇÃO LOGICA
        jogar = int(jogar)
        
        # ABAIXO, A CONDIÇÃO 'IF' FAZ UMA VALIDAÇÃO PARA A RESPOSTA DO USUARIO,
        # CASO ELE DIGITE UMA OPÇÃO INVALIDA, O JOGO NÃO É EXECUTADO, E APARECE UMA MSG DE ERRO
        if jogar == 1 or jogar == 2 or jogar == 0:
            if jogar == 1:
                jogo_dois_ou_um()

            elif jogar == 2:
                jogo_adivinha()
                
            else:
                print('Saindo do jogo...\n')
                print("Até a próxima! 🙋‍♂️")
                break
        else:
            print("\nOpção inválida! Tente novamente!\n")

menu()



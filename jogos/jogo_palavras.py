# jogo_palabras.py
# Jogo de Palabras.
# Descricao: Script de consola para jogo de palavras.

import random
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def carregar_palavras(nome_arquivo="palavras_pt.txt"):
    base = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base, nome_arquivo)

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
        return palavras
    except FileNotFoundError:
        print("Arquivo não encontrado, usando palavras padrão...")
        return ["python", "perfume", "brasil", "mexico", "mundo", "borboleta", 
        "computador", "teclado", "monitor", "internet", "telefone", "mensagem"]

palavras = carregar_palavras()

def jogar():
    palavra_secreta = random.choice(palavras)
    estado_atual = ["*"] * len(palavra_secreta)   
    tentativas = 0                                
    letras_digitadas = []                         

    print("Bem-vindo ao jogo da palavra secreta!")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    print(" ".join(estado_atual))

    while "*" in estado_atual:
        

        print("\n-----------------------------------")
        print(" ".join(estado_atual))
        print("Letras já digitadas:", ", ".join(letras_digitadas))
        letra = input("Digite uma letra: ").lower().strip()
        
          
        if len(letra) != 1:
            print("⚠️ Digite apenas uma letra!")
            continue

        if letra.isnumeric():
            print("⚠️ Digite apenas letras, não números!")
            continue

        if letra in letras_digitadas:
            print(f"⚠️ Você já digitou a letra '{letra}'. Tente outra.")
            continue

        letras_digitadas.append(letra)
        tentativas += 1

        if letra in palavra_secreta:
            print(f"✅ Boa! A letra '{letra}' está na palavra!")
            
            for i, letra_palavra in enumerate(palavra_secreta):
                if letra_palavra == letra:
                    estado_atual[i] = letra
        else:
            print(f"❌ A letra '{letra}' não está na palavra.")

    clear_screen()
    print("🎉 PARABÉNS! 🎉")
    print(f"Você descobriu a palavra '{palavra_secreta}' em {tentativas} tentativas!")

if __name__ == "__main__":
    while True:
        jogar()
        seguir = input("\nQuer continuar? (s/n): ").lower()
        if seguir != "s":
            print("Até logo!")
            break
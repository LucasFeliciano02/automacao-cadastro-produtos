import pyautogui  # Automatiza movimento do mouse e do teclado e digitacao
from time import sleep
from mouseinfo import mouseInfo

# pip install pyautogui pillow mouseinfo
# mouseInfo()

# 1 - Clicar e digitar usuário
pyautogui.click(972, 540, duration=1)
pyautogui.write('Lucas')

# 2 - Clicar e digitar a senha
pyautogui.click(974, 568, duration=0.5)
pyautogui.write('12345')

# 3 - Clicar em no botão "Entrar"
pyautogui.click(866, 594, duration=0.5)

# 4 - Extrair produtos e inserir no sistema
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:  # divide cada tipo de item do arquivo txt encontrar uma ,
        produto = linha.split(',')[0]  
        qtd = linha.split(',')[1] 
        preco = linha.split(',')[2] 

        # 1 - Clicar e digitar produto
        pyautogui.click(683, 528, duration=0.5)
        pyautogui.write(produto) 
        
        # 2 - Clicar e digitar quantidade
        pyautogui.click(686, 555, duration=0.5)
        pyautogui.write(qtd) 
        
        # 3 - Clicar e digitar preço
        pyautogui.click(684, 580, duration=0.5)
        pyautogui.write(preco) 
        
        # 4 - Clicar no botão "Registrar"
        pyautogui.click(595, 737, duration=0.5)

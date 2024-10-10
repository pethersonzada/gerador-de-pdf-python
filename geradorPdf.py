# Importando as bibliotecas.

import os # Criar pastas.
from reportlab.pdfgen import canvas # Gerador de PDF.
from reportlab.lib.pagesizes import A4 # Configuração de tamanho de página.
from reportlab.pdfbase.ttfonts import TTFont # Fontes.

os.makedirs("projetos-python/python-gerador-pdf", exist_ok=True) # Cria a pasta para o PDF, mas se a pasta já existir, não cria nada.

nome = input("Nome do funcionário (Apenas primeiro nome) : ") # Input para pegar o nome do funcionário.
quantidade_de_vendas = int(input("Quantidade de vendas: ")) # Input para pegar a quantidade de vendas do funcionário.

def avaliar_funcionario(quantidade_de_vendas): # Função para avaliar o rendimento do funcionário.
    if quantidade_de_vendas >= 25:
        return "Sim!"
    elif quantidade_de_vendas < 25:
        return"Não, mínimo de 25 vendas."

avaliacao = avaliar_funcionario(quantidade_de_vendas)

def mm2p(milimetros): # Função para converter milimetros em polegadas.
    return milimetros / 0.352777

cnv = canvas.Canvas("projetos-python/python-gerador-pdf/Meu primeiro Pdf.pdf") # Cria o PDF.
cnv.drawImage("projetos-python/python-gerador-pdf/plano-de-fundo.png", 0, 0, width=A4[0], height=A4[1]) # Insere o plano de fundo do PDF.

cnv.drawString(mm2p(153), mm2p(242.1), nome) # Insere o nome do funcionário no PDF.
cnv.drawString(mm2p(156), mm2p(180), str(quantidade_de_vendas)) # Insere a quantidade de vendas do funcionário no PDF.

if avaliacao == "Sim!": # Se o valor for maior ou igual a 25, insira isso.
    cnv.drawString(mm2p(156), mm2p(120), str(avaliacao)) # Insere o rendimento do funcionário no PDF.
elif avaliacao == "Não, mínimo de 25 vendas.": # Se o valor for menor que 25, insira isso.
    cnv.drawString(mm2p(135.2), mm2p(120), str(avaliacao)) # Insere o rendimento do funcionário no PDF.

cnv.save() # Salva o PDF com todos os parâmetros acima
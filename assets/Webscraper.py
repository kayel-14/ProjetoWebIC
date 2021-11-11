import bs4
import time
from _datetime import datetime
import requests
import pygame
from bs4 import BeautifulSoup as Soup

def Sprice(url):
   r = requests.get(url)
   soup = bs4.BeautifulSoup(r.text, "html.parser")
   p = soup.find_all('div', {'class': 'value'})[0].text
   A = p[1:6].replace(',', '.')
   A = A.replace('Re', '')
   price = float(A)
   print(price)
   return price
def Name(name):
   font = pygame.font.SysFont("Times New Roman, Arial", 20)
   Text = font.render( name, True, (0, 0, 0))
   return Text
def Pname(text, width, height):
   return window.blit( text, (width, height))

#===============================

try:
   pygame.init()
except:
   print('ERROR')

#===============================

height = 580
width = 340
print(datetime.hour)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stocks")
window.fill((255, 255, 255))
clock = pygame.time.Clock()
fps = 30
on = True
k = 1000

#===============================

Text0 = Name("Net Worth: ")
Pname(Text0, 125, 100)
Text1 = Name("Engie: ")
Pname(Text1, 140, 160)
Text2 = Name("Fleury: ")
Pname(Text2, 138, 220)
Text3 = Name("Ambev: ")
Pname(Text3, 136, 280)
Text4 = Name("Itaúsa: ")
Pname(Text4, 137, 340)
Text5 = Name("Magalu: ")
Pname(Text5, 137, 400)
Text6 = Name("EnergBr: ")
Pname(Text6, 130, 460)
Text7 = Name("Previsão: ")
Pname(Text7, 128, 520)

#===============================

P_engie = Sprice('https://www.infomoney.com.br/cotacoes/engie-brasil-egie3/grafico/')
P_fleury = Sprice("https://www.infomoney.com.br/cotacoes/fleury-flry3/")
P_ambev = Sprice("https://www.infomoney.com.br/cotacoes/ambev-abev3/")
P_itausa = Sprice("https://www.infomoney.com.br/cotacoes/itausa-itsa4/grafico/")
P_Magalu = Sprice("https://www.infomoney.com.br/cotacoes/magazine-luiza-mglu3/grafico/")
P_Enbr = Sprice("https://www.infomoney.com.br/cotacoes/energias-br-enbr3/grafico/")

#===============================

Net_Worth = P_engie * 2 + P_fleury * 11 + P_ambev * 4 + P_itausa * 9 + P_Enbr * 5 + P_Magalu * 10
Pre = Net_Worth * (1.1)
pre5 = Pre * (1.1)**4

#===============================

Text00,Text10, Text20, Text30, Text40, Text50, Text60, Text70, Text80 = Name(str("%.2f" % Net_Worth)), Name(str(P_engie)), Name(str(P_fleury)), Name(str(P_ambev)), Name(str(P_itausa)), Name(str(P_Magalu)), Name(str(P_Enbr)), Name(str("%.2f" % Pre)), Name(str("%.2f" % pre5))

Pname(Text00, 128, 130)
Pname(Text10, 141, 190)
Pname(Text20, 140, 250)
Pname(Text30, 140, 310)
Pname(Text40, 145, 370)
Pname(Text50, 140, 430)
Pname(Text60, 140, 490)
Pname(Text70, 100, 550)
Pname(Text80, 170, 550)
#===============================
while on:

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False


   pygame.display.update()

pygame.quit()






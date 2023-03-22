print("Olá,bem-vindo(a) ao cérebro:hemisfério direito") 
print("Vamos começar,as seguinte variáveis irão ser demonstradas,pressione ''Enter'':")      
input(">Arte,3D e criatividade: ")

if input :"Arte"
print(">Os neurocientistas afirmam que a arte provoca alterações nos padrões das ondas e do ritmo cerebral, bem como estimula o nosso sistema límbico,provocando emoções->ex->Poema:''É sempre mais difícil ancorar um navio no espaço''-(Ana Cristina César)")

input("A seguir,será desenhado uma figura que representa como nosso cérebro processa um objeto tridimensional,quando estiver pronto(a)digite ''Enter''")
print("Exemplo de figura 3D processada pelo nosso cérebro:")

import turtle  
tut = turtle.Screen() 
tut.bgcolor("green") 
tut.title("Turtle") 
my_pen = turtle.Turtle() 
my_pen.color("orange") 
tut = turtle.Screen()            
for i in range(4): 
    my_pen.forward(100) 
    my_pen.left(90) 
my_pen.goto(50,50) 
for i in range(4): 
    my_pen.forward(100) 
    my_pen.left(90) 
my_pen.goto(150,50) 
my_pen.goto(100,0) 
my_pen.goto(100,100) 
my_pen.goto(150,150) 
my_pen.goto(50,150) 
my_pen.goto(0,100)


input("Agora será mostrado um exemplo de como o cérepro processa a criatividade,aperte ''Enter'' para prosseguir")
from random import choice
import string
print(">o pensamento criativo ocorre sobretudo no interior de redes neurais,combinando e organizando conceitos que se sabia anteriormente.Por exemplo,a criação de um nova palavra,o programa simulará as redes cerebrais e o produto final:")
tamanho = input("Qual será o tamanho da sua nova palavra?(quantos digitos?): ")
tamanho = int(tamanho)
valores = string.ascii_letters 
palavra = ''
for i in range(tamanho):
    palavra += choice(valores)

print("Aqui está a sua nova palavra!: " + palavra)

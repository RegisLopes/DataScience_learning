#Curso Python para Machine Learning e Análise de Dados

#tupla é uma lista que nao pode ser alterada, ocupam menos memória e sao mais rápidas e mais seguras do que listas.

def exe1():
#Exercício 1 (Aula3)   
  x_i=[]
  a=0
  
  b=int(input("Tamanho da lista: "))
  #print(type(x),type(a),type(b))

  while a<b:
    c=int(input("Item: "))
    x_i.append(c)
    a+=1

  x_f=[float(i) for i in x_i]
    
    
  print("{%}----->{%}".format(x_i,x_f))

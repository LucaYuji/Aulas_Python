# Acessando um sub-módulo
import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abre', 'Mai', 'Jun']
vendas = [1000,2000,3000,4000,5000,1500]

# rotulo dos eixos
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas Mensais')
# plt.grid(True)
# x, y
# graf = plt.plot(meses, vendas, marker='o', linestyle=':', color='green') linha
# graf = plt.bar(meses, vendas, edgecolor='black', color='green') barra
plt.scatter(meses, vendas) #pontos, dispersão
plt.pie(vendas, labels=meses, autopct='%1.1f%%')

# Executando matplotlib
plt.show()
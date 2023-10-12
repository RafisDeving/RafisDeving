listaprodutos = ["iphone", "ipad", "computador"]
dinheirovendas = 10000

if dinheirovendas > 5000:
    print('Você alcançou a meta')
elif dinheirovendas < 0:
    print('Erro')
else:
    print('Você não alcançou a meta')
for produto in listaprodutos:
    print(produto)
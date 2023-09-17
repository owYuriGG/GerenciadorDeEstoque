from utilits import clear
from datetime import datetime

def sell_product(stock, sales_control): #Função para vender um produto
    """
    Função utilizada para vender um produto
    recebendo por parâmetro o estoque e o controle de vendas
    """
    product = str(input("Digite o nome do produto: "))

    #Verificação se o produto existe
    if product not in stock:
        clear()
        print("Este produto não existem em seu estoque!")

    #Se houver produto em estoque, ele verifica a quantia a ser vendida
    elif product in stock:
        amount = int(input("Qual a quantia a ser vendida? "))

        #Após solicitar a quantia, ele verifica se há estoque o suficiente para realizar a venda
        if stock[product]['amount'] < amount:
            clear()
            print("Estoque insuficiente!")
            return stock, sales_control
        
        #Se houver estoque suficiente, ele realiza a venda, diminuindo a quantia em estoque
        #calcula o preço, e adiciona ao relatório de vendas,
        else:
            clear()
            stock[product]['amount'] -= amount
            sale_price = amount * stock[product]['price']

            #Adição do horário ao controle de vendas, utilizando da bibliotéca datetime, com o método now()
            date = datetime.now()
            #Aqui é utilizado a classe 'date', nativa do python, para formatação de datas, usando o método strftime()
            date_formated = date.strftime('%d/%m/%Y às %H:%M')
            sales_control.append(f"Venda -->  {amount} {product} vendido(s) por R${sale_price} na seguinte data: {date_formated}")
            print(f"Venda realizada com sucesso! Valor da venda: R${sale_price}, quantia vendida: {amount} {product}")
            return stock, sales_control
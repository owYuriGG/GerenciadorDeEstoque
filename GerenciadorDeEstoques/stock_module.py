from utilits import clear

def add_product(stock, changes_historic):
    """
    Função para adicionar produto ao estoque,
    recebendo como parâmetros o estoque e o histórico de alterações
    """
    product = str(input("Digite o nome do produto: "))
    amount = int(input("Digite a quantia de unidades do produto: "))
    #Verifica se o produto já existe em estoque e soma as unidades caso ele já esteja
    if product in stock:
        clear()
        print("Este produto já está cadastrado em estoque! Somando estoque...")
        #Aqui o código soma o estoque e já adiciona o mesmo ao histórico de alterações
        changes_historic.append(f"Foi somado {amount} unidades ao estoque do produto '{product}'.")
        stock[product]['amount'] += amount
        return stock, changes_historic
    else:   
        #Caso o produto não esteja em estoque, ele continua com as perguntas e cria o mesmo
        price = float(input("Digite o preço de venda do produto: "))
        category = str(input("Digite a categoria do produto: "))
        #Tendo as informações do produto, ele adiciona ao estoque. E após, adiciona ao histórico de alterações à adição
        stock[product] = {
            'amount' : amount,
            'price' : price,
            'price_historic' : [f"R${price}"],
            'category' : category
        }
        changes_historic.append(f"O produto '{product}' foi adicionado ao estoque com {amount} unidades.")
        clear()
        print("Produto adicionado com sucesso!")
        return stock, changes_historic


def search_product(stock, sales_control):
    """
    Função para buscar um produto no estoque e mostrar suas informações
    recebendo por parâmetros o estoque e o controle de vendas
    """
    product = str(input("Digite o nome do produto a ser procurado: "))
    clear()
    #Verificação se há o produto pesquisado em estoque
    if product in stock:
        print("----------")
        print(f"Produto: {product}")
        print(f"Preço de venda: R${stock[product]['price']}")
        print(f"Quantia em estoque: {stock[product]['amount']}")
        print(f"Histórico de preços: {stock[product]['price_historic']}")
        print(f"Categoria do produto: {stock[product]['category']}")
        #Criação do método para filtrar palavras para printar o histórico de vendas
        def key_word_verify(iten):
            return product in iten
        #Filtragem da palavra
        product_filter = filter(key_word_verify, sales_control)
        #Print do histórico de vendas do produto filtrado
        print("Histórico de vendas: ")
        for iten in product_filter:
            print(iten)
        print("----------")
    else:
        print(f"O produto '{product}' não existe em estoque!")


def see_products(stock):
    """
    Função para visualizar todos os produtos em estoque, junto com suas informações
    recebendo por parâmetro o estoque.
    """
    clear()
    print("----------")
    #Laço for para passar item por item e printar as suas respectivas informações
    for product in stock:
        print(f"Produto: {product}")
        print(f"Preço de venda: R${stock[product]['price']}")
        print(f"Quantia em estoque: {stock[product]['amount']}")
        print(f"Histórico de preços: {stock[product]['price_historic']}")
        print(f"Categoria: {stock[product]['category']}")
        print("----------")


def change_product_value(stock, changes_historic):
    """
    Função utilizada para atualizar o valor de um produto já existente em estoque
    e adicionar a mudança de preço ao histórico de mudanças
    recebendo como parâmetros o estoque e a lista de histórico de mudanças.
    """
    product = str(input("Digite o nome do produto que deseja alterar o preço de venda: "))
    #Verificação se o produto existe em estoque
    if product in stock:
        new_value = float(input("Digite o novo valor de venda: "))
        #Aqui o código adiciona a alteração no histórico de alterações
        changes_historic.append(f"Alteração -> valor do produto '{product}' alterado de R${stock[product]['price']} para R${new_value}")
        #Atualização do preço do produto
        stock[product]['price'] = new_value
        #Aqui o código adiciona o antigo valor ao histórico de preços
        stock[product]['price_historic'] += [f"R${stock[product]['price']}"]
        clear()
        print(f"Valor do produto '{product}' atualizado com sucesso para R$ {new_value}!")
        return stock, changes_historic
    else:
        clear()
        print(f"O produto '{product}' não existe em seu estoque!")
        return stock, changes_historic


def delete_product_from_stock(stock, changes_historic):
    """
    Função utilizada para remover um produto de estoque
    e adicionar a remoção ao histórico de alterações
    recebendo por parâmetro o estoque e o histórico de mudanças.
    """
    product = str(input("Digite o nome do produto a ser removido do estoque: "))
    #Verifica se o produto existe em estoque
    if product in stock:
        #Aqui o código remove o produto e adiciona a remoção ao histórico de alterações
        stock.pop(product)
        clear()
        print(f"O produto '{product}' foi removido com sucesso do estoque!")
        changes_historic.append(f"Alteração -> produto '{product}' removido de estoque")
        return stock, changes_historic
    else:
        clear()
        print(f"O produto '{product}' não existe em seu estoque!")
        return stock, changes_historic


def see_products_by_category(stock):
    """
    Função utilizada para listar os produtos de determinada categoria
    recebendo por parâmetro o estoque.
    """
    category = str(input("Digite o nome da categoria que deseja listar: "))
    clear()
    counter = 0
    print("----------")
    for product in stock:
        if stock[product]['category'] == category:
            print(f"Produto: {product}")
            print(f"Preço de venda: R${stock[product]['price']}")
            print(f"Quantia em estoque: {stock[product]['amount']}")
            print(f"Histórico de preços: {stock[product]['price_historic']}")
            print("----------")
            counter += 1
    if counter == 0:
        print("Não existe nenhum produto nesta categoria!")
        print("----------")

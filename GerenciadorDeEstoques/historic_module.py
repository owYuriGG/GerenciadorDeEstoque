from utilits import clear

def print_sales_control(sales_control):
    """
    Função para mostrar o relatório de vendas
    recebendo por parâmetro o relatório de vendas
    """
    clear()
    if len(sales_control) == 0:
        print("Nenhuma venda foi realizada ainda!")
    for item in sales_control:
        print(item)

def print_changes_history(changes_history):
    """
    Função para mostrar o histórico de alterações
    recebendo por parâmetro o histórico de alterações.
    """
    clear()
    if len(changes_history) == 0:
        print("Nenhuma alteração foi realizada ainda!")
    for item in changes_history:
        print(item)
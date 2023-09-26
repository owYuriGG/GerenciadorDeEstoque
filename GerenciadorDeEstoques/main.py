import stock_module
import sales_module
import historic_module
import menu_module

def main():
    stock = {
        'batata' : {
            'amount' : 500,
            'price' : 2.50,
            'price_historic' : ['R$2.50'],
            'category' : "comida" 
        },
        'cafe' : {
            'amount' : 50,
            'price' : 5,
            'price_historic' : ['R$2.50'],
            'category' : "comida" 
        },
        'refrigerante' : {
            'amount' : 20,
            'price' : 10,
            'price_historic' : ['R$10'],
            'category' : "refrigerante" 
        }
    }
    sales_control = []
    changes_historic = []
    while True:
        option = menu_module.menu()
        if option == 1:
            stock, changes_historic = stock_module.add_product(stock, changes_historic)
        elif option == 2:
            stock, changes_historic = stock_module.change_product_value(stock, changes_historic)
        elif option == 3:
            stock, changes_historic = stock_module.delete_product_from_stock(stock, changes_historic)
        elif option == 4:
            historic_module.print_changes_history(changes_historic)
        elif option == 5:
            historic_module.print_sales_control(sales_control)
        elif option == 6:
            stock_module.search_product(stock, sales_control)
        elif option == 7:
            stock_module.see_products(stock)
        elif option == 8:
            stock_module.see_products_by_category(stock)
        elif option == 9:
            stock, sales_control = sales_module.sell_product(stock, sales_control)
        elif option == 10:
            break

main()

import matplotlib.pyplot as plt

sales_list = []


def read_sales_data(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read().splitlines()
        for i in content:
            model, quantity, price, data = i.split(', ')
            sales_list.append({'product_name': model,
                               'quantity': quantity,
                               'price': price,
                               'data': data})
    print("SALES LIST:")
    print(sales_list)
    print()


def total_sales_per_product(sales_data):
    total_sales_for_each_product = []
    total_product_sales = {}
    for product in sales_data:
        car = product['product_name']
        price = product['price']
        quantity = product['quantity']
        overall_price = int(price) * int(quantity)

        if car in total_product_sales:
            total_product_sales[car] += overall_price
        else:
            total_product_sales[car] = overall_price
    total_sales_for_each_product.append(total_product_sales)
    most_profitabel_product = max(total_product_sales, key=total_product_sales.get)

    x = list(total_product_sales.keys())
    y = list(total_product_sales.values())
    plt.bar(x, y, label='Величина выручки')
    plt.xlabel('Название продукта')
    plt.ylabel('Размер выручки')
    plt.title('Общая сумма продаж по каждому продукту')
    plt.legend()

    print('TOTAL SALEL PER PRODUCT:')
    print(total_sales_for_each_product)
    print()
    print(f'Самый прибыльный товар: {most_profitabel_product} с общей выручкой: {total_product_sales[most_profitabel_product]}')
    plt.show()
    print()


def sales_over_time(sales_data):
    total_sales_for_each_date = []
    total_date_sales = {}
    for product in sales_data:
        date = product['data']
        price = product['price']
        quantity = product['quantity']
        overall_price = int(price) * int(quantity)

        if date in total_date_sales:
            total_date_sales[date] += overall_price
        else:
            total_date_sales[date] = overall_price
    total_sales_for_each_date.append(total_date_sales)
    most_profitable_date = max(total_date_sales, key=total_date_sales.get)

    x = list(total_date_sales.keys())
    y = list(total_date_sales.values())
    plt.bar(x, y, label='Величина выручки')
    plt.xlabel('Дата')
    plt.ylabel('Размер выручки')
    plt.title('Общая сумма продаж по каждой дате')
    plt.legend()

    print('TOTAL SALEL FOR EACH DATE:')
    print(total_sales_for_each_date)
    print()
    print(f'Самая прибыльная дата: {most_profitable_date} с общей выручкой: {total_date_sales[most_profitable_date]}')
    plt.show()


read_sales_data('data.txt')
total_sales_per_product(sales_list)
sales_over_time(sales_list)

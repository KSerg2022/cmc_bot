
from prettytable import PrettyTable


def get_table(data):
    table = PrettyTable()
    table.title = list(data.keys())[0]
    table.field_names = ['coin', 'qwt', 'price in USD', 'total']
    table._min_width = {'coin': 6, 'qwt': 15, 'price in USD': 15, 'total': 10}
    for coin in list(data.values())[0][0]:
        table.add_row([coin['coin'], f"{coin['bal']:.4f}", f"{coin['price']:.4f}", f"{ coin['total']:.4f}"])
    table.add_row(['-' * 6, '-' * 15, '-' * 15, '-' * 10])
    table.add_row(['', '', 'Total:', f'{list(data.values())[0][-1]:.4f}'])
    return table


def get_table_all_data(data):

    table = PrettyTable()

    # for data_ in list(data.values())[0]:
    for data_ in list(data.values())[0][:4]:
        table.title = list(data_.keys())[0]
        table.field_names = ['coin', 'qwt', 'price in USD', 'total']
        table._min_width = {'coin': 6, 'qwt': 15, 'price in USD': 15, 'total': 10}
        for coin in list(data_.values())[0]:
            table.add_row([coin['coin'], f"{coin['bal']:.4f}", f"{coin['price']:.4f}", f"{ coin['total']:.4f}"])
        table.add_row(['-' * 6, '-' * 15, '-' * 15, '-' * 10])

        table.add_row(' ' * 4)
        table.add_row(['-' * 6, '-' * 15, '-' * 15, '-' * 10])
    return table

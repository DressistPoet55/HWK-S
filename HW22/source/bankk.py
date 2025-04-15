# bankk.py

class Deposit:
    def __init__(self, start_balance, years, interest_rate=0.10):
        self.start_balance = start_balance
        self.years = years
        self.interest_rate = interest_rate
        self.koll_months = years * 12

    def calculate_final_amount(self):
        monthly_rate = self.interest_rate / 12
        final_amount = self.start_balance * (1 + monthly_rate) ** self.koll_months
        return final_amount


class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return f'Клиент с ID {client_id} уже существует'
        self.clients[client_id] = name
        return f'Зарегистрирован клиент по имени {name} , и присвоен личный id {client_id}'

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            self.deposits[client_id] = Deposit(float(start_balance), int(years))
            return (f'Открыт депозитный счет по id: {client_id}, '
                    f'с балансом {start_balance} рублей на {years} лет')
        else:
            return f'Клиент с ID {client_id} не найден'

    def calc_deposit_interest_rate(self, client_id):
        if client_id in self.deposits:
            return self.deposits[client_id].calculate_final_amount()
        return None

    def close_deposit(self, client_id):
        if client_id in self.deposits:
            del self.deposits[client_id]
            return 'Депозитный счет закрыт'
        return 'Депозитный счет не найден'

def create_bank():
    """Создает экземпляр банка и возвращает его"""
    return Bank()

def create_deposit(start_balance, years, interest_rate=0.10):
    """Создает экземпляр депозита и возвращает его"""
    return Deposit(start_balance, years, interest_rate)
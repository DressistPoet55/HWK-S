# Task 1 Колода карт
import random

class Card:
    number_list = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, must):
        self.number = number
        self.must = must

    def __str__(self):
        return f"Card {self.must}, {self.number}"

class CardsDeck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        self.cards.append(Card('Joker', 'Black'))
        self.cards.append(Card('Joker', 'Red'))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, card_numb):
        if 0 <= card_numb < len(self.cards):
            return self.cards[card_numb]
        else:
            return 'Неверный номер'


deck = CardsDeck()
deck.shuffle()

card_number = int(input('Выберите карту из колоды в 54 карт:'))
card = deck.get(card_number)
print(f'You card is: {card}')

card_number = int(input('Выберите карту из колоды в 54 карт:'))
card = deck.get(card_number)
print(f'You card is: {card}')
print()


# Task 2 Конвертер валют
class CurrencyConverter:
    def __init__(self, val):
        self.val = val

    def exchange_currency(self, currency, amount, target_currency='BYN'):
        if currency not in self.val:
            raise ValueError(f"Неизвестная валюта: {currency}")
        if target_currency not in self.val:
            raise ValueError(f"Неизвестная целевая валюта: {target_currency}")
        amount_in_byn = amount * self.val[currency]
        if target_currency == 'BYN':
            return round(amount_in_byn, 2), target_currency
        amount_in_target_currency = amount_in_byn / self.val[target_currency]
        return round(amount_in_target_currency, 2), target_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


val1 = {
    'USD': 3.27,
    'EUR': 3.50,
    'BYN': 1.00
}
converter = CurrencyConverter(val1)

print(converter.exchange_currency('USD', 10))
print(converter.exchange_currency('EUR', 5))
print(converter.exchange_currency('USD', 10, 'EUR'))
print(converter.exchange_currency('EUR', 5, 'USD'))

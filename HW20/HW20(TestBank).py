import unittest
from HW12 import Bank, Deposit


class TestDeposit(unittest.TestCase):
    def test_calculate_final_amount_default_rate(self):
        deposit = Deposit(1000, 1)
        result = deposit.calculate_final_amount()
        self.assertEqual(result, 1104.7130674412967)

    @unittest.expectedFailure
    def test_negative_balance_should_fail(self):
        # Тест с отрицательным балансом
        deposit = Deposit(-1000, 1)
        result = deposit.calculate_final_amount()
        self.assertGreater(result, 0)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.register_client("0000001", "Siarhei")

    def test_register_client(self):
        result = self.bank.register_client("0000001", "Siarhei")
        self.assertEqual(result, "Зарегистрирован клиент по имени Siarhei ,"
                                 " и присвоен личный id 0000001")

    def test_open_deposit_account(self):
        result = self.bank.open_deposit_account("0000001", 1000, 1)
        self.assertEqual(result, "Открыт депозитный счет по id: 0000001,"
                                 " с балансом 1000 рублей на 1 лет")

    def test_calc_deposit_interest_rate(self):
        self.bank.open_deposit_account("0000001", 1000, 1)
        result = self.bank.calc_deposit_interest_rate("0000001")
        self.assertEqual(result, 1104.7130674412967)

    def test_close_deposit(self):
        self.bank.open_deposit_account("0000001", 1000, 1)
        result = self.bank.close_deposit("0000001")
        self.assertEqual(result, "Депозитный счет закрыт")

    @unittest.expectedFailure
    def test_calc_interest_nonex_deposit(self):
        # Попытка рассчитать проценты для клиента без депозита
        result = self.bank.calc_deposit_interest_rate("0000001")
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()

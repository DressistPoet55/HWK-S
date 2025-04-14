import pytest
import logging
from HW21.source.bank import Bank, Deposit


logger = logging.getLogger()
file_handler = logging.FileHandler("bank_test.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


@pytest.fixture
def bank():
    bank = Bank()
    bank.register_client("0000001", "Siarhei")
    return bank


@pytest.fixture
def deposit():
    return Deposit(start_balance=1000, years=2, interest_rate=0.10)


def test_register_client(bank):
    logger.info("Тест регистрации клиента")
    result = bank.register_client("0000002", "Stepan")
    assert result == "Зарегистрирован клиент по имени Stepan , и присвоен личный id 0000002"


def test_open_deposit_account(bank):
    logger.info("Тест открытия депозитного счета")
    result = bank.open_deposit_account("0000001", 1000, 1)
    assert result == "Открыт депозитный счет по id: 0000001, с балансом 1000 рублей на 1 лет"


def test_calc_deposit_interest_rate(bank):
    logger.info("Тест расчета процентов по депозиту")
    bank.open_deposit_account("0000001", 1000, 1)
    result = bank.calc_deposit_interest_rate("0000001")
    assert result == 1104.7130674412967


def test_deposit_calculate_final_amount(deposit):
    logger.info("Тест расчета итоговой суммы по депозиту")
    result = deposit.calculate_final_amount()
    assert result == 1220.3909613755593


@pytest.mark.xfail(reason="Клиент не существует")
def test_open_deposit_for_nonexistent_client(bank):
    logger.warning("Тест открытия счета для несуществующего клиента")
    result = bank.open_deposit_account("003", 1000, 1)
    assert result == "Открыт депозитный счет по id: 003, с балансом 1000 рублей на 1 лет"

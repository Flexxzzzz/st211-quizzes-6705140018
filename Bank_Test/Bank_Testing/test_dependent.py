from bank import BankAccount

def test_a_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150

def test_b_withdraw():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70
import BankAccount
import unittest

class BankAccountTest(unittest.TestCase):
    
    def test_deposit(self):
        s = BankAccount.Bank_Account()
        self.assertEqual(s.deposit(10000), "Amount Deposited: 10000")
    
    def test_withdraw(self):
        s = BankAccount.Bank_Account()
        self.assertEqual(s.withdraw(50000), "You Withdrew: 50000")

    def test_display(self):
        s = BankAccount.Bank_Account()
        self.assertEqual(s.deposit(50000), "Amount Deposited: 50000")
        self.assertEqual(s.withdraw(10000), "You Withdrew: 10000")
        self.assertEqual(s.display(), "Your Available Balance= 40000")

if __name__ == '__main__':
    unittest.main()
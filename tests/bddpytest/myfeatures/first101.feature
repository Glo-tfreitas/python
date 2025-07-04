Feature: Bank Transactions
    Tests pertaining to banking transactions like withdrawal, deposit

    Scenario: Withdrawal of money
        Given the account balance is 100
        When the account holder withdraws 30
        Then the account balance should be 70

    Scenario: Removal of items from set
        Given a set of three fruits
        When we remove a fruit from the set
        Then the set will have two fruits
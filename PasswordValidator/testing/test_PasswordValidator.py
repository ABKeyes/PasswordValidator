import unittest

from PasswordValidator import validate

class Test_test_PasswordValidator(unittest.TestCase):
    def test_BlankArgs(self) -> None:
        result = validate("Password")
        print(result)
        self.assertTrue(result)

    def test_TrueMessage(self) -> None:
        result = validate("Password")
        print(result)
        self.assertTupleEqual(result, (True, "Password is acceptable"))

    def test_lowerTrue(self) -> None:
        result = validate("Password", lower=5)
        print(result)
        self.assertTrue(result)

    def test_lowerFalse(self) -> None:
        result = validate("Password", lower=9)
        print(result)
        self.assertFalse(result)

    def test_upperTrue(self) -> None:
        result = validate("Password", upper=10)
        print(result)
        self.assertTrue(result)

    def test_upperFalse(self) -> None:
        result = validate("Password", upper=4)
        self.assertFalse(result)

    def test_badUpperBoundMessage(self)-> None:
        result = validate("Password", lower=5, upper=4)
        print(result)
        self.assertTupleEqual(result, (False, "Invalid Upper Bound"))

    def test_badLowerBoundMessage(self) -> None:
        result = validate("Password", lower=0)
        print(result)
        self.assertTupleEqual(result, (False, "Lower limit cannot be less than 1"))

if __name__ == '__main__':
    unittest.main()

import unittest
import string

from PasswordValidator import validate

class test_PasswordValidator(unittest.TestCase):
    special = string.punctuation
    def test_BlankArgs(self) -> None:
        result = validate("Password")
        print(result)
        self.assertTrue(result)

    def test_TrueMessage(self) -> None:
        result = validate("Password")
        test = (True, "Password is acceptable", [])
        print(result)
        self.assertTupleEqual(result, test)

    def test_lowerTrue(self) -> None:
        result = validate("Password", lower=5)
        print(result)
        self.assertTrue(result)

    def test_lowerFalse(self) -> None:
        result = validate("Password", lower=9)
        test = (False, "Password too short", [])
        print(result)
        self.assertTupleEqual(result, test)

    def test_upperTrue(self) -> None:
        result = validate("Password", upper=10)
        print(result)
        self.assertTrue(result)

    def test_upperFalse(self) -> None:
        result = validate("Password", upper=4)
        test = (False, "Password too long", [])
        self.assertTupleEqual(result, test)

    def test_badUpperBoundMessage(self)-> None:
        result = validate("Password", lower=5, upper=4)
        test = (False, "Invalid upper bound", [])
        print(result)
        self.assertTupleEqual(result, test)

    def test_badLowerBoundMessage(self) -> None:
        result = validate("Password", lower=0)
        test = (False, "Lower limit cannot be less than 1", [])
        print(result)
        self.assertTupleEqual(result, test)
    
    def test_singleRegexFail(self) -> None:
        args = ['\d+']
        result = validate("Password", args)
        test = (False, "Failed regex test", [0])
        self.assertTupleEqual(result, test)

    def test_singleRegexPass(self) -> None:
        args = ['[A-Z]']
        result = validate("Password", args)
        test = (True, "Password is acceptable", [])
        self.assertTupleEqual(result, test)

    def test_singleRegexPass2(self) -> None:
        args = ['\d+']
        result = validate("Passw0rd", args)
        test = (True, "Password is acceptable", [])
        self.assertTupleEqual(result, test)

    def test_multiRegexFail(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Password", args)
        test = (False, "Failed regex test", [0,2])
        self.assertTupleEqual(result, test)

    def test_multiRegexPass(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Passw0rd!", args)
        test = (True, "Password is acceptable", [])
        self.assertTupleEqual(result, test)

    def test_multiRegexWithUpperFail(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Passw0rd!", args, upper=6)
        test = (False, "Password too long", [])
        self.assertTupleEqual(result, test)

    def test_multiRegexFailWithUpperFail(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Password", args, upper=6)
        test = (False, "Password too long", [0,2])
        self.assertTupleEqual(result, test)

    def test_multiRegexWithLowerFail(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Passw0rd!", args, 15)
        test = (False, "Password too short", [])
        self.assertTupleEqual(result, test)

    def test_multiRegexFailWithLowerFail(self) -> None:
        args = ['\d+', '[A-Z]', f'[{self.special}]']
        result = validate("Password", args, 15)
        test = (False, "Password too short", [0,2])
        self.assertTupleEqual(result, test)

if __name__ == '__main__':
    unittest.main()

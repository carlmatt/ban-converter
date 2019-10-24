import unittest
from utils.common import convert_bban_to_iban, convert_iban_to_bban


class ConvertBbanToIbanTestCase(unittest.TestCase):
    """ Tests for BBAN to IBAN converter """

    def test_bban_iban_converter_1(self):
        bban = '137835-60518'
        iban = convert_bban_to_iban(bban)
        self.assertEqual(iban, 'FI9113783500060518')

    def test_bban_iban_converter_2(self):
        bban = '4055000800899774'
        iban = convert_bban_to_iban(bban)
        self.assertEqual(iban, 'FI4040550080899774')

    def test_bban_iban_converter_3(self):
        bban = '1597-123'
        iban = convert_bban_to_iban(bban)
        self.assertEqual(iban, 'FI8815971200000003')


class ConvertIbanToBbanTestCase(unittest.TestCase):
    """ Tests for IBAN to BBAN converter """

    def test_iban_bban_converter_1(self):
        iban = 'FI4040550080899774'
        bban = convert_iban_to_bban(iban)
        self.assertEqual(bban, '4055000800899774')

    def test_iban_bban_converter_2(self):
        iban = 'FI3949704998100401'
        bban = convert_iban_to_bban(iban)
        self.assertEqual(bban, '4970490908100401')

    def test_iban_bban_converter_3(self):
        iban = 'FI9113783500060518'
        bban = convert_iban_to_bban(iban)
        self.assertEqual(bban, '1378350000060518')

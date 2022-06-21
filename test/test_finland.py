from unittest import TestCase

from ban_converter.converter import Converter


class ConvertBbanToIbanTestCasesFinland(TestCase):
    """Tests for BBAN to IBAN converter"""

    def test_bban_iban_converter(self):
        converter = Converter(country_code="FI")

        bban = "137835-60518"
        actual = converter.convert_bban_to_iban(bban)
        expected = "FI9113783500060518"
        self.assertEqual(actual, expected)

        bban = "4055000800899774"
        actual = converter.convert_bban_to_iban(bban)
        expected = "FI4040550080899774"
        self.assertEqual(actual, expected)

        bban = "1597-123"
        actual = converter.convert_bban_to_iban(bban)
        expected = "FI8815971200000003"
        self.assertEqual(actual, expected)

        bban = "1597-124"
        actual = converter.convert_bban_to_iban(bban)
        expected = "FI8815971200000003"
        with self.assertRaises(AssertionError):
            assert actual == expected


class ConvertIbanToBbanTestCase(TestCase):
    """Tests for IBAN to BBAN converter"""

    def test_iban_bban_converter(self):
        converter = Converter(country_code="FI")

        iban = "FI4040550080899774"
        actual = converter.convert_iban_to_bban(iban)
        expected = "4055000800899774"
        self.assertEqual(actual, expected)

        iban = "FI3949704998100401"
        actual = converter.convert_iban_to_bban(iban)
        expected = "4970490908100401"
        self.assertEqual(actual, expected)

        iban = "FI9113783500060518"
        actual = converter.convert_iban_to_bban(iban)
        expected = "1378350000060518"
        self.assertEqual(actual, expected)

        iban = "FI9113783500060519"
        actual = converter.convert_iban_to_bban(iban)
        expected = "1378350000060518"
        with self.assertRaises(AssertionError):
            assert actual == expected

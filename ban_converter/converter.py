from ban_converter.countries import finland

supported_countries = {"FI"}


class Converter:
    def __init__(self, country_code: str = "FI"):
        """BBAN <-> IBAN converter.

        Args:
            country_code (optional): Account ISO 3166 country code, defaults to 'FI'.

        Raises:
            ValueError: If the country is not supported.
        """
        self.country_code = country_code

        if country_code not in supported_countries:
            raise ValueError(f"This country is not supported: {country_code}")

    def convert_bban_to_iban(self, bban: str) -> str:
        """Convert a bank account number from BBAN to IBAN format.

        Args:
            bban: Account number in BBAN format.

        Returns:
            Account number in IBAN format.
        """
        if self.country_code == "FI":
            return finland.bban_to_iban(bban)

    def convert_iban_to_bban(self, iban: str) -> str:
        """Convert a bank account number from IBAN to BBAN machine language format.

        Args:
            iban: Account number in IBAN format.

        Returns:
            Account number in BBAN machine language format.
        """
        country_code = iban[:2]

        if country_code == "FI":
            return finland.iban_to_bban(iban)

__version__ = '0.0.2'


def convert_bban_to_iban(bban: str, country: str = 'FI') -> str:
    """
    Convert an account number from BBAN to IBAN format.
    :param bban: Account number in BBAN format
    :param country: Account country
    :return: Account number in IBAN format
    :raises ValueError: If BBAN is too short
    """
    len_orig = len(bban)
    bban_no_dash = bban.replace('-', '')
    len_bban_no_dash = len(bban_no_dash)
    zeros = '0000000'

    if len_orig == 16 and bban.find('-') == -1:
        account_number = bban[0:4] + bban[5:8] + bban[9:]
    elif bban_no_dash[0] in ('4', '5'):
        if 8 <= len_bban_no_dash <= 13:
            account_number = bban_no_dash[0:7] + zeros[:(14 - len_bban_no_dash)] + bban_no_dash[7:]
        else:
            account_number = bban_no_dash
    elif 7 <= len_bban_no_dash <= 13:
        account_number = bban_no_dash[0:6] + zeros[:(14 - len_bban_no_dash)] + bban_no_dash[6:]
    else:
        raise ValueError('BBAN is too short')

    checksum = 98 - int(account_number + '151800') % 97
    iban = country + (zeros + str(checksum))[-2:] + account_number
    return iban


def convert_iban_to_bban(iban: str) -> str:
    """
    Convert an account number from IBAN to BBAN manchine language format.
    :param iban: Account number in IBAN format
    :return: Account number in BBAN machine language format
    :raises ValueError: If IBAN is not in Finnish format
    """
    len_iban = len(iban)
    country_iban = iban[:2]

    if len_iban == 18 and country_iban == 'FI':
        if iban[4] in ('4', '5'):
            bban = iban[4:10] + '0' + iban[10] + '0' + iban[11:]
        else:
            bban = iban[4:10] + '00' + iban[10:]
    else:
        raise ValueError('IBAN is not in Finnish format')

    return bban

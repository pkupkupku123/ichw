"""Currency.py: A Exchange Calculator

__author__ = "Liye"
__pkuid__ = "1800011779"
__email__ = "pkupkupku@pku.edu.cn"
"""

from urllib.request import urlopen


def isinput_valid(currency_from, currency_to, currency_amt):
    """A function to judge whether the input is valid.
    
    For this function, its three arguments are the inputted strings, 
    which are used to modify the URL to visit the exchange website.
    This function will figure out whether the input is valid.
    
    Returns: True or False.
    The value returned has type bool.
    """
    currency_name = ['AED', 'LKR', 'AFN', 'LRD', 'ALL', 
                     'LSL', 'AMD', 'LTL', 'ANG', 'LVL', 
                     'AOA', 'LYD', 'ARS', 'MAD', 'AUD',	
                     'MDL', 'AWG', 'MGA', 'AZN', 'MKD', 
                     'BAM',	'MMK', 'BBD', 'MNT', 'BDT', 
                     'MOP', 'BGN', 'MRO', 'BHD', 'MTL', 
                     'BIF', 'MUR', 'BMD', 'MVR', 'BND', 
                     'MWK', 'BOB', 'MXN', 'BRL', 'MYR', 
                     'BSD', 'MZN', 'BTC', 'NAD', 'BTN', 
                     'NGN', 'BWP', 'NIO', 'BYR', 'NOK', 
                     'BZD', 'NPR', 'CAD', 'NZD', 'CDF', 
                     'OMR', 'CHF', 'PAB', 'CLF', 'PEN', 
                     'CLP', 'PGK', 'CNY', 'PHP', 'COP', 
                     'PKR', 'CRC', 'PLN', 'CUC', 'PYG', 
                     'CUP', 'QAR', 'CVE', 'RON', 'CZK', 
                     'RSD', 'DJF', 'RUB', 'DKK', 'RWF', 
                     'DOP', 'SAR', 'DZD', 'SBD', 'ZWL', 
                     'SCR', 'EGP', 'SDG', 'ERN', 'SEK', 
                     'ETB', 'SGD', 'EUR', 'SHP', 'FJD', 
                     'SLL', 'FKP', 'SOS', 'GBP', 'SRD', 
                     'GEL', 'STD', 'GGP', 'SVC', 'GHS', 
                     'SYP', 'GIP', 'SZL', 'GMD', 'THB', 
                     'GNF', 'TJS', 'GTQ', 'TMT', 'GYD', 
                     'TND', 'HKD', 'TOP', 'HNL', 'TRY', 
                     'HRK', 'TTD', 'HTG', 'TWD', 'HUF', 
                     'TZS', 'IDR', 'UAH', 'ILS', 'UGX', 
                     'IMP', 'USD', 'INR', 'UYU', 'IQD', 
                     'UZS', 'IRR', 'VEF', 'ISK', 'VND', 
                     'JEP', 'VUV', 'JMD', 'WST', 'JOD', 
                     'XAF', 'JPY', 'XAG', 'KES', 'XAU', 
                     'KGS', 'XCD', 'KHR', 'XDR', 'KMF', 
                     'XOF', 'KPW', 'XPD', 'KRW', 'XPF', 
                     'KWD', 'XPT', 'KYD', 'YER', 'KZT', 
                     'ZAR', 'LAK', 'ZMK', 'LBP', 'ZMW', 
                     'LKR']
    n = currency_amt.count('.')
    return (currency_from in currency_name) and (currency_to in currency_name)\
        and (n == 0 or n == 1) and currency_amt.replace('.','1').isdigit()


def test_isinput_valid():
    """A test function of function 'isinput_valid()'.
    
    In this function, with the help of 'assert()', some logical expressions 
    are used to judge if the tested function can work correctly.
    
    If all tests passed, the following statements will be executed.
    Else, the program will report an error and stop.
    
    This test function doesn't need any argument and it has no return value.
    """
    assert(True == isinput_valid('USD', 'EUR', '100'))
    assert(False == isinput_valid('AAA', 'EUR', '100'))
    assert(False == isinput_valid('CNY', 'BBB', '100'))
    assert(False == isinput_valid('MAD', 'EUR', 'ONE HUNDRED'))


def get_input():
    """A function to get a vaild input.
    
    When this function is called, users should enter two currency names and 
    the amount of currency to convert. Then 'isinput_valid()' is called to 
    judge if the input is valid. And this function uses a recursion to make 
    sure that it can get a valid input.
    
    Returns: The name of currency on hand, the name of currency to convert to 
    and the amount of currency to convert.
    The returned values have type string.
    """
    currency_from = input("Enter the currency on hand: ")
    currency_to = input("Enter your target currency: ")
    currency_amt = input("Enter the amount of currency to convert: ")
    if isinput_valid(currency_from, currency_to, currency_amt):
        return currency_from, currency_to, currency_amt
    else:
        print("ERROR!\nCheck your input,please.\nNow try again.")
        return get_input()


def exchange(currency_from, currency_to, currency_amt):
    """A function to figure out the amount of currency after exchange.
    
    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.
    
    Returns: amount of currency received in the given exchange.
    The value returned has type float.
    
    Parameter currency_from: the currency on hand.
    Precondition: currency_from is a string for a valid currency code.

    Parameter currency_to: the currency to convert to.
    Precondition: currency_to is a string for a valid currency code.

    Parameter amount_from: amount of currency to convert.
    Precondition: amount_from is a float.
    """
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=source&to=target&amt=amount'
    url = url.replace('source',currency_from)
    url = url.replace('target',currency_to)
    url = url.replace('amount',currency_amt)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('", "','" : "')
    substr = jstr.split('" : "')
    currency_num = float(substr[3].split()[0]) 
    return currency_num


def test_exchange():
    """A test function of function 'exchange()'.
    
    In this function, with the help of 'assert()', some logical expressions 
    are used to judge if the tested function can work correctly.
    
    If all tests passed, the following statements will be executed.
    Else, the program will report an error and stop.
    
    This test function doesn't need any argument and it has no return value.
    """
    assert(95.856159 == exchange('USD', 'EUR', '111'))
    assert(381169.78326896 == exchange('MAD', 'JPY', '32333'))
    assert(333.28169466295 == exchange('CNY', 'JPY', '20.5'))
    assert(1880.7744844075 == exchange('LSL', 'AOA', '100'))
    assert(82114.69845 == exchange('BBD', 'CDF', '100'))

    
def testAll():
    """test all cases"""
    test_isinput_valid()
    test_exchange()
    print("All tests passed.")


def main():
    """The main module
    
    This main module is consist of function 'exchange()' and 'get_input()'.
    
    And some statements to print instructions are added, in order to create a 
    better user experience.
    """
    print("Wait for a moment,the program is being tested now.")
    testAll()
    print("""Now you can use this Exchange Calculator.
    Follow the instructions below.
    NOTIFICATION: 
    1.The currency name is made up by 3 capital letters,such as USD and CNY.
    2.The amount is a positve integer or decimal,such as 100 and 1.234.
    """)
    currency_from, currency_to, currency_amt = get_input()
    print("After the exchange you have:",end="   ")
    print(exchange(currency_from, currency_to, currency_amt), currency_to)
    print("Thanks for using this program!")

    
if __name__=='__main__':
    main()

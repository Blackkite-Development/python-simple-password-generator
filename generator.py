# Copyright 2020 Blackkite-Development
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" A simple password generator with basic functionality

A simple and easy to use password generator script. The script
has basic functionality, namely a variable password length and the option
to exclude certain groups of characters. The generator only uses the printable
characters from the ASCII table (33-127) and does not depend on any third party libraries.
The password is generated using a SystemRandom to guarantee a more secure password.

"""
import string
from secrets import SystemRandom


def generate_password(length, upper_case=True, lower_case=True, digits=True, punctuation=True):
    """ Generates a secure and random password by using a SystemRandom(),
        a custom length, and four properties influencing the used chars.

        Args:
            length:
                Passes the length for the password
            upper_case:
                Passes the information whether upper case letters should be included or not
            lower_case:
                asses the information whether lower case letters should be included or not
            digits:
                asses the information whether digits should be included or not
            punctuation:
                asses the information whether punctuation letters should be included or not


        Returns:
            A randomly generated password

        Raises:
            Exception: Occurs when length is to short
            TypeError: Occurs when length is not passed as an int
    """

    if type(upper_case) is not bool or type(lower_case) is not bool or type(digits) is not bool or type(
            punctuation) is not bool:
        raise TypeError('Properties have to passed as booleans')

    if type(length) is not int:
        raise TypeError('Length must be passed as int')

    if length <= 0:
        raise Exception("Passed length parameter is to short")

    li = get_allowed_chars(upper_case, lower_case, digits, punctuation)
    secure_random = SystemRandom()
    password = ""
    for i in range(length):
        # Appending a random character from a random list index
        password = password + secure_random.choice(li[secure_random.randint(0, len(li) - 1)])

    return password


def get_allowed_chars(upper_case, lower_case, digits, punctuation):
    """ Checks if a certain group of ASCII characters are passed as
        forbidden and adds one random group to a list.
        In case all groups are being passed as False the function automatically
        adds lower and uppercase characters to the list.

        Args:
            upper_case:
                Passes the information whether upper case letters should be included or not
            lower_case:
                asses the information whether lower case letters should be included or not
            digits:
                asses the information whether digits should be included or not
            punctuation:
                asses the information whether punctuation letters should be included or not


        Returns:
             Returns a list with 1 to 4 groups of characters
    """
    characters = []
    if upper_case is False and lower_case is False and digits is False and punctuation is False:
        characters.append(string.ascii_lowercase)
        characters.append(string.ascii_uppercase)
        return characters

    if upper_case is True:
        characters.append(string.ascii_uppercase)
    if lower_case is True:
        characters.append(string.ascii_lowercase)
    if digits is True:
        characters.append(string.digits)
    if punctuation is True:
        characters.append(string.punctuation)

    return characters

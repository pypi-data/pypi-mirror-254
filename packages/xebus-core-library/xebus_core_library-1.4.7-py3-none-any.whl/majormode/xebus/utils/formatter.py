# Copyright (C) 2019 Majormode.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Majormode or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Majormode.
#
# MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY
# OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE SHALL NOT BE LIABLE FOR ANY
# LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
# OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

import re

from majormode.perseus.model.locale import Locale


ENGLISH_LOCALE = Locale('eng')
FRENCH_LOCALE = Locale('fra')
KOREAN_LOCALE = Locale('kor')
VIETNAMESE_LOCALE = Locale('vie')


def format_first_name(first_name, locale=None):
    """
    Format the first name according to the locale.

    All the name components of French, English, and Vietnamese first names
    are capitalized, while the rest of the words are lower cased.  Korean
    personal names are not transformed.


    @param first_name: Forename (also known as *given name*) of the person.
        The first name can be used to alphabetically sort a list of users.

    @param locale: An object `Locale` that supposedly refers to the name
        of this person.


    @return: The formatted first name of the person.
    """
    first_name_ = normalize_name(first_name)
    return ' '.join([
        component.lower().capitalize()
        for component in first_name_.split()
    ])


def format_full_name(last_name, first_name, locale=None):
    """
    Format the full name according to the locale.

    For French and English personal names, first name comes first, and
    last name comes last.  While for Vietnamese and Korean, this order is
    reversed.


    @param last_name: Surname (also known as *family name*) of the person.
        The last name can be used to alphabetically sort a list of users.

    @param first_name: Forename (also known as *given name*) of the person.
        The first name can be used to alphabetically sort a list of users.

    @param locale: An object `Locale` that supposedly refers to the name
        of this person.


    @return: The formatted full name of the person.
    """
    return f'{first_name} {last_name}' if locale is None or locale in (FRENCH_LOCALE, ENGLISH_LOCALE) \
        else f'{last_name} {first_name}'


def format_last_name(last_name, locale=None):
    """
    Format the last name according to the locale.

    French, English, and Vietnamese personal names are converted to upper
    case.  However, Korean personal names are not upper cased.


    @param last_name: Surname (also known as *family name*) of the person.
        The last name can be used to alphabetically sort a list of users.

    @param locale: An object `Locale` that supposedly refers to the name
        of this person.


    @return: The formatted last name of the person.
    """
    last_name_ = normalize_name(last_name)
    return last_name_.upper()


def normalize_name(name):
    """
    Remove any punctuation and duplicated space characters.


    @param name: A surname, a forename, or a full name of a person.


    @return: The given name that has been cleansed from useless characters.
    """
    # Replace any punctuation character with space.
    punctuationless_string = re.sub(r'[.,\\/#!$%^&*;:{}=\-_`~()<>"\']', ' ', name)

    # Remove any duplicate space characters.
    return ' '.join(punctuationless_string.split())

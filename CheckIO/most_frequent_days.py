__author__ = 'Su-Young Hong'
__version__ = '0.1'
__email__ = 'suyoung.hong@gmail.com'
__status__ = 'for fun'

import datetime

def most_frequent_days(year):
    """
    :param year: integer, year you want to check
    :return: list, days which were most common days in that year
    """
    reference = [('Monday', 0), ('Tuesday', 1), ('Wednesday', 2), ('Thursday', 3), ('Friday', 4), ('Saturday', 5), \
                                                                                                    ('Sunday', 6)]
    firstDay = datetime.date(year, 1, 1)
    lastDay = datetime.date(year, 12, 31)
    firstWeek = range(firstDay.weekday(), 7)
    lastWeek = range(0, lastDay.weekday() + 1)
    Combined = firstWeek + lastWeek # combines last week and first week into one list
    maxFreq = max([Combined.count(i) for i in Combined]) # gets the most common frequency day's frequency in Combined
    MaxDays = [i for i in set(Combined) if Combined.count(i) == maxFreq] # gets days where maxFreq occurs
    freq_Days = [i[0] for i in reference if i[1] in MaxDays]
    return freq_Days



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"


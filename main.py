# Problem 34:
#     Digit Factorials
#
# Description:
#     145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#     Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#     Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

# Store all the factorials once to avoid re-calc
DIGIT_FACTS = [factorial(i) for i in range(10)]
CURIOUS_LIMIT = 7 * factorial(9)


def digit_factorial_sum(n: int) -> int:
    """
    Returns the 'digit factorial sum' of `n`,
      meaning the sum of the factorials of the digits of `n`.

    Args:
        n (int): Natural number

    Returns:
        (int): Digit factorial sum of `n`
    """
    global DIGIT_FACTS
    # Just use the str of the number
    return sum(map(lambda d: DIGIT_FACTS[int(d)], list(str(n))))


def main() -> int:
    """
    Returns the sum of all 'curious' numbers, meaning
      numbers which are equal to the sum of the factorials of their digits.

    Returns:
        (int): Sum of all curious numbers
    """
    # Idea 0:
    #     No single-digit numbers qualify, according to instructions.
    #
    #         ==> Only consider numbers with 2 or more digits (10 and above)

    # Idea 1:
    #     Consider range of all 8-digit numbers: [10^7, 10^8).
    #     Largest achievable sum of digit factorials among this is when all digits are 9's.
    #         => 99,999,999 => 8 * 9! = 2,903,040 < 10^7 = 10,000,000
    #
    #     Thus no 8-digit number is a candidate.
    #     Same issue arises when number of digits exceeds 8,
    #       as numbers grow faster than possible digit factorial sums.
    #
    #         ==> Only consider numbers less than 10^7

    # Idea 2:
    #     Consider range of all 7-digit numbers: [10^6, 10^7).
    #     Largest achievable sum of digit factorials among this is when all digits are 9's.
    #         => 9,999,999 => 7 * 9! = 2,540,160 >= 10^6 = 1,000,000
    #
    #     Thus we have another upper limit of 2,540,160, as no 7-digit number above this would qualify.
    #
    #         ==> Only consider numbers up to 7 * 9! = 2,540,160 (inclusive)

    global CURIOUS_LIMIT
    curious_total = 0
    for i in range(10, CURIOUS_LIMIT + 1):
        if digit_factorial_sum(i) == i:
            curious_total += i
    return curious_total


if __name__ == '__main__':
    curious_sum = main()
    print('Sum of all curious numbers:')
    print('  {}'.format(curious_sum))

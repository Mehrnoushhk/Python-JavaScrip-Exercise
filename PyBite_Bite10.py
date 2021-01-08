# In this bite you learn to catch/raise exceptions.
#
# Write a simple division function meeting the following requirements:
#
# when denominator is 0 catch the corresponding exception and return 0. when
# numerator or denominator are not of the right type reraised the
# corresponding exception. if the result of the division (after surviving
# the exceptions) is negative, raise a ValueError

def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError
    except ZeroDivisionError:
        result = 0
        return result
    except TypeError:
        print('Type Error')
    except ValueError:
        print('Value Error')
    else:
        return result


print(positive_divide(50, -10))
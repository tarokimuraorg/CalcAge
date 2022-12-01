from AgeCalculator import AgeCalculator

if __name__ == '__main__':

    try:
        age = AgeCalculator().age(1976,12,27)
        print('{}'.format(age))

    except ValueError as ve:
        print('{}'.format(ve))

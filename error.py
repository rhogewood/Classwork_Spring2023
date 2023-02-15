# def calc_square_root(n):
# 	try:
# 		from my_calc import sqrt
# 	except ModuleNotFoundError:
# 		from math import sqrt

# 	answer = sqrt(n)
# 	return n


def my_func(val):
    try:
        for i in val:
            print(i)
    except TypeError:
        val = str(val)
        for i in val:
            print(i)


def main():
    my_func(12345)


if __name__ == "__main__":
    main()

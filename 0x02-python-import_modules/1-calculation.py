#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mu1, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
<<<<<<< HEAD
    print("{} * {} = {}".format(a, b, mu1(a, b)))
=======
    print("{} * {} = {}".format(a, b, mul(a, b)))
>>>>>>> 798e7bb1754db6a5437482c6521e2cbee32f4415
    print("{} / {} = {}".format(a, b, div(a, b)))

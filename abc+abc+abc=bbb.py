from random import sample

def get_rand_str():
    a, b, c = sample(set(list(range(10))), 3)
    a = str(a)
    b = str(b)
    c = str(c)
    return a, b, c

a, b, c = get_rand_str()
while 3 * int(a + b + c) != int(b + b + b):
    a, b, c = get_rand_str()
print("a=%s, b=%s, c=%s" % (a, b, c))



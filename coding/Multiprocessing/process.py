"""Multiprocessing Testing """


from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__process__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from src.util import rand_date

    print(rand_date(10, start=18))

if __name__ == '__main__':
    import sys
    sys.path.append('..')

    from src.factory.user import CustomerFactory

    cf = CustomerFactory()
    customer = cf.make('Anne')
    print(customer, '\n')

    names = ['John', 'Peter', 'Jack', 'Anne', 'Hanna']
    customers = cf.make_many(names)

    for c in customers:
        print(c)
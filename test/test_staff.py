if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from src.user.employee import Manager, Salesperson, Receptionist

    m = Manager('John')
    s = Salesperson('Peter')
    r = Receptionist('Jack')

    m.active = True
    print(m.active)
    print(m.work)

    print(m)
    print(s)
    print(r)
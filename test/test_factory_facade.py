
if __name__ == '__main__':
    import sys
    sys.path.append('..')

    from src.facades import FactoryFacade
    from src.factory.user import CustomerFactory
    from src.factory.staff import RandStaffFactory

    path = '..\\src\\resource\\names.txt'

    ff = FactoryFacade(RandStaffFactory())
    ff.factory = CustomerFactory()
    customers = ff.load_data_by_name(3, path)
    for c in customers:
        print(c)
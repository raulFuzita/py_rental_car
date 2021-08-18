
if __name__ == "__main__":
    import sys
    sys.path.append('..')
    
    from src.factory.user import CustomerFactory
    from src.factory.vehicle import RandCarFactory
    from src.factory.staff import RandStaffFactory, ManagerFactory, \
    SalespersonFactory, ReceptionistFactory
    from src.facades import FactoryFacade, RentalCarFacade
    from src.user.employee import Salesperson
    from src.views import Menu

    path = 'resource\\names.txt'

    ff = FactoryFacade(CustomerFactory())
    customers = ff.load_data_by_name(30, path)

    ff.factory = ManagerFactory()
    managers = ff.load_data_by_name(2, path)

    ff.factory = SalespersonFactory()
    salespersons = ff.load_data_by_name(2, path)

    ff.factory = ReceptionistFactory()
    receptionists = ff.load_data_by_name(2, path)

    ff.factory = RandStaffFactory()
    staff = ff.load_data_by_name(10, path)
    staff += managers + salespersons + receptionists

    cf = RandCarFactory()
    cars = cf.make_many(300)

    saller = [s for s in staff if isinstance(s, Salesperson) and s.active]
    rcf = RentalCarFacade(saller, cars)

    records = [rcf.rent_car(c) for c in customers]

    m = Menu()
    m.cars(cars).staff(staff).customers(customers).records(records)
    m.show_menu()

    print('System has ended')
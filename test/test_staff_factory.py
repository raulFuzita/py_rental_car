
if __name__ == '__main__':
    import sys
    sys.path.append('..')

    from src.factory.staff import ManagerFactory, SalespersonFactory, \
    ReceptionistFactory, RandStaffFactory

    mf = ManagerFactory()
    sf = SalespersonFactory()
    rf = ReceptionistFactory()

    rdf = RandStaffFactory()

    names = ['John', 'Peter', 'Jack', 'Anne', 'Hanna', 
            'Caroline', 'Fergal', 'Kathleen', 'Brian',
            'Ross', 'Barbara', 'Erick', 'Wallace']

    staff = rdf.make_many(names)

    for s in staff:
        print(s)
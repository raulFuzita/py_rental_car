
if __name__ == '__main__':
    import sys
    sys.path.append('..')
    
    from src.factory.staff import RandStaffFactory
    from src.user.employee import StaffCollection, MinActiveStaffFilter

    rdf = RandStaffFactory()

    names = ['John', 'Peter', 'Jack', 'Anne', 'Hanna']

    staff = rdf.make_many(names)

    sf = StaffCollection.rand_staff(staff)
    print(sf)

    for s in staff:
        print(s)

    staff = StaffCollection.filter(staff, MinActiveStaffFilter())

    print(' After Filtering '.center(80, '-'))

    for s in staff:
        print(s)
    
    
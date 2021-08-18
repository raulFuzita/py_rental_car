
if __name__ == '__main__':
    import sys
    sys.path.append('..')

    from src.factory.vehicle import RandCarFactory

    carfactory = RandCarFactory()

    cars = carfactory.make_many(5)

    for car in cars:
        print(car)



if __name__ == "__main__":
    import sys
    sys.path.append('..')

    from src.vehicle import BMW, Ford, Toyota
    from src.vehicle.model import Family, Luxury, Sport

    bmw = BMW()
    bmw.model = Luxury()
    print(bmw)

    ford = Ford()
    ford.model = Sport()
    print(ford)

    toyota = Toyota()
    toyota.model = Family()
    print(toyota)
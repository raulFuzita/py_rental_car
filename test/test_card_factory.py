
if __name__ == '__main__':

    import sys
    sys.path.append('..')

    from src.factory.card.visacard_factory import VisaCardFactory
    from src.factory.card.maestro_factory import MaestroFactory
    from src.factory.card import MasterCardFactory

    vcf = VisaCardFactory()
    print(vcf.make('John'))

    mtf = MaestroFactory()
    print(mtf.make('Peter'))

    mcf = MasterCardFactory()
    print(mcf.make('Jack'))
    
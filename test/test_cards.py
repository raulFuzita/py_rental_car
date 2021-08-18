
if __name__ == "__main__":
    import sys

    sys.path.append('..')

    from src.card import Card
    from src.card import MasterCard
    from src.util import fmt_card_number

    mc = MasterCard('John')
    print(fmt_card_number(mc.card_number))
    
    print(mc)
    print(repr(mc))

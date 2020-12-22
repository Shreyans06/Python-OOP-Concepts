class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:
            raise Exception("")
        if price > self.cards[card_no].balance:
            raise Exception()


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)

while True:
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        print("Something went wrong. " + str(e))



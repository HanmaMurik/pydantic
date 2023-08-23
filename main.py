from pydantic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    name: Optional[str]
    mail: Optional[str]
    address: Optional[str]

user = User(name='Murik', mail='u@pac', address='street: burit')
print(user)


class Banks(BaseModel):
    name: Optional[str]
    rating: Optional[str]
    opened: Optional[str]

bank = Banks(name='NBU', rating='top1', opened='24 hours')
print(bank)


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: Optional[str]

cards = Cards(cardholder=user, which_bank=bank, opened='24 hours')
print(cards)


class Balance(BaseModel):
    card: Cards
    amount: Optional[int]
    currency: List[Dict[str, int]]

balance = Balance(card=cards, amount=100, currency=[{'USD-UZS': 2000}])
print(balance)




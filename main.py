#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.id_cards import IdCards
from web_api.route import app

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print('-- Create a new Id --')
id_card = IdCards()
id_card.is_found = False
id_card.owner_first_name = 'Yebsira'
id_card.owner_last_name = 'Moges'
id_card.save()
print(id_card)

my_user.add_found_id(id_card)
print(my_user)
my_user.id = '12dsfdf'
my_user.save()

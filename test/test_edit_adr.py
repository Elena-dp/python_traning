from model.addrress import Addrress
from random import randrange

def test_edit_fname(app):
    if app.addline.count()==0:
        app.addline.add_new(Addrress(fname="edit", mname="edit", lname="edit", niname="test8", comp="test8", addrr="test8", homtel="+7777444test8", mail="8ehgsl@test"))
    old_list_adr = app.addline.get_adr_list()
    index = randrange(len(old_list_adr))
    addrrss = Addrress(fname="New06okt_3")
    addrrss.id=old_list_adr[index].id
    app.addline.edit_adr_by_index(index, addrrss)
    assert len(old_list_adr) == app.addline.count()
    new_list_adr = app.addline.get_adr_list()
    old_list_adr[index]=addrrss
    assert sorted(old_list_adr, key=Addrress.id_or_max) == sorted(new_list_adr, key=Addrress.id_or_max)

#def test_edit_adr(app):
#    if app.addline.count()==0:
#        app.addline.add_new(Addrress(fname="test7", mname="test7", lname="test7", niname="test7", comp="test7", addrr="test7", homtel="+7777444test7", mail="7ehgsl@test"))
#    old_list_adr = app.addline.get_adr_list()
#    app.addline.edit_adr(Addrress(fname="N", mname="N", lname="N", niname="N", comp="N", addrr="N", homtel="+71239876543", mail=""))
#    new_list_adr = app.addline.get_adr_list()
#    assert len(old_list_adr) == len(new_list_adr)

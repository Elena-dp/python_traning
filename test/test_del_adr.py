from model.addrress import Addrress
from random import randrange

def test_del_some_adr(app):
    if app.addline.count()==0:
        app.addline.add_new(Addrress(fname="test", mname="test", lname="test", niname="test", comp="test", addrr="test", homtel="+7777444test", mail="ehgsl@test"))
    old_list_adr = app.addline.get_adr_list()
    index = randrange(len(old_list_adr))
    app.addline.del_adr_by_index(index)
    assert len(old_list_adr)-1 == app.addline.count()
    new_list_adr = app.addline.get_adr_list()
    old_list_adr[index:index+1]=[]
    assert old_list_adr == new_list_adr

def test_del_alladr(app):
    if app.addline.count() == 0:
        app.addline.add_new(Addrress(fname="test", mname="test", lname="test", niname="test", comp="test", addrr="test", homtel="+7777444test", mail="ehgsl@test"))
        app.addline.add_new(Addrress(fname="test 2", mname="test 2", lname="test 2", niname="test 2", comp="test 2", addrr="test 2", homtel="+7777444test", mail="ehgsl@test 2"))
    app.addline.delete_alladr()
    assert app.addline.count() == 0



#def test_del_first_adr(app):
#    if app.addline.count()==0:
#        app.addline.add_new(Addrress(fname="test", mname="test", lname="test", niname="test", comp="test", addrr="test", homtel="+7777444test", mail="ehgsl@test"))
#    old_list_adr = app.addline.get_adr_list()
#    app.addline.del_first_adr()
#    assert len(old_list_adr)-1 == app.addline.count()
#    new_list_adr = app.addline.get_adr_list()
#    old_list_adr[0:1]=[]
#    assert old_list_adr == new_list_adr
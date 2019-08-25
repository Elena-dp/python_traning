# -*- coding: utf-8 -*-

from model.addrress import Addrress



def test_add_adr(app):
    old_list_adr = app.addline.get_adr_list()
    addrress=(Addrress(fname="gs", mname="tr", lname="ytj", niname="hs", comp="yjj", addrr="aa", homtel="+77774444455", mail="ehgsl@dp"))
    app.addline.add_new(addrress)
    new_list_adr = app.addline.get_adr_list()
    assert len(old_list_adr)+1 == len(new_list_adr)
    old_list_adr.append(addrress)
    assert sorted(old_list_adr, key=Addrress.id_or_max) == sorted(new_list_adr, key=Addrress.id_or_max)

#def test_add_empty_adr(app):
#    old_list_adr = app.addline.get_adr_list()
#    app.addline.add_new(Addrress(fname="", mname="", lname="", niname="", comp="", addrr="", homtel="", mail=""))
#    new_list_adr = app.addline.get_adr_list()
#    assert len(old_list_adr)+1 == len(new_list_adr)


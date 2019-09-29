# -*- coding: utf-8 -*-

from model.addrress import Addrress



def test_add_adr(app):
    old_list_adr = app.addline.get_adr_list()
    addrrss=(Addrress(fname="F29092019", mname="tr", lname="L29092019", niname="hs", comp="yjj", addrr="aa", homtel="+77774444455", mail="ehgsl@dp"))
    app.addline.add_new(addrrss)
    assert len(old_list_adr)+1 == app.addline.count()
    new_list_adr = app.addline.get_adr_list()
    old_list_adr.append(addrrss)
    assert sorted(old_list_adr, key=Addrress.id_or_max) == sorted(new_list_adr, key=Addrress.id_or_max)

#def test_add_empty_adr(app):
#    old_list_adr = app.addline.get_adr_list()
#    app.addline.add_new(Addrress(fname="", mname="", lname="", niname="", comp="", addrr="", homtel="", mail=""))
#    new_list_adr = app.addline.get_adr_list()
#    assert len(old_list_adr)+1 == len(new_list_adr)


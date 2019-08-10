# -*- coding: utf-8 -*-

from model.addrress import Addrress



def test_add_adr(app):
    app.addline.add_new(Addrress(fname="gs", mname="tr", lname="ytj", niname="hs", comp="yjj", addrr="aa", homtel="+77774444455", mail="ehgsl@dp"))


def test_add_empty_adr(app):
    app.addline.add_new(Addrress(fname="", mname="", lname="", niname="", comp="", addrr="", homtel="", mail=""))


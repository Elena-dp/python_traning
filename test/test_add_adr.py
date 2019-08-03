# -*- coding: utf-8 -*-

import pytest
from model.addrress import Addrress
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_adr(app):
    app.session.login(username="admin", password="secret")
    app.addline.add_new(Addrress(fname="Le", mname="An", lname="Ka", niname="eldp", comp="DiPi", addrr="Moj", homtel="+77777777777", mail="el@dprint.ru"))
    app.session.logout()


def test_add_empty_adr(app):
    app.session.login(username="admin", password="secret")
    app.addline.add_new(Addrress(fname="", mname="", lname="", niname="", comp="", addrr="", homtel="", mail=""))
    app.session.logout()


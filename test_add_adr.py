# -*- coding: utf-8 -*-

import pytest
from addrress import Addrress
from applicationaddrr import Applicationaddrr


@pytest.fixture
def app(request):
    fixture=Applicationaddrr()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_adr(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_string(Addrress(fname="Le", mname="An", lname="Ka", niname="eldp", comp="DiPi", addrr="Moj", homtel="+77777777777", mail="el@dprint.ru"))
    app.return_to_home()
    app.logout()


def test_add_empty_adr(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_string(Addrress(fname="", mname="", lname="", niname="", comp="", addrr="", homtel="", mail=""))
    app.return_to_home()
    app.logout()


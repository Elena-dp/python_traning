


def test_del_first_adr(app):
    app.session.login(username="admin", password="secret")
    app.addline.del_first_adr()
    app.session.logout()


def test_del_alladr(app):
    app.session.login(username="admin", password="secret")
    app.addline.delete_alladr()
    app.session.logout()

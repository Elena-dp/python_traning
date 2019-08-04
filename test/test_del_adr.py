


def test_del_first_adr(app):
    app.session.login(username="admin", password="secret")
    app.delete.del_first_adr(app)
    app.session.logout()


def test_del_alladr(app):
    app.session.login(username="admin", password="secret")
    app.delete.delete_alladr(app)
    app.session.logout()

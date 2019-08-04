


def test_del_first_adr(app):
    app.session.login(username="admin", password="secret")
    app.delete.del_first_adr(app)
    app.session.logout()
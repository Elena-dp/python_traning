

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.delete.delete_first_group(app)
    app.session.logout()


def test_adr_in_group(app):
    app.session.login(username="admin", password="secret")
    app.adr_and_group.first_adr_fist_group(app)
    app.session.logout()
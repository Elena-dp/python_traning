

def test_adr_in_group(app):
    app.session.login(username="admin", password="secret")
    app.adr_and_group.first_adr_fist_group(app)
    app.session.logout()

def test_adr_in_specgroup(app):
    app.session.login(username="admin", password="secret")
    app.adr_and_group.first_adr_spec_group(app)
    app.session.logout()
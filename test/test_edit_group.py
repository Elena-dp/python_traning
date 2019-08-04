from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.edit.edit_group(Group(name="3", header="3", footer="3"),app)
    app.session.logout()
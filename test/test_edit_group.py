from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="3", header="3", footer="3"))
    app.session.logout()
from model.group import Group


def test_edit_group(app):
    app.group.edit_group(Group(name="3", header="3", footer="3"))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new header"))

from model.group import Group


def test_edit_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test5", header="test5", footer="test5"))
    app.group.edit_group(Group(name="3", header="3", footer="3"))

def test_modify_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="test6"))
    app.group.modify_first_group(Group(name="new group"))

def test_modify_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(header="test7"))
    app.group.modify_first_group(Group(header="new header"))

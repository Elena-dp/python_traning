from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="modify"))
    old_groups=app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups)==app.group.count()
    new_groups=app.group.get_group_list()
    old_groups[index]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#тест до ДЗ13
#def test_modify_group_name(app):
#    if app.group.count()==0:
#        app.group.create(Group(name="test6"))
#    old_groups=app.group.get_group_list()
#    group = Group(name="new group")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    assert len(old_groups)==app.group.count()
#    new_groups=app.group.get_group_list()
#    old_groups[0]=group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group(app):
#    if app.group.count()==0:
#        app.group.create(Group(name="test5", header="test5", footer="test5"))
#    old_groups=app.group.get_group_list()
#    app.group.edit_group(Group(name="3", header="3", footer="3"))
#    new_groups=app.group.get_group_list()
#    assert len(old_groups)==len(new_groups)

#def test_modify_group_header(app):
#    if app.group.count()==0:
#        app.group.create(Group(header="test7"))
#    old_groups=app.group.get_group_list()
#    app.group.modify_first_group(Group(header="new header"))
#    new_groups=app.group.get_group_list()
#    assert len(old_groups)==len(new_groups)
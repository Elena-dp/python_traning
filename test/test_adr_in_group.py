from model.addrress import Addrress
from model.group import Group

def test_adr_in_group(app):
# сейчас и при (0.7 и 2) срабатывает.....ранее работало корректно при self.wd.implicitly_wait(60), при 5, 30 - падает - происходит выделение чекбокса группы, а его быть не может.
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    else:
        if app.addline.count() == 0:
            app.addline.add_new(Addrress(fname="test 3", mname="test 3", lname="test 3", niname="test 3", comp="test 3", addrr="test 3",
                     homtel="+7777444test3", mail="3ehgsl@test"))
    app.addline.first_adr_fist_group()

#def test_adr_in_specgroup(app):
#    app.addline.first_adr_spec_group(app)

#def test_alladr_in_specgroup(app):
#    app.addline.alladr_in_specgroup(app)

from model.addrress import Addrress


def test_del_first_adr(app):
    if app.addline.count()==0:
        app.addline.add_new(Addrress(fname="test", mname="test", lname="test", niname="test", comp="test", addrr="test", homtel="+7777444test", mail="ehgsl@test"))
    app.addline.del_first_adr()

def test_del_alladr(app):
    app.addline.delete_alladr()

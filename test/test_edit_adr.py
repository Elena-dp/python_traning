from model.addrress import Addrress



def test_edit_adr(app):
    if app.addline.count()==0:
        app.addline.add_new(Addrress(fname="test7", mname="test7", lname="test7", niname="test7", comp="test7", addrr="test7", homtel="+7777444test7", mail="7ehgsl@test"))
    app.addline.edit_adr(Addrress(fname="N", mname="N", lname="N", niname="N", comp="N", addrr="N", homtel="+71239876543", mail=""))

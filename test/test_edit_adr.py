from model.addrress import Addrress



#def test_edit_adr(app):
#    if app.addline.count()==0:
#        app.addline.add_new(Addrress(fname="test7", mname="test7", lname="test7", niname="test7", comp="test7", addrr="test7", homtel="+7777444test7", mail="7ehgsl@test"))
#    app.addline.edit_adr(Addrress(fname="N", mname="N", lname="N", niname="N", comp="N", addrr="N", homtel="+71239876543", mail=""))


def test_edit_fname(app):
    if app.addline.count()==0:
        app.addline.add_new(Addrress(fname="test8", mname="tes8", lname="test8", niname="test8", comp="test8", addrr="test8", homtel="+7777444test8", mail="8ehgsl@test"))
    app.addline.edit_adr(Addrress(fname="New24082019"))

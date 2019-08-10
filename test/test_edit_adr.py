from model.addrress import Addrress



def test_edit_adr(app):
    app.addline.edit_adr(Addrress(fname="N", mname="N", lname="N", niname="N", comp="N", addrr="N", homtel="+71239876543", mail=""))

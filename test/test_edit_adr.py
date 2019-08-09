from model.addrress import Addrress



def test_edit_adr(app):
    app.session.login(username="admin", password="secret")
    app.addline.edit_adr(Addrress(fname="N", mname="N", lname="N", niname="N", comp="N", addrr="N", homtel="+71239876543", mail=""),app)
    app.session.logout()
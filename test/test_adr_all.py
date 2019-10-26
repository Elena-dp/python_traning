from random import randrange
import re



def test_some_contact_all(app):
    index=randrange(app.addline.count())
    contact_all_from_home_page = app.addline.get_adr_list()[index]
    contact_all_from_edit_page = app.addline.get_contact_info_from_edit_page(index)
    assert merge_contact_all(contact_all_from_home_page) == merge_contact_all_to_edit(contact_all_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_contact_all_to_edit(addrress):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [addrress.lname, addrress.fname, addrress.id, addrress.addrr,
                                         addrress.mail1, addrress.mail2, addrress.mail3,
                                         addrress.homephone, addrress.mobilephone,
                                         addrress.workphone, addrress.secondaryphone])))))

def merge_contact_all(addrress):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [addrress.lname, addrress.fname, addrress.id, addrress.addrr,
                                         addrress.mail,
                                         addrress.all_phones_from_home_page])))))


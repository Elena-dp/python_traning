import re



def test_phones_on_home_page(app):
    contact_from_home_page = app.addline.get_adr_list()[0]
    contact_from_edit_page = app.addline.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.addline.get_contact_from_view_page(0)
    contact_from_edit_page = app.addline.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(addrress):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [addrress.homephone, addrress.mobilephone, addrress.workphone, addrress.secondaryphone])))))


from random import randrange



def test_some_contact_all(app):
    index=randrange(app.addline.count())
    contact_from_home_page = app.addline.get_adr_list()[index]








    contact_from_home_page = app.addline.get_adr_list()[0]
    contact_from_edit_page = app.addline.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_hpme_page == merge_phones_like_on_home_page(contact_from_edit_page)
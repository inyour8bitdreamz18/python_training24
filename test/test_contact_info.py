import re
from random import randrange

def test_info_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname.strip()
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname.strip()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)


def clear_phones(s):
    return re.sub("[()/ .-]", "", s)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    # Обратная проверка - (работа с данными в функциональном стиле)
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x),
                                                   filter(lambda x: x is not None,
                                                                              [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    # Обратная проверка - (работа с данными в функциональном стиле)
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2, contact.email3]))))

'''
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
'''
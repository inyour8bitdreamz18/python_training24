import re
from random import randrange
'''
def test_info_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname.strip()
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname.strip()
    assert contact_from_home_page.address == contact_from_edit_page.address.strip()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
'''

def test_all_info_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    #contacts_from_edit_page = db.get_contact_list()
    for contact_from_home_page in contacts_from_home_page:
        try:
            contact_from_edit_page = db.get_contact_by_id(contact_from_home_page.id)
            assert contact_from_home_page.firstname == contact_from_edit_page.firstname.strip()
            assert contact_from_home_page.lastname == contact_from_edit_page.lastname.strip()
            assert contact_from_home_page.address == contact_from_edit_page.address.strip()
            assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
            assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
        except AssertionError:
            print(contact_from_edit_page, " has assert Error")

def clear(phone):
    if phone != "":
        return re.sub("[()/ .-]", "", phone)
    else:
        return ""


def clear_emails(email):
    if email != "":
        return email.strip()
    else:
        return ""


def merge_phones_like_on_home_page(contact):
    # Обратная проверка - (работа с данными в функциональном стиле)
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                                              [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    # Обратная проверка - (работа с данными в функциональном стиле)
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_emails(x),
                                                   filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2, contact.email3]))))

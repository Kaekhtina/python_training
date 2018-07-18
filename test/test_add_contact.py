# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.init_contacts_creation(Contact(firstName="test", middleName="test", lastName="test", nickname="test", company="tttt", title="ttttt", address="ffffff", home="ffffff",
                                mobile="567565756756757", email="fff", secondAddress="ferfre", notes="erfrefre"))




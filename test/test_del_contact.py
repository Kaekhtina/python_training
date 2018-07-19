# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test", middleName="test", lastName="test", nickname="test", company="tttt", title="ttttt", address="ffffff", home="ffffff",
                               mobile="567565756756757", email="fff", secondAddress="ferfre", notes="erfrefre"))
    app.contact.delete_first_contact()

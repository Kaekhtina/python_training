# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.init_contacts_creation(Contact(firstName="test", middleName="test", lastName="test", nickname="test", company="tttt", title="ttttt", address="ffffff", home="ffffff",
                                mobile="567565756756757", email="fff", secondAddress="ferfre", notes="erfrefre"))
    app.session.logout()




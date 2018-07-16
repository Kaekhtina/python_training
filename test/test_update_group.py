# -*- coding: utf-8 -*-
from model.group import Group

def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(name="test7", header="test7", footer="test7"))
    app.session.logout()
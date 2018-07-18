# -*- coding: utf-8 -*-
from model.group import Group

def test_update_group(app):
    app.group.update_group(Group(name="test7", header="test7", footer="test7"))

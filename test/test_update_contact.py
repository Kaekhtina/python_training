from model.contact import Contact


def test_update_contact(app):
    app.contact.update_contact(Contact(firstName="test7", middleName="test7", lastName="test7", nickname="test7", company="tttt7", title="ttttt7", address="ffffff7", home="ffffff7",
                                mobile="77777777777", email="fff7", secondAddress="ferfre7", notes="erfrefre7"))

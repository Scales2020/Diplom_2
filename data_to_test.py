class TestData:
    new_user = {"email": "kuku000@ku.ru","password": "123456","name": "Kuku000"}
    user_empty_email = {"email": "","password": "123456","name": "Kuku00"}
    new_user_wrong = {"email": "kuku_ruku@ku.ru", "password": "654321", "name": "Kukuruku"}
    changed_user = {"email": "kuku00@ku.ru", "password": "123456", "name": "Kukuruku"}

    ingr = {"ingredients": ["61c0c5a71d1f82001bdaaa6e","61c0c5a71d1f82001bdaaa6d"]}
    ingr_empty = {"ingredients": []}
    ingr_nonvalid = {"ingredients": ["111","aaa"]}


import requests
import json
import unittest


class OurTestCase(unittest.TestCase):

    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/books'
        self.book = {"title": "Kaidzen", "author": "Masaki Imae"}
        self.book_changed = {"title": "Kaidzen", "author": "Isaaki Amae"}
        req = requests.post(url=self.url, data=self.book)
        self.book_created = req.json()
        self.book_id = self.book_created['id']

    def test_create_and_check(self):
        check = requests.get(url=self.url + '/' + str(self.book_id))
        check1 = check.json()
        self.assertEqual(self.book["title"], check1["title"])
        self.assertEqual(self.book["author"], check1["author"])

    def test_change_and_check(self):
       req_change = requests.put(url=self.url + '/' + str(self.book_id), data=self.book_changed)
       changed_book = req_change.json()
       self.assertEqual(self.book_changed["title"], changed_book["title"])
       self.assertEqual(self.book_changed["author"], changed_book["author"])

    def test_delete_and_check(self):
        req_delete = requests.delete(url=self.url + '/' + str(self.book_id))
        req_check_delete = requests.get(url=self.url+'/'+str(self.book_id))
        self.assertEqual(req_check_delete.json()['detail'], 'Not found.')

#   ВАЖНО! ФИЛОСОФСКИЙ ВОПРОС ДЛЯ ЛЕНЫ.  Скажи пожалуйста, у нас получается метод POST искользуется в setUp чтобы сделать переменную book_id "передаваемую" в другие методы.
# корректно ли это, когда тестируемый метод используется в сет-ап и теар-дауне ?


test_cr = OurTestCase('test_create_and_check')
test_ch_check = OurTestCase('test_change_and_check')
test_del_check = OurTestCase('test_delete_and_check')

test_cr.run()
test_ch_check.run()
test_del_check.run()






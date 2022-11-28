# class BookTestCase(TestCase):
#     def test_fields_author_name(self):
#         author = Author(name="Mazuki Sekida")
#         author.save()
#         book = Book(name="Zen Training", author=author)
#         book.save()

#         # assertion example ...
#         record = Book.objects.get(id=1)
#         self.assertEqual(record.author.name, "Mazuki Sekida")  
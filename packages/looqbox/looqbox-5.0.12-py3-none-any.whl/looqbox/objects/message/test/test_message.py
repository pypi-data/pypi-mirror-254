import unittest

from looqbox.objects.message.key import Key
from looqbox.objects.message.message import Message


@Key.delegate
class DelegationsTest:
    MY_KEY: str


class TestMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.message = Message()

    def test_offer_accepted(self):
        try:
            self.message[DelegationsTest.MY_KEY] = "test"
        except TypeError as e:
            self.fail("Typechecking failed: " + str(e))

    def test_offer_failed(self):
        self.assertRaises(TypeError, self.message.__setitem__, DelegationsTest.MY_KEY, 1)

    def test_key_querying(self):
        self.message[DelegationsTest.MY_KEY] = "test"
        my_key = self.message.get(DelegationsTest.MY_KEY)
        self.assertEqual(my_key, "test")

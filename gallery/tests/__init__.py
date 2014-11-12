from django.test import TestCase as BaseTestCase


class TestCase(BaseTestCase):

    def test_something(self):
        #raise NotImplementedError('Test not implemented. Bad developer!')
        self.failUnless(1 == 1)

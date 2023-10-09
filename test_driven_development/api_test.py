import unittest

from ns_api import NS_Services


class API_test_drive(unittest.TestCase):
    def test_create_pi(self):
        o_rest = NS_Services()
        result = o_rest.create_purchase_order(environ=2)
        self.assertEqual(result, 204)


if __name__ == '__main__':
    unittest.main()

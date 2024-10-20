import unittest
import my_app.main_v1_1 import suma

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(suma(1,2),3)



if __name__ == '__main__':
    unittest.main()
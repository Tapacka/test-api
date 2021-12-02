import unittest
from main import *
class def_testing(unittest.TestCase):
   
  def test_put_folder(self):
    
    self.assertEqual(put_folder('kk'), 201)
    self.assertEqual(put_folder('kk/bb'), 201)
    self.assertEqual(put_folder('kk'), 409)
    self.assertEqual(put_folder('несуществующий путь/ппп'), 409)
    


if __name__ == '__main__':
    unittest.main()
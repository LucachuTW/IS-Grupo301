import unittest
import houseModel


class testing(unittest.TestCase):
    def test_addDrug(self):
        # @SantiagoRR2004
        a = houseModel.HouseModel()
        number = a.getDrug()
        a.addDrug(3)
        self.assertEqual(a.getDrug(), number+3)
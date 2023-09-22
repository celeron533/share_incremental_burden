import unittest
from share_incremental_burden import redistribute_integer_dose_single_shot_by_weight, redistribute_integer_dose

class TestCase(unittest.TestCase):
    def test_redistribute_integer_dose_single_shot_by_weight(self):
        result = redistribute_integer_dose_single_shot_by_weight({'FLD_A':100, "FLD_B":200},30)
        print(result)
        self.assertDictEqual(result, {'FLD_A':110, 'FLD_B':220})

        result = redistribute_integer_dose_single_shot_by_weight({'FLD_A':100, "FLD_B":200},29)
        print(result)
        self.assertDictEqual(result, {'FLD_A':109, 'FLD_B':219})

        result = redistribute_integer_dose_single_shot_by_weight({'FLD_A':100, "FLD_B":200},28)
        print(result)
        self.assertDictEqual(result, {'FLD_A':109, 'FLD_B':218})

        result = redistribute_integer_dose_single_shot_by_weight({'FLD_A':100, "FLD_B":200},27)
        print(result)
        self.assertDictEqual(result, {'FLD_A':108, 'FLD_B':218})


    def test_redistribute_integer_dose(self):
        result = redistribute_integer_dose({'FLD_A':100, "FLD_B":200},30)
        print(result)
        self.assertDictEqual(result, {'FLD_A':110, 'FLD_B':220})

        result = redistribute_integer_dose({'FLD_A':100, "FLD_B":200},29)
        print(result)
        self.assertDictEqual(result, {'FLD_A':109, 'FLD_B':220})

        result = redistribute_integer_dose({'FLD_A':100, "FLD_B":200},28)
        print(result)
        self.assertDictEqual(result, {'FLD_A':109, 'FLD_B':219})

        result = redistribute_integer_dose({'FLD_A':100, "FLD_B":200},27)
        print(result)
        self.assertDictEqual(result, {'FLD_A':109, 'FLD_B':218})

if __name__ == '__main__':
    unittest.main()
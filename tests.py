import unittest
from s_p_box import substitute_byte, get_inverse_s_box, get_inverse_p_box, permutate_byte, S_BOX, P_BOX


class TestSubstitutionBox(unittest.TestCase):
    def test_substitute_byte(self):
        test_cases = [
            (0xD1, 0x3E),
            (0x08, 0x30),
            (0x40, 0x09),
            (0xFA, 0x2D),
            (0xDD, 0xC1)
        ]

        for input_byte, expected in test_cases:
            with self.subTest(input_byte=input_byte, test_cases=test_cases):
                substituted_byte = substitute_byte(input_byte, S_BOX)
                self.assertEqual(substituted_byte, expected)

    def test_inverse_substitute_byte(self):
        test_cases = [
            (0x3E, 0xD1),
            (0x30, 0x08),
            (0x09, 0x40),
            (0x2D, 0xFA),
            (0xC1, 0xDD)
        ]

        inv_s_box = get_inverse_s_box(S_BOX)

        for input_byte, expected in test_cases:
            with self.subTest(input_byte=input_byte, test_cases=test_cases):
                substituted_byte = substitute_byte(input_byte, inv_s_box)
                self.assertEqual(substituted_byte, expected)


class TestPermutationBox(unittest.TestCase):
    def test_permutate_byte(self):
        test_cases = [
            (0xD1, 0xD8),
            (0x08, 0x20),
            (0x40, 0x80),
            (0xFA, 0xF5),
            (0xDD, 0xFA)
        ]

        for input_byte, expected in test_cases:
            with self.subTest(input_byte=input_byte, test_cases=test_cases):
                permutated_byte = permutate_byte(input_byte, P_BOX)
                self.assertEqual(permutated_byte, expected)

    def test_inverse_permutate_byte(self):
        test_cases = [
            (0xD8, 0xD1),
            (0x20, 0x08),
            (0x80, 0x40),
            (0xF5, 0xFA),
            (0xFA, 0xDD),
        ]
        inv_p_box = get_inverse_p_box(P_BOX)

        for input_byte, expected in test_cases:
            with self.subTest(input_byte=input_byte, test_cases=test_cases):
                permutated_byte = permutate_byte(input_byte, inv_p_box)
                self.assertEqual(permutated_byte, expected)


if __name__ == '__main__':
    unittest.main()

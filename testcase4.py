import unittest

def alternate(s):
    max_length = 0
    letters = list(set(s))
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            first, second = letters[i], letters[j]
            filtered = [c for c in s if c == first or c == second]
            is_valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]: 
                    is_valid = False
                    break
            if is_valid:
                max_length = max(max_length, len(filtered))
    return max_length


class TestAlternate(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternate("ababababa"), 9)  
        self.assertEqual(alternate("cccc"), 0)      
        self.assertEqual(alternate("xyzxyz"), 4)      
        self.assertEqual(alternate("abcdabcd"), 4)   
        self.assertEqual(alternate("z"), 0)        
        self.assertEqual(alternate(""), 0)          
        self.assertEqual(alternate("xyxyxyxyxyxyxyxy"), 16) 
        self.assertEqual(alternate("dddddddddddddddddddd"), 0) 
        self.assertEqual(alternate("ab"), 2)
if __name__ == "__main__":
    unittest.main()
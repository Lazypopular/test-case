import unittest


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    for x in list(zip(*grid)):
        if list(x) != sorted(x):
            return "NO"
    return "YES"

class Test_gridChallenge(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(gridChallenge([]), "YES")
        self.assertEqual(gridChallenge(["abc"]), "YES")
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["bac", "def", "ghi"]), "NO")
        self.assertEqual(gridChallenge(["zzz", "zzz", "zzz"]), "YES")
        self.assertEqual(gridChallenge(["zyx", "wvu", "tsr"]), "NO")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl"]), "YES")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl", "mnop"]), "YES")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl", "mnop", "qrst"]), "YES")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx"]), "YES")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"]), "YES")
        self.assertEqual(gridChallenge(["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz", "a"]), "NO")

Test_gridChallenge()
print("All passed")

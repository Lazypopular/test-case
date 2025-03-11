import unittest
def caesarCipher(s, k):
    ans = ''
    k = k % 26 
    for i in s:
        if i.islower():
            ans += chr(((ord(i) - ord('a') + k) % 26) + ord('a'))
        elif i.isupper():
            ans += chr(((ord(i) - ord('A') + k) % 26) + ord('A'))
        else:
            ans += i 
    return ans

class Test_caesarCipher(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(caesarCipher("banana", 2), "dcpcpc")
        self.assertEqual(caesarCipher("tiger", 4), "xmkiw")
        self.assertEqual(caesarCipher("Welcome!", 0), "Welcome!")
        self.assertEqual(caesarCipher("Good Morning!", 7), "Nvvk Tvuypun!")
        self.assertEqual(caesarCipher("grape", 26), "grape")
        self.assertEqual(caesarCipher("Orange", 5), "Twdslj")
        self.assertEqual(caesarCipher("python", -5), "ktocji")
        self.assertEqual(caesarCipher("12345", 3), "12345")
        self.assertEqual(caesarCipher("Hello World!", 26), "Hello World!")
        self.assertEqual(caesarCipher("", 10), "")
        self.assertEqual(caesarCipher("abcXYZ", 30), "efgBCD")
        self.assertEqual(caesarCipher("abcXYZ", -30), "yzaVWX")
        self.assertEqual(caesarCipher("!@#$%^&*()", 10), "!@#$%^&*()")
        self.assertEqual(caesarCipher("AaBbCc", 1), "BbCcDd")
        self.assertEqual(caesarCipher("AaBbCc", 27), "BbCcDd")

Test_caesarCipher()
print("All passed")
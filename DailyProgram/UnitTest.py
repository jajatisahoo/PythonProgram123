import unittest
class calc(unittest.TestCase):

    def test_add(self,x,y):
        return self.x * self.y
obj = calc()
res = obj.test_add(5, 4)
print(res)
if __name__ == "__main__":
    unittest.main()

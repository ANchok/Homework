import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = Runner('First')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = Runner('First')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj1 = Runner('First')
        obj2 = Runner('Second')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == "__main__":
    unittest.main()
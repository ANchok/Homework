import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник' , 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_result.items():
            for k, v in value.items():
                value[k] = v.name
            print(cls.all_result[key])

    def test_tournament1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_result['test1'] = tournament.start()
        self.assertTrue(self.all_result['test1'].get(2).name, 'Ник')

    def test_tournament2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_result['test2'] = tournament.start()
        self.assertTrue(self.all_result['test2'].get(2).name, 'Ник')

    def test_tournament3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_result['test3'] = tournament.start()
        self.assertTrue(self.all_result['test3'].get(3).name, 'Ник')


if __name__ == "__main__":
    unittest.main()
import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = Runner('First')
        for i in range(5):
            obj.walk()
        self.assertEqual(obj.distance, 25)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj = Runner('First')
        for i in range(5):
            obj.run()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = Runner('First')
        obj2 = Runner('Second', 10)
        for i in range(5):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_result['test1'] = tournament.start()
        self.assertTrue(self.all_result['test1'].get(2).name, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_result['test2'] = tournament.start()
        self.assertTrue(self.all_result['test2'].get(2).name, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_result['test3'] = tournament.start()
        self.assertTrue(self.all_result['test3'].get(3).name, 'Ник')
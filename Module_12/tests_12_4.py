import unittest
import logging
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj = Runner('First', -5)
            for i in range(5):
                obj.walk()
            self.assertEqual(obj.distance, 25)

            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj = Runner(14, 5)
            for i in range(5):
                obj.run()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = Runner('First')
        obj2 = Runner('Second', 10)
        for i in range(5):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} | {levelname} | {message}",
    style="{",
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)
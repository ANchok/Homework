import unittest
import tests_12_3


module12_ST = unittest.TestSuite()
module12_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
module12_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner_ = unittest.TextTestRunner(verbosity=2)
runner_.run(module12_ST)

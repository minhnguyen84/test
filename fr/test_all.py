import unittest

import fr.service_simple
import fr.service_api


class TestAll(unittest.TestCase):

    def test_all(self):
        testSuite = unittest.TestSuite()
        testResult = unittest.TestResult()
        testSuite.addTest(unittest.makeSuite(fr.service_simple.MotsInterditsSimpleServicesTest))
        testSuite.addTest(unittest.makeSuite(fr.service_api.MotsInterditsApiServicesTest))
        print(testResult.testsRun)  # prints 1 if run "normally"


if __name__ == "__main__":
    unittest.main()

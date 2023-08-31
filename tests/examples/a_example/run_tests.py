import unittest
...

from test.examples.a_example import tests_devprocess

suite = unittest.TestLoader().loadTestsFromModule(tests_devprocess)
unittest.TextTestRunner(verbosity=2).run(suite)

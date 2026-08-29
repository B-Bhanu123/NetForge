"""
NetForge Test Suite Runner
Runs all unit and integration test modules, reporting total executed assertions, duration, and pass status.
"""

import unittest
import sys
import os

def main():
    print("=" * 65)
    print("                NETFORGE AUTOMATED TEST SUITE RUNNER            ")
    print("=" * 65)
    
    loader = unittest.TestLoader()
    start_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tests"))
    suite = loader.discover(start_dir, pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 65)
    print(f"Total Tests Executed: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 65)
    
    if result.wasSuccessful():
        print("ALL TESTS PASSED SUCCESSFULLY!")
        return 0
    else:
        print("TEST SUITE FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())

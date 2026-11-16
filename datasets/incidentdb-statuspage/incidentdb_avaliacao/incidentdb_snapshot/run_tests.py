import unittest
import sys
from pathlib import Path

def main():
    print("=" * 70)
    print("IncidentDB Test Suite: Deterministic Quality & Census Verification")
    print("=" * 70)
    
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 70)
    if result.wasSuccessful():
        print(f"[PASS] All {result.testsRun} tests passed successfully with 0 failures and 0 errors.")
        sys.exit(0)
    else:
        print(f"[FAIL] Tests failed: {len(result.failures)} failures, {len(result.errors)} errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()

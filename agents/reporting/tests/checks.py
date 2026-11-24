"""A tiny helper so every test prints PASS / FAIL in the same simple way."""
import sys


class Checker:
    def __init__(self):
        self.total = 0
        self.failed = 0

    def check(self, name, condition, detail=""):
        """Print PASS or FAIL for one check. `detail` is shown only when it fails."""
        self.total += 1
        if condition:
            print(f"  PASS  {name}")
        else:
            self.failed += 1
            print(f"  FAIL  {name}  {detail}")

    def finish(self):
        """Print the summary and stop with an error code if something failed."""
        print(f"\n{self.total - self.failed} of {self.total} checks passed")
        sys.exit(1 if self.failed else 0)

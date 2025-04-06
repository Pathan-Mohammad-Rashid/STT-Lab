import os
import pytest

for i in range(1, 11):
    print(f"Run {i}:")
    os.system('pytest')
import sys
from src.brainfreak import brainfreak


with open(sys.argv[1]) as f:
    with open(sys.argv[2], "w") as out:
        out.write(brainfreak.brainfreak(f.read()))

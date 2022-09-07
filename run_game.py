# Check if user has correct version of Python
import sys

MIN_VER = (3, 10)

if sys.version_info[:2] < MIN_VER:
    sys.exit(
        "This game requires Python {}.{}.".format(*MIN_VER)
    )

# Run code
import src.main
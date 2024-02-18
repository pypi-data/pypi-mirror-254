"""Shared type definitions and constants."""
from typing import Any, Dict  # for type hinting

# Default maximum iterations
MAX_ITERATIONS = 25

# Default packet loss threshold
MAX_PACKET_LOSS = 0

# Defualt expected  maximum bitrate
INITIAL_BITRATE = 1e9

# Defualt Tolerated Frame Loss
TOLERATED_FRAME_LOSS = 1e-3

# Default test accuracy: 100Kb
TEST_ACCURACY = 1e5

# Default sleep time
SLEEP_TIME = 100

# Maximum number of retries on trial failure
MAX_RETRY_COUNT = 5

# Default duration of one trial
DEFAULT_TRIAL_DURATION = 60

# Type aliases
PortConfig = Dict[str, Any]

LOGGING_PREFIX = 'ByteBlower Test: '

DEFAULT_FRAME_CONFIG = [
    {
        "size": 60,
        "initial_bitrate": 3e8,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 3.7e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 124,
        "initial_bitrate": 6e8,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 4.5e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 252,
        "initial_bitrate": 8e8,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 5.7e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 508,
        "initial_bitrate": 8e8,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 6.6e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 1020,
        "initial_bitrate": 1e9,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 7.15e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 1276,
        "initial_bitrate": 1e9,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 7.25e8,
        "accuracy": TEST_ACCURACY
    }, {
        "size": 1514,
        "initial_bitrate": 1e9,
        "tolerated_frame_loss": TOLERATED_FRAME_LOSS,
        "expected_bitrate": 7.35e8,
        "accuracy": TEST_ACCURACY
    }
]


class TestProgress():

    def __init__(self, estimated_test_iterations):
        self.estimated_test_iterations = estimated_test_iterations
        self._current_iteration = 1

    def test_progress(
        self, estimated_test_iterations: int, current_test_iterations: int
    ) -> None:
        rate = round(
            current_test_iterations / estimated_test_iterations * 100, 2
        )
        # Clear screen before desplay progress bar?
        # run("clear")
        bar = "*" * int(rate)
        print(f"Estimated progress state {rate}%".center(100, " "))
        print(bar + "\n")

    def next_iteration(self):
        self.test_progress(
            self.estimated_test_iterations, self._current_iteration
        )
        self._current_iteration += 1

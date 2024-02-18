"""Exception related to the RFC 2544 throughput test implementation."""


class Rfc2544Exception(Exception):
    pass


# Exceptions related to misconfigured parameters
class ConfigFileError(Rfc2544Exception):
    pass


class InvalidInput(Rfc2544Exception):
    """
    Raised when the user provided invalid input values.

    .. versionchanged:: 1.0.0
       Improved exception handling.
    """


class FrameSizeMissing(ConfigFileError):

    def __init__(self):
        message = "Frame size missing"
        super().__init__(message)


class MissingParameter(ConfigFileError):
    """
    Raised when a configuration parameter is missing in the configuration file.

    .. versionadded:: 1.0.0
    """


class DiffSubnet(ConfigFileError):

    def __init__(self):
        message = "IP address and gateway are not in the same subnet"
        super().__init__(message)


# Exceptions That might occur during a trial
class TrialException(Rfc2544Exception):
    pass


class OtherTrialException(TrialException):

    def __init__(self, test_bitrate, frame_test_duration, frame_results):
        self.test_bitrate = test_bitrate
        self.frame_test_duration = frame_test_duration
        self.frame_results = frame_results
        super().__init__(test_bitrate, frame_test_duration, frame_results)


class MaxRetriesReached(TrialException):

    def __init__(self, frame_size, max_rety_count):
        message = f"Maximum number of retries reached ({max_rety_count}) on frame size {frame_size}."
        super().__init__(message)


# To be added later on
class DuplicateFrames(TrialException):

    def __init__(self, frame_size: int, dup: int):
        message = f"{dup} duplicate frames are detected for frame size {frame_size}"
        super().__init__(message)


class AllFramesLost(TrialException):

    def __init__(self, frame_size: int):
        message = f"Frame loss reached 100% on frame size {frame_size}. Check setup for eventual failures"
        super().__init__(message)


class PortLayer3Mismatch(TrialException):

    def __init__(self):
        message = "Source and destination ports IP version is different"
        super().__init__(message)

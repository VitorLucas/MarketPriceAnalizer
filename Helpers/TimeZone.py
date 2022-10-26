import time
class TimeZone:

    @staticmethod
    def generate_timeZone():
        timezone = 60 * 60 * 1  # seconds * minutes * utc + 1
        return (int(time.time() + timezone)) * 1000
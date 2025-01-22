# rate limt of 10 seconds

# initialize Logger with a hashtable
class Logger:
    def __init__(self):
        self.lookup = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        # check if message is in table
        if message not in self.lookup:
            self.lookup[message] = timestamp
            return True
        # check for last occurance
        if timestamp < (self.lookup[message] + 10):
            return False
        self.lookup[message] = timestamp
        return True


logger = Logger()

# Logging a message at timestamp 1
print(logger.should_print_message(1, "foo"))  # True

# Logging the same message at timestamp 2
print(logger.should_print_message(2, "foo"))  # False

# Logging a new message at timestamp 3
print(logger.should_print_message(3, "bar"))  # True

# Logging the first message again at timestamp 11
print(logger.should_print_message(11, "foo"))  # True
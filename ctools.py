import sys
class util:
    def print(d):
        sys.stdout.write(d)
        sys.stdout.flush()

    def load(k):
        return " ".join(open(k, "r+").readlines())
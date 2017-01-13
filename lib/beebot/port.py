import threading
import collections


class _ExpectationQueue:

    def __init__(self):
        self._cv = threading.Condition()
        self._queue = collections.deque()

    def produce(self, message):
        with self._cv:
            self._queue.appendleft(message)
            self._cv.notify_all()

    def consume(self, matcher):
        with self._cv:
            while not self._queue or self._queue[-1] != matcher:
                self._cv.wait()
            self._queue.pop()


class InputPort:

    def __init__(self, stream, encoder):
        self._stream = stream
        self._encoder = encoder

    def send(self, message):
        encoded = self._encoder.encode(message)
        self._stream.write(encoded)
        self._stream.flush()


class OutputPort:

    def __init__(self, stream, decoder):
        self._stream = stream
        self._decoder = decoder
        self._expectation_queue = _ExpectationQueue()
        self._reading_thread = threading.Thread(target=self._read, daemon=True)
        self._reading_thread.start()

    def _read(self):
        while True:
            message = self._decoder.decode(self._stream)
            self._expectation_queue.produce(message)

    def receive(self, matcher):
        self._expectation_queue.consume(matcher)

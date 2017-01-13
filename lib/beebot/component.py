import threading
import subprocess

from beebot.port import InputPort, OutputPort


class Program:

    def start(self):
        self._proc = subprocess.Popen(self.executable_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._async_tasks = []

    def run(self, task):
        task(self)

    def run_async(self, task):
        t = threading.Thread(target=task, args=[self])
        t.start()
        self._async_tasks.append(t)

    def done(self):
        for t in self._async_tasks:
            t.join()

    @property
    def stdin(self):
        return InputPort(self._proc.stdin, self.stdin_encoder)

    @property
    def stdout(self):
        return OutputPort(self._proc.stdout, self.stdout_decoder)

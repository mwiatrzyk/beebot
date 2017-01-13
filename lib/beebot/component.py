import subprocess

from beebot.port import InputPort, OutputPort


class Program:

    def start(self):
        self._proc = subprocess.Popen(self.executable_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def run(self, task):
        task(self)

    def done(self):
        pass

    @property
    def stdin(self):
        return InputPort(self._proc.stdin, self.stdin_encoder)

    @property
    def stdout(self):
        return OutputPort(self._proc.stdout, self.stdout_decoder)

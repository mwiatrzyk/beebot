from beebot.component import Program
from beebot.filesystem import path


class Encoder:

    def encode(self, message):
        operator = message['operator']
        args = ' '.join(str(x) for x in message['args'])
        return ('%s %s\n' % (operator, args)).encode()


class Decoder:

    def decode(self, stream):
        result = stream.readline().strip()
        if b'.' in result:
            result = float(result)
        else:
            result = int(result)
        return {'result': result}


class Calculate(Program):

    @property
    def executable_path(self):
        return path.join('testing', 'bin', 'calculate.py')

    @property
    def stdin_encoder(self):
        return Encoder()

    @property
    def stdout_decoder(self):
        return Decoder()

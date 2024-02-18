import socket

class RSCPy:
    def __init__(self, ip, port=61000, tcp_port=61001, protocol='UDP'):
        self.ip = ip
        self.port = port
        self.tcp_port = tcp_port
        self.protocol = protocol

    def send_command(self, command, expect_response=False):
        if self.protocol.upper() == 'UDP':
            return self.send_udp(command)
        elif self.protocol.upper() == 'TCP':
            return self.send_tcp(command, expect_response)

    def send_udp(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(command.encode('utf-8'), (self.ip, self.port))

    def send_tcp(self, command, expect_response=False):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.ip, self.tcp_port))
            sock.send(command.encode('utf-8'))
            if expect_response:
                response = sock.recv(4096)
                return response.decode('utf-8')

    def open_presentation(self, filename):
        self.send_command(f'OPEN "{filename}"')

    def close_presentation(self, filename=None):
        if filename:
            self.send_command(f'CLOSE "{filename}"')
        else:
            self.send_command('CLOSE')

    def run_presentation(self, filename=None):
        if filename:
            self.send_command(f'RUN "{filename}"')
        else:
            self.send_command('RUN')

    def run_current(self):
        self.send_command('RUNCURRENT')

    def stop_presentation(self, filename=None):
        if filename:
            self.send_command(f'STOP "{filename}"')
        else:
            self.send_command('STOP')

    def prev_slide(self):
        self.send_command('PREV')

    def next_slide(self):
        self.send_command('NEXT')

    def go_to_slide(self, slide):
        self.send_command(f'GO {slide}')

    def set_background(self):
        self.send_command('SETBG')

    def find_files(self, path):
        response = self.send_command(f'FIND "{path}"', expect_response=True)
        if response:
            return response.split('\n')
        return []
    
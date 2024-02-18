import threading
from datetime import datetime


class ConsoleFileDualWriter:
    def __init__(self, service, stdout):
        self.__lock = threading.Lock()
        current_file = self.get_file_path(service)
        self.current_file = current_file
        self.file = open(current_file, 'a')
        self.initialize_file_header()
        self.stdout = stdout
        self.service = service

    def write(self, line):
        self.rotate_file()
        self.file.write(line)
        self.stdout.write(line)

    def flush(self):
        self.file.flush()
        self.stdout.flush()

    def isatty(self):
        return False

    def get_file_path(self, service):
        time = str(datetime.now())
        time = time.replace('-', '').replace(':', '').replace(' ', '')[0:11] + '0'

        file_name = service.get_configuration('observability.stdout').replace('{TIME}', time)
        return service.get_configuration('observability.path') + '/' + file_name

    def rotate_file(self):
        with self.__lock:
            new_file = self.get_file_path(self.service)
            if new_file != self.current_file:
                self.current_file = new_file
                self.file.flush()
                self.file = open(self.current_file, 'a')

                self.initialize_file_header()

    def initialize_file_header(self):
        self.file.write("------------------------------------------------------------\n"
                        "Language: Python\nFormat: FastAPI\n"
                        "------------------------------------------------------------"
                        "\n\n\n")

import time
import os

from command import Connection


class Sender(object):
    def __init__(self):
        self.host = '192.168.137.111'
        self.port = 2112
        self.c = None
        self.data = []
        self.open_file()
        self.send()

    def send(self):
        for command in self.data:
            try:
                action, value = command.split(":")
                value = value.strip()
                print("Performing AUTORUN {} {}".format(action, value))
                if action == "PAUSE":
                    print("Sleeping for {} seconds".format(value))
                    time.sleep(float(value))
                else:
                    self.c = Connection()
                    self.c.create()
                    self.c.connect(host=self.host, port=self.port)
                    rtn_data = self.c.send(command)
                    print(rtn_data)
            except Exception as e:
                print("Exception ".format(e))

    def open_file(self):
        cwd = os.getcwd()
        filename = "autorun.ini"
        path = os.path.join(cwd, filename)
        try:
            with open(path, 'r') as reader:
                for cnt, line in enumerate(reader):
                    if not line.startswith("#"):
                        self.data.append(line)
                        cnt += 1
        except Exception as e:
            print("Error: {}", format(e))


if __name__ == "__main__":
    s = Sender()

class Sequencer:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        self.line = self.file.readline()
        self.line_number = 0
    

    
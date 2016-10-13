class Measure(object):
    def __init__(self):
        self.sum_of_duration = 0
        self.measure = []

    def add_note(self, note):
        self.measure.append(note)
        self.sum_of_duration += note.duration

    def flush(self):
        self.measure.clear()
        self.sum_of_duration = 0

    def msr_print(self):
        print("--------")
        for note in self.measure:
            print(note)
        print("--------")
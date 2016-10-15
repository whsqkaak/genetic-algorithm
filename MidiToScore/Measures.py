class Measure(object):
    def __init__(self):
        self.sum_of_duration = 0
        self.measure = []
        # 유전 알고리즘으로 생성한 코드
        self.chord

    def add_note(self, note):
        self.measure.append(note)
        self.sum_of_duration += note.duration

    def msr_print(self):
        print("--------")
        for note in self.measure:
            print(note)
        print("--------")
class Measure(object):
    def __init__(self):
        self.sum_of_duration = 0
        self.measure = []
        # 유전 알고리즘으로 생성한 코드
        self.chord = None

    def add_note(self, note):
        self.measure.append(note)
        self.sum_of_duration += note.duration

    # 유전 알고리즘으로 생성한 코드를 삽입하는 메소드
    def add_chord(self, chord):
        self.chord = chord

    def print_msr(self):
        print("--------")
        if self.chord is not None:
            print(self.chord.print_chord())
        for note in self.measure:
            print(note)
        print("--------")
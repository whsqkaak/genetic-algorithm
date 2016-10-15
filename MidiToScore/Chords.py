from MidiToScore.Notes import Note


class Chord(object):
    def __init__(self, chord_duration):
        self.notes = []
        self.chord_duration = chord_duration
        self.chord_num = 0

    def generate_chord(self, chord_num):
        self.chord_num = chord_num
        if chord_num == 1:
            self.notes.append(Note(False, 48, self.chord_duration))
            self.notes.append(Note(False, 52, self.chord_duration))
            self.notes.append(Note(False, 55, self.chord_duration))
        elif chord_num == 2:
            self.notes.append(Note(False, 50, self.chord_duration))
            self.notes.append(Note(False, 53, self.chord_duration))
            self.notes.append(Note(False, 57, self.chord_duration))
        elif chord_num == 3:
            self.notes.append(Note(False, 52, self.chord_duration))
            self.notes.append(Note(False, 55, self.chord_duration))
            self.notes.append(Note(False, 59, self.chord_duration))
        elif chord_num == 4:
            self.notes.append(Note(False, 53, self.chord_duration))
            self.notes.append(Note(False, 57, self.chord_duration))
            self.notes.append(Note(False, 60, self.chord_duration))
        elif chord_num == 5:
            self.notes.append(Note(False, 55, self.chord_duration))
            self.notes.append(Note(False, 59, self.chord_duration))
            self.notes.append(Note(False, 62, self.chord_duration))
        elif chord_num == 6:
            self.notes.append(Note(False, 57, self.chord_duration))
            self.notes.append(Note(False, 60, self.chord_duration))
            self.notes.append(Note(False, 64, self.chord_duration))
        elif chord_num == 7:
            self.notes.append(Note(False, 59, self.chord_duration))
            self.notes.append(Note(False, 62, self.chord_duration))
            self.notes.append(Note(False, 65, self.chord_duration))

    def chord_print(self):
        print('chord_num: %d' % self.chord_num)
        print('chord_dur: %d' % self.chord_duration)
        print('chord')
        for note in self.notes:
            print(note)
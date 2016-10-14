from MidiToScore.Notes import Note
from MidiToScore.Measures import Measure
from Chords import Chord


class ScoreWriter(object):
    def __init__(self):
        self.diatonic_chords = []
        self.dur_by_denominator = {'4': 480, '8': 240}
        self.dur_per_msr = 0
        self.score = []
        self.time_sign = {}

    def scr_print(self):
        for measure in self.score:
            measure.msr_print()

    def write(self, midi):
        for i, track in enumerate(midi.tracks):
            # 트랙 정보 출력
            print('Track {} : {}'.format(i, track.name))
            for message in track:
                # 곡의 박자 저장
                if message.type == 'time_signature':
                    self.time_sign['denominator'] = message.denominator
                    self.time_sign['numerator'] = message.numerator
                    break
            dur_of_denominator = self.dur_by_denominator[str(self.time_sign['denominator'])]
            self.dur_per_msr = self.time_sign['numerator'] * dur_of_denominator
            # 마디 생성
            new_measure = Measure()
            for message in track:
                # 마디가 완성됐을 때 혹은 악보가 끝났을 때 마디를 악보에 저장 후 초기화
                if new_measure.sum_of_duration == self.dur_per_msr \
                        or message.type == 'end_of_track':
                    # 악보의 끝일 떄
                    if new_measure.sum_of_duration < self.dur_per_msr:
                        last_note = Note(True, 0, self.dur_per_msr - new_measure.sum_of_duration)
                        new_measure.add_note(last_note)
                    # 마디를 악보에 저장
                    self.score.append(new_measure)
                    # 마디 초기화
                    new_measure = Measure()
                # 음표를 마디에 저장
                if message.type == 'note_off':
                    new_note = Note(False, message.note, message.time)
                    new_measure.add_note(new_note)
                # 쉼표를 마디에 저장
                elif message.type == 'note_on' and message.time != 0:
                    new_note = Note(True, message.note, message.time)
                    new_measure.add_note(new_note)

    def create_diatonic_chords(self):
        for i in [1, 2, 3, 4, 5, 6, 7]:
            new_chord = Chord(self.dur_per_msr)
            new_chord.generate_chord(i)
            self.diatonic_chords.append(new_chord)
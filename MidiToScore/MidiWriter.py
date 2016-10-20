from mido import Message, MidiTrack


class MidiWriter(object):
    def __init__(self, midi_file):
        self.mid = midi_file
        self.track_of_chords = MidiTrack()

    def write(self, score_writer):
        self.mid.type = 1
        self.mid.tracks.append(self.track_of_chords)

        for message in score_writer.meta_message:
            if message.type == 'end_of_track':
                break
            self.track_of_chords.append(message)
        for measure in score_writer.score:
            chord = measure.chord
            for note in chord.notes:
                pitch = note.octave * 12 + note.pitch
                duration = chord.chord_duration
                if chord.notes.index(note) != 0:
                    self.track_of_chords.append(Message('note_on', note=pitch, time=0))
                else:
                    if score_writer.score.index(measure) != 0:
                        self.track_of_chords.append(Message('note_on', note=pitch, time=duration))
                    else:
                        self.track_of_chords.append(Message('note_on', note=pitch, time=0))
        self.track_of_chords.append(score_writer.meta_message[3])

    def save(self, path):
        self.mid.save(str(path))

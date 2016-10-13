class Note(object):
    def __init__(self, is_rest, note, duration):
        self.is_rest = is_rest
        self.pitch = note % 12
        self.octave = note // 12
        self.duration = duration

    def __str__(self):
        if self.is_rest:
            return "rest duration: %s" % str(self.duration)
        else:
            return "octave: %s, pitch: %s, duration: %s" \
                   % (str(self.octave), str(self.pitch), str(self.duration))
from mido import MidiFile
from MidiToScore.ScoreWriter import *
# main

# 미디 파일 읽음
midi = MidiFile('')

# ScoreWriter 객체 생성
score = ScoreWriter()
# 미디 파일의 정보를 ScoreWriter 객체의 형식에 맞춰 변형
score.write(midi)
# 악보 출력
# score.scr_print()

# 다이아토닉 코드 생성 확인용
# score.create_diatonic_chords()
# for chord in score.diatonic_chords:
#     chord.chord_print()


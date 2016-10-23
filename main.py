from mido import MidiFile

from MidiToScore.MidiWriter import *
from MidiToScore.ScoreWriter import *

from genetic.algorithm import *
from genetic.population import *
# main

# 미디 파일 읽음
midi = MidiFile('test.mid')

# ScoreWriter 객체 생성
score_writer = ScoreWriter()
# 미디 파일의 정보를 ScoreWriter 객체의 형식에 맞춰 변형
score_writer.write(midi)
# 악보 출력
#score_writer.scr_print()

# 다이아토닉 코드 생성
score_writer.create_diatonic_chords()
# 다이아토닉 코드 생성 확인용
# for chord in score_writer.diatonic_chords:
#     chord.print_chord()

# 유전 알고리즘을 사용해 코드 리스트 생성
population = Population(score_writer)
chords = GeneticAlgorithm(population).algorithm()

# # 테스트용 코드 measure 에 삽입
# for i, measure in enumerate(score_writer.score):
#     if i is 2:
#         measure.add_chord(score_writer.diatonic_chords[1])
#     else:
#         measure.add_chord(score_writer.diatonic_chords[0])

# 유전 알고리즘을 사용하여 만든 코드를 마디마다 삽입
for i, measure in enumerate(score_writer.score):
    measure.add_chord(chords[i])

# MidiWriter 객체 생성
midi_writer = MidiWriter(midi)
midi_writer.write(score_writer)
midi_writer.save('result.mid')

from mido import MidiFile

from MidiToScore.ScoreWriter import *
from MidiToScore.MidiWriter import *
import pygame


# main

# 미디 파일 읽음
midi = MidiFile('C:/Users/JmirS/Desktop/test.mid')

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

# 테스트용 코드 measure 에 삽입
for i, measure in enumerate(score_writer.score):
    if i is 2:
        measure.add_chord(score_writer.diatonic_chords[1])
    else:
        measure.add_chord(score_writer.diatonic_chords[0])

# MidiWriter 객체 생성
midi_writer = MidiWriter(midi)
midi_writer.write(score_writer)
midi_writer.save('C:/Users/JmirS/Desktop/result.mid')

# # Pygame mixer 모듈 초기화
# pygame.mixer.init()
#
# # 미디 파일을 로드하여 재생할 준비
# pygame.mixer.music.load('C:/Users/JmirS/Desktop/test.mid')
# # 재생
# pygame.mixer.music.play()
# # 재생 중 프로그램 종료를 방지
# while pygame.mixer.music.get_busy():
#     pygame.time.wait(1000)
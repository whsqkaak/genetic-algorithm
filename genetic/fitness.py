from MidiToScore.Chords import Chord


# 적응도 클래스
class Fitness(object):
	def __init__(self, pop):
		self.pop = pop  # Population 객체를 인수로 받음
		
	def fitness(self, chord_list):
		# 적응도 함수
		score = self.pop.scorewriter.score
		fit = 30
		f_chord = [4, 7, 7, 8, 8, 5, 5]  # 적응도 함수 요인별 적응도 가중치, 임의
		rate = self.rate_chord_num_1()  # 3. 반 종지 코드를 위한 비율
		for i in range(len(chord_list)):
			# 			1. 화성음의 비율
			for note in score[i / 2].measure:
				if self.pop.is_harmonic(chord_list, note):
					fit += f_chord[0] * note.duration
				
				# 			2. 종지 코드
			if i == len(chord_list) and chord_list[i].chord_num == 1:
				fit += f_chord[1]
			
			# 3. 반 종지 코드
			if rate >= 0.75:
				if i != len(chord_list) and chord_list[i].chord_num == 1:
					fit -= f_chord[2]
				
				#				4. 불안정한 / 안정적인 코드 진행
			if not (i == 0):  # 맨 처음과 마지막 경우 제외
				# 	불안정한 코드 진행
				if self.is_stable_chord(chord_list, i) == 2:
					fit -= f_chord[3]
				# 안정적인 코드 진행
				if self.is_stable_chord(chord_list, i) == 1:
					fit += f_chord[4]
				
				# 				5. 코드 간격
			if not (i == 0 or i == len(chord_list) - 1):
				dist_1 = chord_list[i].chord_num - chord_list[i - 1].chord_num
				dist_2 = chord_list[i + 1].chord_num - chord_list[i].chord_num
				if (dist_1 == 0 and dist_2 == 0) or (dist_1 == 1 and dist_2 == 1):
					fit -= f_chord[5]
		
		# 6. 반복 마디
		i = 0
		while i < len(chord_list):
			j = i
			while j < len(chord_list):
				if (score[i] == score[j]) or (score[i] == score[j + 1]) or (score[i + 1] == score[j]) or \
						(score[i + 1] == score[j + 1]):
					if chord_list[i] == chord_list[j]:
						fit += f_chord[6]
				j += 2
			i += 2
		if fit < 0:
			return 1
		return fit
	
	def rate_chord_num_1(self):
		# 	fitness 함수에서 3. 반종지 코드를 확인하기 위해 1음, 3음, 5음 즉 1화음이 score 에서 차지하는 비율을 구하는 함수
		score = self.pop.scorewriter.score
		chord = Chord(0)
		chord.generate_chord(1)  # 1 화음
		num_of_chord_1 = 0
		len_score = 0
		for m in score:
			for note in m.measure:
				if self.pop.is_harmonic(chord, note):
					num_of_chord_1 += 1
				len_score += 1
		return num_of_chord_1 / len_score
	
	@staticmethod
	def is_stable_chord(chord_list, i):
		# 불안정
		if (chord_list[i].chord_num == 5 and chord_list[i - 1].chord_num == 2) or \
				(chord_list[i].chord_num == 7 and chord_list[i - 1].chord_num == 2) or \
				(chord_list[i].chord_num == 5 and chord_list[i - 1].chord_num == 4) or \
				(chord_list[i].chord_num == 7 and chord_list[i - 1].chord_num == 4):
			return 2
		# 안정
		if (chord_list[i].chord_num == 2 and chord_list[i - 1].chord_num == 5) or \
			(chord_list[i].chord_num == 3 and chord_list[i - 1].chord_num == 6) or \
			(chord_list[i].chord_num == 6 and chord_list[i - 1].chord_num == 2) or \
			(chord_list[i].chord_num == 7 and chord_list[i - 1].chord_num == 3):
			return 1
		# no case
		return 0

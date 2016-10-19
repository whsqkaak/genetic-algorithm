from MidiToScore.Chords import Chord
import random


class GeneticAlgorithm:
	def __init__(self, scorewriter):
		self.scorewriter = scorewriter  # 생성 시 ScoreWriter 객체를 필드로 받아옴
		
	def population(self):
		# 초기 해집단 생성하는 함수
		s = self.scorewriter.score
		n = 100  # 개체군의 크기
		pop = [n][len(s) * 2]  # 개체군
		for i in range(n):
			for j in range(len(s)):
				c = random.choice(self.scorewriter.diatonic_chords)  # 임의의 다이아토닉 코드
				pop[i][j * 2] = c  # 선두 반 마디에 임의의 코드 대응
				k = self.len_nonharmonic(c, s[j])
				tension = s[j].sum_of_duration / 3
				if k < tension:
					pop[i][j * 2 + 1] = None
				else:
					pop[i][j * 2 + 1] = random.choice(self.scorewriter.diatonic_chords)
		return pop
	
	def fitness(self, chord_list):
		# 적응도 함수
		score = self.scorewriter.score
		fitness = 30
		f_chord = [4, 7, 7, 8, 8, 5, 5]  # 적응도 함수 요인별 적응도 가중치, 임의
		rate = self.rate_chord_num_1()  # 3. 반 종지 코드를 위한 비율
		for i in range(len(chord_list)):
			# 			1. 화성음의 비율
				for note in score[i/2].measure:
					if self.is_harmonic(chord_list, note):
						fitness += f_chord[0] * note.duration
						
			# 			2. 종지 코드
				if i == len(chord_list) and chord_list[i].chord_num == 1:
					fitness += f_chord[1]
					
			# 			3. 반 종지 코드
				if rate >= 0.75:
					if i != len(chord_list) and chord_list[i].chord_num == 1:
						fitness -= f_chord[2]
						
			#				4. 불안정한 / 안정적인 코드 진행
				if not (i == 0):  # 맨 처음과 마지막 경우 제외
					# 	불안정한 코드 진행
					if self.is_stable_chord(chord_list, i) == 2:
						fitness -= f_chord[3]
					# 	안정적인 코드 진행
					if self.is_stable_chord(chord_list, i) == 1:
						fitness += f_chord[4]
						
		# 				5. 코드 간격
				if not (i == 0 or i == len(chord_list)-1):
					dist_1 = chord_list[i].chord_num - chord_list[i-1].chord_num
					dist_2 = chord_list[i+1].chord_num - chord_list[i].chord_num
					if (dist_1 == 0 and dist_2 == 0) or (dist_1 == 1 and dist_2 == 1):
						fitness -= f_chord[5]
				
		# 				6. 반복 마디
		i = 0
		while i < len(chord_list)	:
			j = i
			while j < len(chord_list):
				if (score[i] == score[j]) or (score[i] == score[j+1]) or (score[i+1] == score[j]) or\
							(score[i+1] == score[j+1]):
					if chord_list[i] == chord_list[j]:
						fitness += f_chord[6]
				j += 2
			i += 2
		if fitness < 0:
			return 1
		return fitness
	
	def len_nonharmonic(self, chord, measure):
		# 후미 반 마디에서 chord 에 대한 비화성음들의 길이의 합을 구하는 함수
		m = measure.measure
		m = m[:(len(m) / 2)]  # 마디를 반으로 나눈다
		length = 0
		for note in m:
			if self.is_harmonic(chord, note):
				length += note.duration
		return length
	
	@staticmethod
	def is_harmonic(chord, note):
		# 화성음인지 아닌지 판별하는 함수
		if not note.is_rest:
			for i in chord.notes:
				if i.pitch == note.pitch:
					return True
		return False
	
	def rate_chord_num_1(self):
		# 	fitness 함수에서 3. 반종지 코드를 확인하기 위해 1음, 3음, 5음 즉 1화음이 score 에서 차지하는 비율을 구하는 함수
		score = self.scorewriter.score
		chord = Chord(0)
		chord.generate_chord(1)  # 1 화음
		num_of_chord_1 = 0
		len_score = 0
		for m in score:
			for note in m.measure:
				if self.is_harmonic(chord, note):
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

	def choose(self, pops):
		fitness_list = []
		for pop in pops:
			fitness_list.append(self.fitness(pop))
	# TODO : 선택 연산
	
	@staticmethod
	def cross(parent_1, parent_2):
		off_spring = []  # 자식 염색체 (코드 리스트)
		p = 50  # 교차 확률 (0 ~ 100 사이의 상수)
		is_parent_1 = 1  # 교차 시 어떤 부모의 염색체를 가져올지 판단하는 변수
		for i in range(len(parent_1)):
			if random.randrange(0, 101) < p:  # 교차 발생
				is_parent_1 = (is_parent_1 + 1) % 2
			if is_parent_1 == 1:
				off_spring[i] = parent_1[i]
			else:
				off_spring[i] = parent_2[i]
		return off_spring
				
	def mutation(self, off_spring):
		p = 15  # 변이 확률 (0 ~ 100 사이의 상수)
		for i in range(len(off_spring)):
			if random.randrange(0, 101) < p:  # 변이 발생
				off_spring[i] = random.choice(self.scorewriter.diatonic_chords)
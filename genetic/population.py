import random


# 초기 개체군 생성 클래스
class Population(object):
	def __init__(self, scorewriter):
		self.scorewriter = scorewriter  # 생성 시 ScoreWriter 객체를 필드로 받아옴
		self.n = 50  # 개체군의 크기
		
	def population(self):
		# 초기 해집단 생성하는 함수
		n = self.n
		s = self.scorewriter.score
		pop = [[0 for _ in range(len(s))] for _ in range(n)]  # 개체군
		for i in range(n):
			for j in range(len(s)):
				c = random.choice(self.scorewriter.diatonic_chords)  # 임의의 다이아토닉 코드
				pop[i][j] = c
		return pop
	
	@staticmethod
	def is_harmonic(chord, note):
		# 화성음인지 아닌지 판별하는 함수
		if not note.is_rest:
			for i in chord.notes:
				if i.pitch == note.pitch:
					return True
		return False
	
	def len_nonharmonic(self, chord, measure):
		# 후미 반 마디에서 chord 에 대한 비화성음들의 길이의 합을 구하는 함수
		m = measure.measure
		# m = m[:(len(m) / 2)]  # 마디를 반으로 나눈다   # org
		m = m[:(len(m) // 2)]  # 마디를 반으로 나눈다
		length = 0
		for note in m:
			if self.is_harmonic(chord, note):
				length += note.duration
		return length

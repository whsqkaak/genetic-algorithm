import random


class FirstPopulation:
	@staticmethod
	def len_nonharmonic(chord, measure):
		# 후미 반 마디에서 chord 에 대한 비화성음들의 길이의 합을 구하는 함수
		chord_notes = chord.notes
		m = measure.measure
		m = m[:(len(m)/2)]  # 마디를 반으로 나눈다
		length = 0
		for note in m:
			if not note.is_rest:
				for c_note in chord_notes:
					if c_note.pitch == note.pitch:
						length += note.duration
		return length
				
	def population(self, scorewriter):
		s = scorewriter.score
		n = 100  # 개체군의 크기
		pop = [n][len(s) * 2]   # 개체군
		for i in range(n):
			for j in range(len(s)):
				c = random.choice(scorewriter.diatonic_chords)  # 임의의 다이아토닉 코드
				pop[i][j*2] = c  # 선두 반 마디에 임의의 코드 대응
				k = self.len_nonharmonic(c, s[j])
				tension = s[j].sum_of_duration / 3
				if k < tension:
					pop[i][j*2+1] = None
				else:
					pop[i][j*2+1] = random.choice(scorewriter.diatonic_chords)
		return pop

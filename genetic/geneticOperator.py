import random


# 유전 알고리즘 연산자 클래스
class GeneticOperator(object):
	def __init__(self, fitness):
		self.fitness = fitness
		
	def select(self, pops):
		# 선택 연산자
		fitness_list = []
		for pop in pops:
			fitness_list.append(self.fitness.fitness(pop))
		select_list = GeneticOperator.make_select_list(fitness_list)
		parent = []
		parent[0] = random.choice(random.choice(select_list))
		parent[1] = random.choice(random.choice(select_list))
		return parent
	
	@staticmethod
	def make_select_list(fitness_list):
		#  fitness 만큼의 갯수를 가지는 리스트
		#  Let fitness[0] = 2, fitness[1] = 3
		#  tmp_list = [[0,0]
		# 						,[1,1,1]]
		#  select 시 fitness 에 비례해 선택할 수 있게 하기 위한 것
		tmp_list = []
		for i in range(len(fitness_list)):
			j = 0
			while j < fitness_list[i]:
				tmp_list[i][j] = i
				j += 1
		return tmp_list
	
	@staticmethod
	def cross(parent_1, parent_2):
		# 교차 연산자
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
	
	@staticmethod
	def mutation(self, off_spring):
		# 변이 연산자
		p = 15  # 변이 확률 (0 ~ 100 사이의 상수)
		for i in range(len(off_spring)):
			if random.randrange(0, 101) < p:  # 변이 발생
				off_spring[i] = random.choice(self.scorewriter.diatonic_chords)

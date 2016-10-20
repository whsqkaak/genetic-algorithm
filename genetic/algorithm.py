from genetic.fitness import Fitness
from genetic.geneticOperator import GeneticOperator


# 유전 알고리즘 클래스
class GeneticAlgorithm(object):
	
	def __init__(self, pop):
		self.population = pop
		self.fitness = Fitness(pop)
		self.operator = GeneticOperator(pop)
		
	def algorithm(self):
		# 1. 초기 개체군 생성
		pop = self.population.population()
		
		# 2. 각 개체군의 적응도를 리스트로 저장
		fit_list = []
		for i in range(len(pop)):
			fit_list.append(self.fitness.fitness(pop[i]))
			
		# 3. 유전 연산
		for i in range(100):  # 유전 연산 세대 숫자
			off_spring_list = []
			for j in range(self.population.n):
				selected = self.operator.select(fit_list)
				off_spring = (self.operator.cross(pop[selected[0]], pop[selected[1]]))
				self.operator.mutation(off_spring)
				off_spring_list.append(off_spring)
			pop = off_spring_list
		return pop

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
		big_fit = [0, 0]
		# 2. 유전 연산
		for i in range(500):  # 유전 연산 세대 숫자
			# 각 개체군의 적응도 리스트로 저장
			fit_list = []
			for m in range(len(pop)):
				fit = self.fitness.fitness(pop[m])
				if fit > 51:
					print("Enough Fitness : ", end=' ')
					for ch in pop[m]:
						print(ch.chord_num, end=' ')
					return pop[m]
				fit_list.append(fit)
				
			off_spring_list = []
			for j in range(self.population.n):
				selected = self.operator.select(fit_list)
				off_spring = (self.operator.cross(pop[selected[0]], pop[selected[1]]))
				self.operator.mutation(off_spring)
				off_spring_list.append(off_spring)
			pop = off_spring_list
			print(i+1, "th generation : ", end=' ')
			for k in pop:
				for j in k:
					print(j.chord_num, end=' ')
				print("   ", end='')
			print(" ")
			big_fit = self.operator.select(fit_list)
			
		big = (self.operator.cross(pop[big_fit[0]], pop[big_fit[1]]))
		print("LAST GENERATION : ", end=' ')
		for i in big:
			print(i.chord_num, end=' ')
		print("  ")
		return big

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import BitStringVectorNFlipMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker



class OneMaxEvaluator(SimpleIndividualEvaluator):
    def _evaluate_individual(self, individual):
        return sum(individual.vector)


algo = SimpleEvolution(
        Subpopulation(creators=GABitStringVectorCreator(length=1000),
                      population_size=300,
                      # user-defined fitness evaluation method
                      evaluator=OneMaxEvaluator(),
                      # minimization problem (fitness is MAE), so higher fitness is worse
                      higher_is_better=True,
                      elitism_rate=1/300,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.5, k=1),
                          BitStringVectorNFlipMutation(probability=0.2, probability_for_each=0.05, n=1000)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
                      ]
                      ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=500,

        termination_checker=ThresholdFromTargetTerminationChecker(optimal=1000, threshold=0.0),
        statistics=BestAverageWorstStatistics()
    )



# evolve the generated initial population
algo.evolve()
# Execute (show) the best solution
print(algo.execute())


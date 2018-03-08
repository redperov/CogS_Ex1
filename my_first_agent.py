# from pddlsim.local_simulator import LocalSimulator
# from random_walker import RandomExecutor
# domain_path = "domain.pddl"
# problem_path = "problem.pddl"
# print LocalSimulator().run(domain_path, problem_path, RandomExecutor())


from pddlsim.local_simulator import LocalSimulator
from pddlsim.executors.plan_dispatch import PlanDispatcher
domain_path = "domain.pddl"
problem_path = "problem.pddl"
print LocalSimulator().run(domain_path, problem_path, PlanDispatcher())

from Domains.Domain import Domain
from Model.Entity import Entity
from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem


class IPProblem(Problem):
    def __init__(self, domain: Domain):
        super().__init__(domain)
        pass
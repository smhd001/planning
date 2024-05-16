from Domains.Domain import Domain
from Model.Predicate import Predicate
from Problems.Problem import Problem
from Model.State import State
from Model.Entity import Entity


class Tire(Problem):
    def __init__(self, domain: Domain):
        super().__init__(domain)
        flat = Entity("Flat", "Tire")
        spare = Entity("Spare", "Tire")
        axle = Entity("Axle", "Location")
        trunk = Entity("Trunk", "Location")

        at_flat_axle = Predicate("At", [flat, axle])

        at_spare_trunk = Predicate("At", [spare, trunk])

        self.initial_state = State(
            "",
            [at_flat_axle, at_spare_trunk],
        )

        at_spare_axel = Predicate("At", [spare, axle])

        self.goal_state = State("", [at_spare_axel])

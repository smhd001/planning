from Domains.Domain import Domain
from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem


class Tiles(Problem):
    def __init__(self, domain: Domain):
        super().__init__(domain)
        on_0_11 = Predicate("On", [domain.Tile0, domain.p11])
        on_1_12 = Predicate("On", [domain.Tile1, domain.p12])
        on_2_13 = Predicate("On", [domain.Tile2, domain.p13])
        on_3_21 = Predicate("On", [domain.Tile3, domain.p21])
        on_4_22 = Predicate("On", [domain.Tile4, domain.p22])
        on_5_23 = Predicate("On", [domain.Tile5, domain.p23])
        on_6_31 = Predicate("On", [domain.Tile6, domain.p31])
        on_7_32 = Predicate("On", [domain.Tile7, domain.p32])
        on_8_33 = Predicate("On", [domain.Tile8, domain.p33])

        self.initial_state = State(
            "",
            [
                on_0_11,
                on_1_12,
                on_2_13,
                on_3_21,
                on_4_22,
                on_5_23,
                on_6_31,
                on_7_32,
                on_8_33,
            ],
        )

        on_1_11 = Predicate("On", [domain.Tile1, domain.p11])
        on_2_12 = Predicate("On", [domain.Tile2, domain.p12])
        on_5_13 = Predicate("On", [domain.Tile5, domain.p13])
        on_3_21 = Predicate("On", [domain.Tile3, domain.p21])
        on_4_22 = Predicate("On", [domain.Tile4, domain.p22])
        on_0_23 = Predicate("On", [domain.Tile0, domain.p23])
        on_6_31 = Predicate("On", [domain.Tile6, domain.p31])
        on_7_32 = Predicate("On", [domain.Tile7, domain.p32])
        on_8_33 = Predicate("On", [domain.Tile8, domain.p33])

        easy_goal = State(
            "",
            [
                on_1_11,
                on_2_12,
                on_5_13,
                on_3_21,
                on_4_22,
                on_0_23,
                on_6_31,
                on_7_32,
                on_8_33,
            ],
        )
        easy_goal

        on_1_11 = Predicate("On", [domain.Tile1, domain.p11])
        on_2_12 = Predicate("On", [domain.Tile2, domain.p12])
        on_5_13 = Predicate("On", [domain.Tile5, domain.p13])
        on_6_21 = Predicate("On", [domain.Tile6, domain.p21])
        on_3_22 = Predicate("On", [domain.Tile3, domain.p22])
        on_4_23 = Predicate("On", [domain.Tile4, domain.p23])
        on_7_31 = Predicate("On", [domain.Tile7, domain.p31])
        on_8_32 = Predicate("On", [domain.Tile8, domain.p32])
        on_0_33 = Predicate("On", [domain.Tile0, domain.p33])

        hard_goal = State(
            "",
            [
                on_1_11,
                on_2_12,
                on_5_13,
                on_6_21,
                on_3_22,
                on_4_23,
                on_7_31,
                on_8_32,
                on_0_33,
            ],
        )

        self.goal_state = easy_goal

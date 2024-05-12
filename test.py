from Planners.ForwardPlanner import ForwardPlanner
from Domains.BlockWorld import BlockDomain
from Problems.block import Block

for_planner = ForwardPlanner(Block(BlockDomain(3)))

print(for_planner.search())

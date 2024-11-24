from question1 import convert_to_dual
from question2 import is_a_feasable_region
from question3 import cs
from question4 import is_the_solution

q = [0,52.5,20]
primal_coef_constraints = [
    [5,2,2],
    [4,8,-8],
    [1,1,4],
]
primal_coef_objective = [1,4,2]
primal_bounds_constraints = [145.0, 260.0, 190.0]

dual = convert_to_dual(
    [ ["x1",0,"inf"], ["x2",0,"inf"], ["x3",0,"inf"] ],
    [ [primal_coef_constraints[0],"<=",primal_bounds_constraints[0]], [primal_coef_constraints[1],"<=",primal_bounds_constraints[1]], [primal_coef_constraints[2],"<=",primal_bounds_constraints[2]] ],
    primal_coef_objective
)
print(dual)

feasable_region = is_a_feasable_region(q, [ [primal_coef_constraints[0],"<=",primal_bounds_constraints[0]], [primal_coef_constraints[1],"<=",primal_bounds_constraints[1]], [primal_coef_constraints[2],"<=",primal_bounds_constraints[2]] ])
print(feasable_region)

y = cs(q, primal_bounds_constraints, primal_coef_constraints, primal_coef_objective)
print(y)

the_solution = is_the_solution(y, primal_bounds_constraints, primal_coef_objective, q)
print(the_solution)
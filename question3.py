import numpy as np

def cs(result_primal, objective_dual, coef_constraints, objective_primal):
    dual_slacks = objective_dual - np.dot(coef_constraints, result_primal)
    
    # We remove the coefs of the variable that are not equal to zero in the dual_slacks
    coef_constraints = np.array(coef_constraints)
    for i in range(len(dual_slacks)):
        if dual_slacks[i] != 0:
            coef_constraints = np.delete(coef_constraints, i, axis=0)
    coef_constraints = np.array(coef_constraints).T
    
    # We remove the lines that are equal to zero in the result_primal
    for i in range(len(result_primal)):
        if result_primal[i] == 0:
            coef_constraints = np.delete(coef_constraints, i, axis=0)
            objective_primal = np.delete(objective_primal, i, axis=0)

    # We resolve the system to obtain y
    y = np.linalg.solve(coef_constraints, objective_primal)
    
    for i in range(len(dual_slacks)):
        if dual_slacks[i] != 0:
            y = np.insert(y, i, 0, axis=0)
   
    return y
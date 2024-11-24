def convert_to_dual(variables, constraints, objectiveCoeffs):
    primal_num_vars = len(variables)
    primal_num_constraints = len(constraints)

    # Dual variables correspond to primal constraints
    dual_variables = [("y" + str(i + 1), 0, "inf") for i in range(primal_num_constraints)]

    # Dual objective coefficients come from primal constraint limits
    dual_objective_coeffs = [constraint[2] for constraint in constraints]

    # Dual constraints correspond to primal variables
    dual_constraints = []
    for j in range(primal_num_vars):
        dual_coefs = [constraint[0][j] for constraint in constraints]
        if variables[j][1] >= 0:  # If primal variables are non-negative
            dual_constraints.append((dual_coefs, ">=", objectiveCoeffs[j]))
    
    return (dual_variables,dual_constraints,dual_objective_coeffs)

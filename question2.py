def is_a_feasable_region(point, constraints):
    for constraint in constraints:
        coefficients, relation, value = constraint
        
        result = sum(point[i] * coefficients[i] for i in range(len(point)))
        
        if relation == ">=" and not (result >= value):
            return False
        elif relation == "<=" and not (result <= value):
            return False
        elif relation == "==" and not (result == value):
            return False
    return True
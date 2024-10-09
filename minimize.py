# import pulp

# # Create a problem instance with the objective to minimize loss
# prob = pulp.LpProblem("Minimize_Loss", pulp.LpMinimize)

# # Define variables with non-negative integer constraints
# x = pulp.LpVariable('x', lowBound=0, cat='Integer')
# y = pulp.LpVariable('y', lowBound=0, cat='Integer')

# length = 2960
# b1_length = 281
# b2_length = 170

# b1_length +=5
# b2_length +=5

# # Define the loss as the difference
# loss = length - (b1_length * x + b2_length * y)

# # Objective: minimize the loss
# prob += loss, "Objective"

# # Constraint: keep the sum below or equal to 2937
# prob += (b1_length * x + b2_length * y) <= length

# # Solve the problem
# prob.solve()

# # Display the results
# x_value = pulp.value(x)
# y_value = pulp.value(y)
# minimized_value = b1_length * x_value + b2_length * y_value

# print("Optimal values found:")
# print(f"x = {x_value}")
# print(f"y = {y_value}")
# print(f"Minimized value of the expression = {minimized_value}")
# print(f"Loss (difference from 2937) = {length - minimized_value}")


def calculate_waste(total_length, cuts):
    used_length = sum(cuts)
    return total_length - used_length

def maximize_units_and_minimize_waste(available_length, required_u, length_u, required_v, length_v, max_cuts):
    total_waste = float('inf')
    best_combination = (0, 0)  # (units of Steel U, units of Steel V)
    
    # Try all possible combinations of units to fulfill
    for u_units in range(required_u + 1):
        for v_units in range(required_v + 1):
            # Calculate total length needed
            total_needed_length = (u_units * length_u) + (v_units * length_v)
            if total_needed_length <= available_length:
                # Calculate waste
                waste = calculate_waste(available_length, [length_u]*u_units + [length_v]*v_units)
                
                # Update best combination if this has less waste or equal waste with more units
                if (waste < total_waste) or (waste == total_waste and (u_units + v_units) > sum(best_combination)):
                    total_waste = waste
                    best_combination = (u_units, v_units)
    
    return best_combination, total_waste

# Example Usage
available_length = 1000  # Total available length of steel
required_u = 48          # Required units of Steel U
length_u = 20            # Length per unit of Steel U
required_v = 12          # Required units of Steel V
length_v = 30            # Length per unit of Steel V
max_cuts = 12            # Maximum cuts allowed in one iteration

result, waste = maximize_units_and_minimize_waste(available_length, required_u, length_u, required_v, length_v, max_cuts)
print(f"Best combination: {result[0]} units of Steel U and {result[1]} units of Steel V with total waste: {waste}")

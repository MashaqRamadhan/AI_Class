    closest_value = x[0]  
    closest_distance = abs(x[0] - y_target) + abs(x[0] ** 2 - y2_target)  
    for value in x:
        y = value
        y2 = value ** 2
        distance = abs(y - y_target) + abs(y2 - y2_target)  
        
        if distance < closest_distance:
            closest_value = value
            closest_distance = distance

    return closest_value  

x = [5, 5, 10, 3, 2, 6, 7]

y_target = 4
y2_target = 2

result = heuristic_search(x, y_target, y2_target)
print("Nilainya berada pada indeks ke:", result)

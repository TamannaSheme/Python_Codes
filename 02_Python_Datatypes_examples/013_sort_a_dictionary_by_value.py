# Example 1: Sort the dictionary based on values

dt = {7:8, 1:9, 6:3}

sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dt)

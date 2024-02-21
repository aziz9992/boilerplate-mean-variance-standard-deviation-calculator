import numpy as np

def calculate(list):
    if len(list) < 9:
            raise ValueError("List must contain nine numbers.")

    def calculate_stats(data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = variance ** 0.5
        return [mean, variance, std_dev, max(data), min(data), sum(data)]

    calculations = {
        'mean': [calculate_stats(list[i:i+3])[0] for i in range(0, len(list), 3)],
        'variance': [calculate_stats(list[i:i+3])[1] for i in range(0, len(list), 3)],
        'standard deviation': [calculate_stats(list[i:i+3])[2] for i in range(0, len(list), 3)],
        'max': [calculate_stats(list[i:i+3])[3] for i in range(0, len(list), 3)],
        'min': [calculate_stats(list[i:i+3])[4] for i in range(0, len(list), 3)],
        'sum': [calculate_stats(list[i:i+3])[5] for i in range(0, len(list), 3)]
    }
    return calculations
# Test the function
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(test_list))
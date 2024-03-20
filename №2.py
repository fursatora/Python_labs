import re
def evaluate_polynomial(coefficients,degrees, x):
    result = 0
    for i in range(len(degrees)):
        result += coefficients[i] * (pow(x,degrees[i]))
    result += coefficients[len(degrees)]
    return result
def read_polynomial(filename):
    with open(filename, 'r') as file:
        polynomial_str = file.readline().strip()

    degree_pattern = r'\^(\d+)\s*[+-]'
    all_degrees = re.findall(degree_pattern, polynomial_str)
    degree=max(all_degrees)

    coefficients_pattern = re.findall(r'(?<!\^)(-?\d+)', polynomial_str)
    coefficients = []
    degrees=[]
    for term in coefficients_pattern:
        coef_str = term
        if (coef_str):
            coef = int(coef_str)
            coefficients.append(coef)

    for term in all_degrees:
        degr_str = term
        if (degr_str):
            degr = int(degr_str)
            degrees.append(degr)

    return coefficients, degree, degrees

def write_polynomial_values(filename, coefficients,degrees, a, b):
    with open(filename, 'a') as file:
        file.write("\n[{}, {}]:\n".format(a, b))
        file.write("x\t\ty\n")
        for x in range(a, b + 1):
            y = evaluate_polynomial(coefficients, degrees, x)
            file.write("{}\t\t{}\n".format(x, y))

filename = "polynomial.txt"
a = 0
b = 10

coefficients, degree,degrees= read_polynomial(filename)
print("Степень многочлена:", degree)
print("Коэффициенты многочлена:", coefficients)

write_polynomial_values(filename, coefficients,degrees, a, b)

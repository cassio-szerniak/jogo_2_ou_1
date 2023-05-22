# Procedural approach

# TESTANDO O GIT NO VSCODE DENTRO DO WSL-LINUX
# COPIEI A PASTA DO PROJETO PRA DENTRO DO LINUX-WSL E ACHO QUE OS PARAMETROS DO GIT FORAM JUNTO
# CAUSANDO UMA PERCEPÇÃO DAS MUDANÇAS, PORÉM TENHO QUE LOGAR NO GITHUB NESTE AMBIENTE

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print("Procedural Approach:")
print("Area:", area)
print("Perimeter:", perimeter)

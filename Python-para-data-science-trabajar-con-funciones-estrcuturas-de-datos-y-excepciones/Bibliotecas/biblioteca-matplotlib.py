import matplotlib.pyplot as plt # otra forma de importar

from matplotlib import pyplot as plt # una forma de importar 

estudiantes = ['Juan', 'Pedro', 'Maria', 'Ana']
notas = [8, 9, 7, 10]

plt.bar(x=estudiantes, height=notas) # x = estudiantes, height = notas
plt.show() # muestra la grafica



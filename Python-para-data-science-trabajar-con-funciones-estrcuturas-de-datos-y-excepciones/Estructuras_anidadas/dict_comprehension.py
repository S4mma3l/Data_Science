lista_completa = [[['juan', 'j259'], ['maria', 'm829'], ['pedro', 'p874'], ['luisa', 'l61']], 
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], 
                  [9.0, 7.3, 5.8, 6.7, 8.5], 
                  ['Aprobado(a)', 'Reprobado(a)', 'Reprobado(a)', 'Reprobado(a)', 'Aprobado(a)']]

columnas = ['notas', 'promedio_final', 'situacion']
print(columnas)

registro = {columnas[i]: lista_completa[i+1] for i in range(len(columnas))}
print(registro)

registro = {'estudiante': [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]}
print(registro)


nombres_estudiantes = ["Enrique Montero", "Luna Pereira", "Anthony Silva", "Leticia Fernandez", 
                       "Juan González", "Maira Caldera", "Diana Carvajo", "Mariana Rosas", "Camila Fernandez", 
                       "Levi Alves", "Nicolás Rocha", "Amanda Navas",  "Lara Morales", "Leticia Olivera", "Lucas Navas", 
                       "Lara Arteaga", "Beatriz Martinez", "Victor Acevedo", "Stephany Hernández", "Gustavo Lima"]

medias_estudiantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 9.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 10.0, 8.2]

# becados = {nombres_estudiantes: medias_estudiantes for i in range(len(medias_estudiantes)) if medias_estudiantes[i] >= 9.0}
# becados = {nombres_estudiantes: media for media in medias_estudiantes if media >= 9.0}
becados = {nombre: media for nombre, media in zip(nombres_estudiantes, medias_estudiantes) if media >= 9.0}
print(becados)
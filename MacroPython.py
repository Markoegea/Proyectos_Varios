from datetime import date
import os
nombreCarpeta = f'Clase_{date.today().day}_{date.today().month}_{date.today().year}'
directorio = "./Documents/HTML/Ciclo_3/"+nombreCarpeta
carpetaImg = directorio + "/Img"
carpetaStyle = directorio + "/CSS"
carpetaJS = directorio + "/JS"
todas = [directorio,carpetaImg,carpetaStyle,carpetaJS]
for i in todas:
    os.mkdir(i)
archivoHTML = open(directorio+"/main.html", "at")
archivoHTML.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>''')
archivoCSS = open(carpetaStyle+"/style.css", "at")
archivoJS = open(carpetaJS+"/ScriptMain.js", "at")


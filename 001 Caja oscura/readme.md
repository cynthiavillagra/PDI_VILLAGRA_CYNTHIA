# 001 - Caja Oscura

Este trabajo corresponde al primer módulo práctico de la materia **Técnicas de Procesamiento de Imágenes**, dictada por el profesor **Matías Barreto** en el IFTS N.º 24, carrera **Ciencia de Datos e Inteligencia Artificial**, año 2025.

---

## 📦 Contenido de la carpeta

- 📸 Fotografías del proceso de armado de la cámara oscura.
- 📄 Archivo `caja oscura.pptx` con instrucciones del desafío, conceptos teóricos y reflexiones sobre el fenómeno óptico.

---

## 🧪 ¿Qué es este proyecto?

La actividad consistió en construir una **cámara oscura funcional** utilizando materiales simples (una caja, papel aluminio, cinta adhesiva, etc.). El objetivo fue observar cómo se forma una imagen a través de un orificio y comprender los principios ópticos que fundamentan la captura y procesamiento de imágenes digitales.

---

## ❓ Respuestas a las preguntas propuestas por el profesor

### 📌 ¿Cómo afecta el tamaño del agujero a la imagen (brillo vs. nitidez)?

- Un **agujero más pequeño** genera una imagen **más nítida**, pero también **más oscura**, ya que deja pasar menos luz.
- Un **agujero más grande** permite una imagen **más brillante**, pero también **más borrosa**, ya que la luz entra desde más ángulos.

### 📌 ¿Qué pasa si la caja no está completamente sellada?

- Si entra luz por otras aberturas, la imagen proyectada **pierde contraste** y puede verse difusa o poco clara.
- La oscuridad total en el interior de la caja es esencial para que la proyección sea visible.

### 📌 ¿Cómo podemos mejorar la calidad de la imagen?

- Asegurarse de que la caja esté **completamente sellada** para evitar filtraciones de luz.
- Usar un **papel negro o aluminio** en el interior para mejorar el contraste.
- **Reducir el tamaño del orificio** lo más posible sin eliminar totalmente la luz.
- **Proyectar hacia una superficie blanca o semitranslúcida** (como papel vegetal) para mayor definición.

---

## 🧠 Teoría vinculada proporcionada por el profesor

### 🔭 Formación de la Imagen por Proyección Rectilínea

La luz viaja en línea recta. Cada punto de la escena emite luz que atraviesa el orificio y forma un punto correspondiente en la imagen proyectada dentro de la caja.

### 🔘 Relación Apertura - Profundidad de Campo

El tamaño del orificio controla la **nitidez** (profundidad de campo) y el **brillo** de la imagen:
- Agujero pequeño → imagen más nítida pero menos luminosa.
- Agujero grande → imagen más brillante pero borrosa.

Este principio también es clave en la construcción de lentes y sensores modernos.

### 🔄 Inversión de la Imagen / Transformación Geométrica

La imagen proyectada está **invertida vertical y horizontalmente**. Este fenómeno es una **transformación geométrica básica**, muy importante en procesamiento digital de imágenes.

### 🧩 Discretización Espacial Implícita

Aunque no es digital, la imagen que se forma está compuesta por una **cantidad finita de puntos de luz**, lo que representa una versión primitiva del concepto de **píxeles**.

### 💡 Intensidad Lumínica y Representación Digital

La **intensidad de la luz en cada punto** es la base de toda representación digital. Esa luz, al ser capturada por sensores, se convierte en **niveles de gris o color**, que forman la imagen digital.

---

## 👤 Autoría

- Autor/a: Cynthia Villagra
- Año: 2025  
- Materia: Técnicas de Procesamiento de Imágenes  
- Profesor: Matías Barreto (GitHub: [@mattbarreto](https://github.com/mattbarreto))  
- Carrera: Ciencia de Datos e Inteligencia Artificial – IFTS 24

---

## 📄 Licencia

Este proyecto se encuentra bajo la licencia [MIT](https://opensource.org/licenses/MIT).

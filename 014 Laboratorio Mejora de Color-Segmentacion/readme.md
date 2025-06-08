# Descripción del contenido de la carpeta
En este TP integrador se aplican técnicas de mejora de brillo y contraste, ecualización de histograma, segmentación por color y detección de objetos sobre imágenes reales.

Enlace al notebook principal: https://github.com/cynthiavillagra/PDI_VILLAGRA_CYNTHIA/blob/main/014%20Laboratorio%20Mejora%20de%20Color-Segmentacion/14_LAB_Integrador_2_clean.ipynb

Profesor: Matías Barreto (GitHub: [@mattbarreto](https://github.com/mattbarreto))

## 📚 Créditos
- Alumna: Cynthia Marcela Villagra
- Docente: Prof. Matías Barreto  
- Carrera: Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial  
- Instituto: IFTS N° 24 - CABA

---

# 🧪 Procesamiento de Imágenes - Laboratorio Integrador 2

Este proyecto práctico integra los contenidos vistos en clase sobre procesamiento digital de imágenes. A partir de una imagen seleccionada, se aplican técnicas como mejora de brillo y contraste, ecualización del histograma, segmentación por color y detección de objetos mediante contornos.

---

## 🧭 Objetivo del proyecto

Utilizar herramientas de procesamiento de imágenes para:

1. Leer y visualizar una imagen.
2. Evaluar y mejorar su brillo y contraste.
3. Aplicar ecualización de histograma.
4. Segmentar regiones de interés (color rojo en este caso).
5. Detectar y marcar objetos en la imagen.

---

## 🧰 Herramientas utilizadas

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib
- NumPy
- Widgets de Jupyter para interacción

---

## 📸 Proceso paso a paso

### 📌 1. Carga y visualización de imagen

- Se utilizó `cv2.imread()` para cargar la imagen (formato BGR).
- Se convirtió a RGB con `cv2.cvtColor()` para visualizar correctamente en `matplotlib`.

### 📌 2. Evaluación y mejora de imagen

- Se definieron funciones personalizadas para calcular **brillo** (media) y **contraste** (desvío estándar).
- Se aplicó mejora con `cv2.convertScaleAbs()`, ajustando:
  - `alpha`: contraste
  - `beta`: brillo

### 📌 3. Ecualización del canal V (HSV)

- La imagen se convirtió a HSV y se trabajó sobre el canal **V** (valor/luminosidad).
- Se usó `cv2.equalizeHist()` para mejorar la distribución de intensidades.
- Se visualizaron histogramas antes y después del procesamiento.

### 📌 4. Segmentación por color (rojo)

- Se definieron dos rangos HSV para cubrir el rojo.
- Se usó `cv2.inRange()` para generar máscaras binarias.
- Las máscaras se combinaron y aplicaron para aislar el color rojo.

### 📌 5. Detección de objetos

- La imagen segmentada se convirtió a escala de grises y luego a binaria.
- Se aplicó `cv2.findContours()` para encontrar los bordes de los objetos.
- Se dibujaron rectángulos usando `cv2.boundingRect()`.

---

## 📊 Resultados

- Mejora visual significativa de imágenes oscuras o con bajo contraste.
- Segmentación precisa del color rojo.
- Detección de regiones de interés con recuadros bien definidos.

---

## 📚 Conclusiones

- Entender el espacio de color y la estructura de los datos es fundamental para segmentar correctamente.
- Las técnicas simples como ajustar contraste o ecualizar el histograma pueden mejorar mucho una imagen.
- Detectar contornos requiere binarizar la imagen y entender cómo OpenCV interpreta los bordes.

---




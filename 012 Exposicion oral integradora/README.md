
# 👁️ De la luz a la imagen digital

Este trabajo práctico aborda el recorrido que realiza la **luz** desde que incide en el objeto hasta que se convierte en una imagen **digital** en una computadora. Se analizan también las formas en las que distintas librerías de Python representan y procesan esa imagen.

---

## 🌞 ¿Cómo vemos? ¿Cómo captura la imagen una cámara?

### 📌 En el ojo humano:

1. La **luz** rebota en los objetos y entra al ojo a través de la **córnea** y la **pupila**.
2. Llega al **cristalino**, que enfoca la luz sobre la **retina**.
3. En la retina hay células fotorreceptoras (**conos y bastones**) que transforman la luz en señales eléctricas.
4. Estas señales viajan por el nervio óptico hasta el cerebro, donde se interpreta la imagen.

### 📌 En una cámara digital:

1. La luz pasa por el lente de la cámara y se enfoca sobre un **sensor** (CCD o CMOS).
2. Este sensor está cubierto por una **matriz de filtros de color** (Bayer).
3. Cada píxel detecta la intensidad de un solo color (rojo, verde o azul).
4. Se combinan esos valores para formar una imagen en **RGB**.
5. La imagen se **convierte en una matriz numérica** que puede ser almacenada y procesada.

---

## 💡 ¿Qué es un píxel?

- Un **píxel** es la unidad mínima de una imagen digital.
- Cada píxel contiene información de **intensidad** de color (en imágenes a color) o de **brillo** (en escala de grises).
- En imágenes RGB, cada píxel tiene **3 valores** (uno por canal de color): Rojo, Verde y Azul.

---

## 🧪 Comparativa entre librerías de procesamiento de imágenes

Se trabajó con la misma imagen utilizando tres librerías diferentes: `PIL`, `OpenCV` y `scikit-image`, comparando:

- Cómo cargan una imagen.
- Cómo visualizan sus datos.
- Cómo transforman los colores y formatos.

| Librería        | Modo de carga        | Tipo de datos | Orden de canales | Comentarios |
|----------------|----------------------|---------------|------------------|-------------|
| **PIL**        | `Image.open()`       | `PIL.Image`   | RGB              | Formato amigable pero limitado. Necesita conversión a array para procesar. |
| **OpenCV**     | `cv2.imread()`       | `np.ndarray`  | BGR              | Carga rápida, pero invierte los colores respecto a RGB. Necesita `cv2.cvtColor`. |
| **scikit-image** | `io.imread()`       | `np.ndarray`  | RGB              | Carga como array NumPy directamente. Usa floats en lugar de uint8 en algunos casos. |

---

## 🔎 Ejercicios realizados

- Se cargó la misma imagen con cada librería.
- Se imprimieron el tipo de datos, forma y valores de ejemplo.
- Se visualizaron las imágenes para comparar diferencias en visualización y representación interna.

---

## 📚 Conclusiones

- La forma en que se representa una imagen digital **depende de la librería** que se use.
- Es importante saber si una imagen está en **RGB o BGR**.
- Entender el formato de los datos es clave para evitar errores en procesamiento posterior.

---

## 🛠️ Herramientas utilizadas

- Python 3.x
- Pillow (PIL)
- OpenCV
- scikit-image
- Matplotlib

---

## 🔗 Enlace al repositorio principal

[https://github.com/cynthiavillagra/IFTS24_PDI](https://github.com/cynthiavillagra/IFTS24_PDI)

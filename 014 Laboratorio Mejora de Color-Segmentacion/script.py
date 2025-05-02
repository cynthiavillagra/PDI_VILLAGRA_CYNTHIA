import nbformat

ruta_entrada = r"C:\Users\misse\Desktop\github\14_LAB_Integrador_2.ipynb"
ruta_salida = r"C:\Users\misse\Desktop\github\14_LAB_Integrador_2_clean.ipynb"

# Leer el notebook
with open(ruta_entrada, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Eliminar por completo metadata.widgets
if "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

# Guardar el notebook limpio
with open(ruta_salida, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

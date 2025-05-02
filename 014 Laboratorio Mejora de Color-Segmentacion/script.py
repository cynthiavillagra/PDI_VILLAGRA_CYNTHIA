import nbformat

# Rutas corregidas
ruta_entrada = r"C:\Users\misse\Desktop\github\14_LAB_Integrador_2.ipynb"
ruta_salida = r"C:\Users\misse\Desktop\github\14_LAB_Integrador_2_fixed.ipynb"

# Leer el notebook
with open(ruta_entrada, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Reparar metadata si es necesario
if "widgets" in nb["metadata"] and "state" not in nb["metadata"]["widgets"]:
    nb["metadata"]["widgets"]["state"] = {}

# Guardar el notebook corregido
with open(ruta_salida, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

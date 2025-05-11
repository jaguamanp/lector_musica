# 🎶 Reproductor de Letras Tipo Karaoke en Python

Este proyecto es una aplicación sencilla en Python que lee un archivo CSV con la letra de una canción y muestra su contenido letra por letra en consola, sincronizado con los tiempos definidos. Ideal para visualizaciones tipo karaoke o demostraciones interactivas.

---

## 📂 Estructura del Proyecto

```

/tu\_proyecto/
│
├── canciones/
│   └── a_donde_vamos_morat.csv
│
├── index.py
└── README.md

````

---

## 📋 Requisitos

- Python 3.7+
- pandas (`pip install pandas`)

---

## ▶️ Cómo ejecutar

1. Asegúrate de tener instalado `pandas`:

```bash
pip install pandas
````

2. Ejecuta el script desde consola:

```bash
python karaoke.py
```

---

## 📄 Formato del CSV

El archivo `.csv` debe tener el siguiente formato:

```csv
Tiempo,Letra
00:02;Recuerdo verte de perfil
00:06;Perdona si no fui sutil
...
```

* **Tiempo:** en formato `MM:SS`
* **Letra:** texto que se mostrará a partir de ese tiempo

---

## 🎨 Colores en consola

Cada letra se muestra en color cian brillante. Puedes personalizar el color modificando la variable `COLOR` en el script:

```python
COLOR = "\033[96m"  # Cambiar por otro código ANSI si se desea
```

---

## 💡 Autor

Desarrollado por   jaguamanp.

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia MIT.


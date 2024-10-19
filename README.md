# 2D Wave equation

![Simulación de onda 2D](video_pre.gif)

Este proyecto implementa una solución numérica a la ecuación de onda en 2 dimensiones con condiciones de contorno fijas. Utiliza matplotlib para visualizar una animación que muestra la evolución de la onda en el tiempo.

## Descripcion

La ecuación de onda es una ecuación en derivadas parciales que describe la propagación de ondas, como el sonido o las ondas en una cuerda vibrante. En este proyecto, se implementa una simulación de la ecuación de onda en 2D utilizando un enfoque basado en la serie de Fourier.

### Funcionalidades
* Resolución numérica de la ecuación de onda 2D con condiciones de contorno definidas.
* Animación de la evolución temporal de la onda en el dominio definido.
* Posibilidad de guardar la animación como un archivo MP4 utilizando ffmpeg.


### Requisitos
* Python 3.x
* Numpy
* Matplotlib
* FFMpeg (para guardar la animación en formato de video)


Puedes instalar los requisitos ejecutando
```
pip install numpy matplotlib
```

### Para ejecutar
1. Asegúrate de tener instalados los requisitos
2. Ejecuta el script animation.py:

```
python3 animation.py
```

### Parámetros del problema
* n, m: Número de iteraciones máximas para las sumas en la serie de Fourier.
* l1, l2: Dimensiones del contorno del problema.
* v: Velocidad de la onda, calculada como sqrt(9.81 * 20).
* epochs: Número de iteraciones de la simulación (frames de la animación).
* f1(x, y): Función que define las condiciones iniciales de la onda.

### Ejemplos con diferentes condiciones iniciales
$$ f(x,y) = xy(L_1-x)(L_2-y)$$
![Simulación de onda 2D](video1.gif)

$$ f(x,y) = xy$$
![Simulación de onda 2D](video2.gif)

$$ f(x,y) = e^{-((x-2)^2+(y-5)^2)}-e^{-((x-7)^2+(y-5)^2)}$$
![Simulación de onda 2D](video3.gif)

# Simulador de Anomalía de Belady - FIFO

Este proyecto implementa un simulador gráfico para demostrar la Anomalía de Belady en el algoritmo de reemplazo de páginas FIFO (First-In-First-Out). La anomalía de Belady es un fenómeno contraintuitivo donde aumentar el número de marcos de página puede resultar en un mayor número de fallos de página.

## 🌟 Características

- Interfaz gráfica moderna e intuitiva usando PyQt5
- Simulación visual del algoritmo FIFO de reemplazo de páginas
- Comparación simultánea de diferentes números de marcos
- Generador de secuencias aleatorias
- Visualización detallada del proceso de reemplazo
- Detección automática de la anomalía de Belady
- Exportación de resultados
- Interfaz responsive y amigable al usuario

## 📋 Requisitos Previos

```bash
Python 3.7+
PyQt5
```

## 🛠️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/XlHader/belady-simulator.git
cd belady-simulator
```

2. Crear y activar un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Unix o MacOS:
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar desde el código fuente:
```bash
python fifo.py
```

### Usar el ejecutable compilado:
1. Abrir la carpeta dist y localizar el ejecutable según su carpeta.

## 💻 Cómo Usar el Simulador

1. **Entrada Manual**:
   - Ingresa una secuencia de números separados por comas en el campo "Secuencia de páginas"
   - Especifica el número de marcos para ambas simulaciones
   - Haz clic en "Simular FIFO"

2. **Generación Automática**:
   - Haz clic en "Generar Secuencia Aleatoria"
   - El programa generará y simulará automáticamente una secuencia

3. **Interpretación de Resultados**:
   - Las tablas muestran el estado de los marcos en cada paso
   - Las celdas rojas indican fallos de página
   - El resumen muestra la comparación de fallos y detecta la anomalía

## 🔨 Compilación

Para crear un ejecutable independiente:

```bash
# Instalar pyinstaller si aún no está instalado
pip install pyinstaller

# Crear el ejecutable
pyinstaller --onefile --windowed --name BeladySimulator main.py
```

El ejecutable se encontrará en la carpeta `dist`.

## 📚 Estructura del Proyecto

```
belady-simulator/
│
├── fifo.py              # Archivo principal del programa
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
│
└── dist/               # Ejecutables compilados
```
## 🔍 Referencias

- [Anomalía de Belady - Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9l%C3%A1dy%27s_anomaly)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
# mlp-simple

Repositorio para el laboratorio MLP: proyecto reproducible que entrena un MLP sencillo con MNIST.

Este paquete contiene:
- `notebooks/mlp_simple.ipynb` — Notebook (Colab-ready) con instrucciones y código.
- `docs/report.md` — Plantilla para el informe del experimento.
- `model/` — Contendrá el modelo guardado (`mlp_model.h5`).
- `ledger/ledger.csv` — Registro de hashes y timestamps para trazabilidad.
- `data/` — Lugar para datos (si aplica).

**Origen de las instrucciones completas:** contenido del archivo **Laboratorio MLP.docx** proporcionado por el usuario. fileciteturn0file0

## Cómo usar (pasos rápidos)

1. Clona este repositorio en tu máquina local:
```bash
git clone <tu-repo-url>.git
cd mlp-simple
```

2. Abre el notebook en Google Colab:
- En Colab: *Archivo → Abrir cuaderno → GitHub* y pega la URL del repo.
- O sube `notebooks/mlp_simple.ipynb` desde tu local.

3. Sigue los pasos en el notebook (cargar MNIST, preparar datos, definir y entrenar el modelo, guardar `model/mlp_model.h5`, generar `docs/report.md` y calcular hashes).

4. Sube los archivos generados a la carpeta correspondiente en GitHub (`model/`, `docs/`, `ledger/`).

## Estructura de ejemplo (ya creada)
```
data/
docs/
model/
notebooks/
ledger/
```

## Licencia
Añade la licencia que prefieras (MIT, Apache 2.0, etc.).

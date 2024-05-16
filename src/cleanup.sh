#!/bin/bash

# Obtener la ruta del directorio del script
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Nombre del archivo del keylogger
KEYLOGGER_SCRIPT="k-log.py"
KEYLOG_FILE="keylog.txt"

# Paso 1: Eliminar archivos del keylogger
echo "Eliminando archivos del keylogger..."
rm -f "$SCRIPT_DIR/$KEYLOGGER_SCRIPT"
rm -f "$SCRIPT_DIR/$KEYLOG_FILE"

# Paso 2: Limpiar el historial de comandos
echo "Limpiando el historial de comandos..."
history -c
echo "" > ~/.bash_history

# Mensaje final
echo "Limpieza completa. El keylogger y sus rastros han sido eliminados."



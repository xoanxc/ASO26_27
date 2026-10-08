#!/bin/bash

if [[ "${EUID}" != 0 ]]
then
    echo "ERROR: No tienes permisos suficientes."
    echo "Debes ejecutar este script como root (ej: sudo $0)"
    exit 1
fi

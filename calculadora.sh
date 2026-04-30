#!/bin/bash

if ! command -v python3 &> /dev/null
then
	echo "Python3 não encontrado. Instalando..."
	sudo apt update
	sudo apt install -y python3
fi

echo "Executado calculadora..."
python3 Calculadora.py

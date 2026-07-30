#!/bin/bash
echo "[INFO] Uruchamiam generowanie raportu AWS"
python export_s3.py
if [ -f "raport.csv" ]; then
    echo "[OK] Raport wygenerowany pomyślnie!"
    echo "Zawartość: "
    cat raport.csv
else
    echo "[BŁĄD] Plik raportu nie powstał!"
fi

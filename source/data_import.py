# data_import.py

import pandas as pd

def import_from_csv(file_path):
    """Function to import data from .CSV"""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Datei nicht gefunden.")
        return None

def import_from_text(file_path):
    """Function to import data from text-data"""
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print("Datei nicht gefunden.")
        return None

def import_from_excel(file_path, sheet_name):
    """Function to import excel data. for .xlsx and .xls"""
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except FileNotFoundError:
        print("Datei nicht gefunden.")
        return None

def import_from_sql(self, query):
"""Funktion zum Importieren von Daten aus einer SQL-Datenbank."""
    try:
    if not self.connection:
        raise Exception("Keine Verbindung zur Datenbank hergestellt.")
    data = pd.read_sql_query(query, self.connection)
return data
except Exception as e:
print(f"Fehler beim Importieren von Daten aus der SQL-Datenbank: {e}")
return None


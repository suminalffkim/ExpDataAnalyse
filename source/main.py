from src import data_import

# Beispielverwendung der import_from_csv-Funktion
csv_data = data_import.import_from_csv("data/experimental_data.csv")
print("CSV-Daten:")
print(csv_data)

# Beispielverwendung der import_from_text-Funktion
text_data = data_import.import_from_text("data/experimental_data.txt")
print("Text-Daten:")
print(text_data)

excel_data = data_import.import_from_excel("data/experimental_data.xlsx", sheet_name="Sheet1")
print("Excel-Daten:")
print(excel_data)

# Beispielverwendung der DataImporter-Klasse für SQL
with DataImporter('example.db') as importer:
    sql_query = "SELECT * FROM table_name;"
    sql_data = importer.import_from_sql(sql_query)
    print("SQL-Daten:")
    print(sql_data)

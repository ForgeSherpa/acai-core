import pandas as pd
import json

# Load the CSV file with the correct delimiter
df = pd.read_csv('Data Dosen test.csv', delimiter=';')  # Specify semicolon as the delimiter

# Initialize a list to store NLU training examples
nlu_data = {"version": "3.1", "nlu": []}

# Print the columns to verify
print("Columns in CSV:", df.columns.tolist())

# Iterate through the rows in the DataFrame
for index, row in df.iterrows():
    lecturer_name = row['nama_dosen']
    nidn = row['nidn_dosen']
    lecturer_id = row['id_dosen']

    # Ensure that nidn is treated as a string
    nidn_str = str(nidn).zfill(10) 
    lecturer_id_str = str(lecturer_id).zfill(8)

    nlu_data['nlu'].append({
        "intent": "ask_lecturer_by_name", #by_nidn
        "examples": f"- Apa NIDN dari {lecturer_name}?\n- Bisa kah Anda memberi tahu NIDN untuk {lecturer_name}?",
        "nidn": nidn_str,
        "lecturer_name": lecturer_name
    })
    
    nlu_data['nlu'].append({
        "intent": "ask_lecturer_by_nidn", #by_name
        "examples": f"- Siapa nama dosen dengan NIDN {nidn_str}?\n- Beritahu saya nama dosen dengan NIDN {nidn_str}.",
        "nidn": nidn_str,
        "lecturer_name": lecturer_name
    })

    # Contoh untuk mencari nama dosen berdasarkan ID dosen
    nlu_data['nlu'].append({
        "intent": "ask_lecturer_by_id",
        "examples": f"- Siapa nama dosen dengan ID {lecturer_id_str}?\n- Beritahu saya nama dosen dengan ID {lecturer_id_str}.",
        "id": lecturer_id_str,
        "lecturer_name": lecturer_name
    })

# Save the NLU training data to a JSON file
output_file_path = 'nlu_training_data.json'  # Specify the output path
with open(output_file_path, 'w', encoding='utf-8') as outfile:  # Add encoding for special characters
    json.dump(nlu_data, outfile, ensure_ascii=False, indent=2)

print("NLU training data generated successfully.")

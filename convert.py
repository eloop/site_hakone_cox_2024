import pandas as pd
import json

# Load the TSV file
file_path = 'hakone.tsv'
data = pd.read_csv(file_path, sep='\t')

# Select the relevant columns
selected_columns = data[['easting', 'northing', 'depth', 'decimal year', 'rupture diameter']]

# Convert the selected data to a JSON-like format for JavaScript
json_data = selected_columns.to_dict(orient='records')

# Convert to a JavaScript variable declaration
js_data = f"const jsonData = {json.dumps(json_data)};"

# Save to a JavaScript file
js_file_path = 'hakone_data.js'
with open(js_file_path, 'w') as f:
    f.write(js_data)

print(f"JavaScript data file saved to {js_file_path}")

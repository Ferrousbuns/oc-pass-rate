import os
import json

def generate_index():
    data_dir = 'data'
    if not os.path.exists(data_dir):
        print(f"Error: {data_dir} directory not found.")
        return

    csv_files = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            # Strip the .csv extension to just leave the base name for the UI
            basename = os.path.splitext(filename)[0]
            csv_files.append(basename)

    # Write the list to data/index.json
    output_path = os.path.join(data_dir, 'index.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(csv_files, f, indent=4)

    print(f"Successfully generated {output_path} with {len(csv_files)} CSV files.")

if __name__ == '__main__':
    generate_index()

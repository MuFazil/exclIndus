import pandas as pd
import json
from datetime import datetime

def read_excel_to_dict_list(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path, dtype=str)  # Ensure all data is read as strings initially

    # Convert the DataFrame to a list of dictionaries
    dict_list = df.to_dict(orient='records')

    # Convert datetime objects to string
    for entry in dict_list:
        for key, value in entry.items():
            if isinstance(value, datetime):
                entry[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            elif pd.isna(value):  # Convert NaN values to None
                entry[key] = None

    return dict_list

def save_dict_list_as_html(dict_list, output_file):
    # Convert list of dictionaries to JSON string
    json_data = json.dumps(dict_list, indent=4)

    # Create an HTML page with the JSON data
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dictionary Output</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                white-space: pre-wrap;
            }}
        </style>
    </head>
    <body>
        <h1>Dictionary Output</h1>
        <pre>{json_data}</pre>
    </body>
    </html>
    """

    # Save the HTML to a file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"HTML file saved to {output_file}")

def main():
    # Example usage
    file_path = 'C:/Acads/exclIndus/datIndus.xlsx'
    data = read_excel_to_dict_list(file_path)
    
    # Specify the output HTML file path
    output_file = 'C:/Acads/exclIndus/datIndus_output.html'
    save_dict_list_as_html(data, output_file)

    # Optionally open the HTML file in the default web browser
    import webbrowser
    webbrowser.open(output_file)

if __name__ == "__main__":
    main()

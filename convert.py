import json

# Load the JSON file
input_json_path = "scholarships.json"  # Replace with the path to your JSON file
output_html_path = "scholarships.html"

# Read the JSON data
with open(input_json_path, "r") as f:
    scholarships = json.load(f)

# Start building the HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholarship Programs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:hover { background-color: #f1f1f1; }
    </style>
</head>
<body>
    <h1>Scholarship Programs</h1>
    <p>Below is a list of available scholarships:</p>
    <table>
        <tr>
            <th>Scholarship Program</th>
            <th>Degree</th>
            <th>Link</th>
        </tr>
"""

# Add each scholarship as a table row
for scholarship in scholarships:
    html_content += f"""
        <tr>
            <td>{scholarship['Scholarship program']}</td>
            <td>{scholarship['Degree']}</td>
            <td><a href="{scholarship['Link to scholarship info page']}" target="_blank">Info</a></td>
        </tr>
    """

# Close the HTML structure
html_content += """
    </table>
</body>
</html>
"""

# Save the HTML file
with open(output_html_path, "w") as f:
    f.write(html_content)

print(f"HTML file successfully created at: {output_html_path}")

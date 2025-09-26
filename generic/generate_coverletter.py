import json
from jinja2 import Environment, FileSystemLoader

# Load JSON data
with open("application_data.json") as f:
    data = json.load(f)

# Setup Jinja environment
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("coverletter_template.tex.jinja")

# Render template with data
output_tex = template.render(**data)

# Write output
with open("coverletter_generated.tex", "w") as f:
    f.write(output_tex)

print("Generated coverletter_generated.tex!")

import json
import subprocess
from jinja2 import Environment, FileSystemLoader

# -----------------------
# 1. Load application data
# -----------------------
with open("application_data.json") as f:
    data = json.load(f)

# -----------------------
# 2. Setup Jinja2
# -----------------------
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("coverletter_template.tex.jinja")

# -----------------------
# 3. Render template
# -----------------------
output_tex = template.render(**data)
recipient_institution = data.get("recipient_institution")
# If the value itself may contain spaces, normalize that
if recipient_institution is not None:
    recipient_institution = recipient_institution.lower().replace(" ", "_")
output_filename = f"coverletter_vibhor_aggarwal_{recipient_institution}.tex"

with open(output_filename, "w") as f:
    f.write(output_tex)

print(f"Generated {output_filename}!")

# -----------------------
# 4. Run pdflatex
# -----------------------
try:
    subprocess.run(
        ["pdflatex", "-shell-escape", output_filename],
        check=True
    )
    print("PDF compiled successfully!")
except subprocess.CalledProcessError:
    print("Error: pdflatex compilation failed.")

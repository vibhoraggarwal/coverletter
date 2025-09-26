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
output_filename = "vibhor_coverletter.tex"

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

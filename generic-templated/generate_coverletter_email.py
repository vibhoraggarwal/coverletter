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
template_coverletter = env.get_template("coverletter_template.tex.jinja")
template_email = env.get_template("email_template.txt.jinja")

# -----------------------
# 3. Render template
# -----------------------
recipient_institution = data.get("recipient_institution")
# If the value itself may contain spaces, normalize that
if recipient_institution is not None:
    recipient_institution = recipient_institution.lower().replace(" ", "_")
output_filename_coverletter = f"coverletter_vibhor_aggarwal_{recipient_institution}.tex"
output_filename_email = f"email_vibhor_aggarwal_{recipient_institution}.txt"

with open(output_filename_coverletter, "w") as f:
    f.write(template_coverletter.render(**data))

print(f"Generated {output_filename_coverletter}!")

with open(output_filename_email, "w") as f:
    f.write(template_email.render(**data))
print(f"Generated {output_filename_email}!")

# -----------------------
# 4. Run pdflatex
# -----------------------
try:
    subprocess.run(
        ["pdflatex", "-shell-escape", output_filename_coverletter],
        check=True
    )
    print("PDF compiled successfully!")
except subprocess.CalledProcessError:
    print("Error: pdflatex compilation failed.")

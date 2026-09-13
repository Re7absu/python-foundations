from pathlib import Path

folder = Path("data")
file_name = "user.csv"

file_path = folder / file_name

print("File path:", file_path)

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")
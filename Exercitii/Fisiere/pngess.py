from pathlib import Path
import sys

ROOT = Path(__file__).parent

png_path = ROOT / “file_name.png”

if not png_path.is_file():
	print("File found")
	sys.exit(1)

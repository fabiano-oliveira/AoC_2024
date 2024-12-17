import sys
import os
from pathlib import Path

# Add the src directory to Python path
src_path = str(Path(__file__).parent / "src")
sys.path.append(src_path)
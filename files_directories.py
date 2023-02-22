from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# Relative path
path = Path()
for file in path.glob('*.py'):
    print(file)

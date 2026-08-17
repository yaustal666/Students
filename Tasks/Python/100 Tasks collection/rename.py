import os

for i in range(1, 101):
    os.rename(f"task{i}.md", f"task{i:03d}.md")
from pathlib import Path

folderName = input()
folderPath = Path(f"./{folderName}")
folderPath.mkdir(parents=True, exist_ok=True)

filepath = folderPath / "sourceEn.txt"
filepath.write_text("")

filepath = folderPath / "sourceRus.txt"
filepath.write_text("")

for i in range(1, 11):
    testingFolder = Path(f"./TestingTasks/{folderName}/Task{i}")
    testingFolder.mkdir(parents=True, exist_ok=True)
    filepath = testingFolder / "main.py"
    filepath.write_text("")


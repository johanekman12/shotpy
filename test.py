import subprocess

problemfile = input('Write filename / path to file: ')

result = subprocess.run([f"SHOT {problemfile}"], shell=True, capture_output=True, text=True)

if result.stderr:
    print(result.stderr)
else:
    print(result.stdout)


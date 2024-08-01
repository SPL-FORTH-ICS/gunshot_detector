libs = ["audioread", "librosa", "matplotlib", "pandas", "PyQt5", "sklearn", "scipy", "soundfile", "tabulate", "tensorflow", "openpyxl", "tqdm"]

err = []

for index, module in enumerate(libs):    
    print(f"Checking module {index+1} of {len(libs)}...  ({module})")
    try:
        exec("import " + module)
    except ImportError as e:
# ModuleNotFoundError:
        err.append(module)
        print(e)
if len(err)>0:
    print("Modules ", err, "failed.")
else:
    print("Everything works fine!")
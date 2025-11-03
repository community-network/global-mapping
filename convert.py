import os

files = os.listdir("global_mapping")
modules = []

for module in map(
    __import__,
    [f"global_mapping.{file.replace('.py', '')}" for file in files if "_" not in file],
):
    modules = [(v, getattr(module, v)) for v in dir(module) if v[:2] != "__"]

for file, variables in modules:
    methods = [(v, getattr(variables, v)) for v in dir(variables) if v[:2] != "__"]
    with open(f"src/generated_ts/{file}.ts", "w") as f:
        f.writelines(
            [f"export const {key.lower()} = {value};\n" for key, value in methods]
        )

with open(f"src/index.ts", "w") as f:
    f.writelines(
        [f'export * as {file} from "./generated_ts/{file}";\n' for file, _ in modules]
    )

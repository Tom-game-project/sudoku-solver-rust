import base64

with open("pkg\sudoku_solver_rust_bg.wasm",mode="rb") as f:
    a=base64.b64encode(f.read()).decode("utf-8")

with open("b64.txt",mode="w",encoding="utf-8")as f:
    f.write(a)

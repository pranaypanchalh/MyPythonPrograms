def createTables(value):
    for i in range(1, value+1):
        ans = ""
        for j in range(1, 11):
            ans += f"{i} x {j} = {i*j}\n"
        with open(f"Files/MultiplicationTables/Tables/Table of {i}", "w") as f:
            f.write(ans)

createTables(20)
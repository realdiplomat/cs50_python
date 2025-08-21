e = input("Expression: ")
x,y,z = e.split()

nx = float(x)
nz = float(z)

if "+" in y:
    r = nx+nz
elif "-" in y:
    r = nx-nz
elif "*" in y:
    r = nx*nz
elif "/" in y:
    r = nx/nz
print(f"{r:.1f}")

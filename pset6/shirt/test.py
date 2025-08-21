#file_before = "before.JPG".lower()
#file_after = "after.JPG".lower()

#extension = (".jpg", ".jpeg", ".png")
#if file_before.endswith(extension) and file_after.endswith(extension):
#    print("Invalid")

file_before = "BEFORE.JPG".lower()
file_after = "after.PnG".lower()

beforeName, beforeExt = file_before.split(".")
afterName, afterExt = file_after.split(".")

print(beforeExt)
print(afterExt)

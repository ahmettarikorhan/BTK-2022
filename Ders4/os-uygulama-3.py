import os

try:
    os.mkdir("elma")
except FileExistsError:
    print("Zaten böyle bir dosya var")



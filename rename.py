run = 1
def prog():
    import os
    psuedo_cwd = str(input("Enter file path: "))

    for root, directories, filenames in os.walk(psuedo_cwd):
        for filename in filenames:
            output = str(", ".join(filename.split('- ')[-1:]))
            a = (root + '\\' + filename)
            b = (output)
            os.system('ren "' + str(a) + '" "' + str(b) + '"')

while run == 1:
    prog()

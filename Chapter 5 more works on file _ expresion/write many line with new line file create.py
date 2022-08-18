lines = ["This is first line", "This is second line", "This is third line"]
with open("lines.txt","w") as fb:
    for line in lines:
        fb.write(line+"/n")

#lines = ["This is first line", "This is second line", "This is third line"]
with open("lines.txt", "w") as fb:
    fb.write("This is first line \nThis is second line \nThis is third line")

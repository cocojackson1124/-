lines_maxlenth = 0
line_numbers = 1
code_in = open("demo.py", "r").readlines()
code_out = open("demo_new.py", "w")
for i in code_in:
    lines_maxlenth = len(i) if lines_maxlenth < len(i) else lines_maxlenth
for i in code_in:
    i = i.ljust(lines_maxlenth+1).replace('\n', '') + "#" + str(line_numbers) + "\n"
    line_numbers += 1
    code_out.write(i)
type = "NAND"
number = 1

s = '.SUBCKT ' + type + str(number)
for i in range(number):
    s += ' x' + str(i + 1)
s += ' y\n'
s += '+ PARAMS: nwidth=1 pwidth=1\n\n.param wn = {nwidth * 0.022u} wp = {pwidth * 0.022u}\n\n'

for i in range(number):
    s += 'Mpmos@' + str(i + 1) + (' vdd' if i == 0 or type == "NAND" else (' net@' + str(i))) + ' x' + str(i + 1) + (' y' if i == number - 1 or type == "NAND" else (' net@' + str(i + 1))) + ' vdd P L=0.022U W={wp}\n'

s += '\n'

for i in range(number):
    s += 'Mnmos@' + str(i + 1) + (' y' if i == 0 or type == "NOR" else (' net@' + str(i))) + ' x' + str(i + 1) + (' gnd' if i == number - 1 or type == "NOR" else (' net@' + str(i + 1))) + ' gnd N L=0.022U W={wn}\n'

s += '.ENDS ' + type + str(number)

s += '\n\n'

s += '** example: X' + type + str(number) + '@1'
for i in range(number):
    s += ' net@' + str(i + 1)
s += ' X' + type + str(number) + '@1_y '+ type + str(number)
s += '\n** + PARAMS: nwidth=1 pwidth=1'

with open('subfiles/' + type + str(number) + '.txt', 'w') as out:
    out.write(s)
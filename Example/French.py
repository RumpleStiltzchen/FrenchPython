from ast import keyword
import sys
import os
import pathlib




NumArgs = len(sys.argv)
Args = sys.argv
print(NumArgs)
print(str(sys.argv))
if Args[1] == "help":
    print('''French Python Translator!\n--------------------------------------------------------------\nArgument 1: French python file path\nArgument 2: Run when done compiling 
    ('True' or 'False')\nArgument 3: Output file name in quotation marks, Defaults to "Output.py"''')
    sys.exit()
elif NumArgs == 2:
    path = sys.argv[1] 
    RunOnExit = "False"
    OutputFileName = "Output"
elif NumArgs >= 3:
    path = sys.argv[1] 
    RunOnExit = sys.argv[2]
    OutputFileName = "Output"
else:
    path = sys.argv[1] 
    RunOnExit = sys.argv[2]
    OutputFileName = str(sys.argv[3]) + ".py"
data = ""
keywords = [' False ', ' None ', ' True ', ' and ', ' as ', ' assert ', ' async ', ' await ', ' break ', ' class ', ' continue ', ' def ', ' del ', ' elif ', ' else ', ' except ',
 ' finally ', ' for ', ' from ', ' global', ' if ', ' import ', ' in ', ' is ', ' lambda ', ' nonlocal ', ' not ', ' or ', ' pass ', ' raise ', ' return ', 
 ' try ', ' while ', ' with ', ' yield ', ' print ', ' self ', ' else:']

FrenchKeywords = [' Faux ', ' Aucun ', ' Vrai ', ' et ', ' comme ', ' affirmer ', 'async ', ' attendre ', ' brise ', ' classe ', ' continue ', ' def ', ' efface ', ' sinsi ', ' sinon ', ' attraper ',
 ' finalement ', ' pour ', ' de ', ' globale ', ' si ', ' importe ', ' dans ', ' est ', ' lambda ', ' paslocale ', ' pas ', ' ou ', ' passe ', ' augmenter ', ' retourner ',
  ' essayer ', ' pendant ',' avec ', ' ceder ', ' imprime ', ' soi ', ' sinon:' ]
try:
    text_file = open(path, "r")

except:
    print("First argument must be file path | Premier argument doit etre le chemin du fichier")
    sys.exit()

data = text_file.read()

text_file.close()



for i in range(1, 5):
    data = data.replace("Vrai", "True")
    data = data.replace("Faux", "False")
    data = data.replace("passe", "pass")

    for i in range(0, len(keywords)):
        data = data.replace(FrenchKeywords[i], keywords[i] )
        
        
        #\t x _
        data = data.replace("\t" + FrenchKeywords[i][1:1],"\t" +  keywords[i][1:1] )
        #\t x \t
        data = data.replace("\t" + FrenchKeywords[i][1:1] + "\t","\t" +  keywords[i][1:1] + "\t")
        #\t x \n
        data = data.replace("\t" + FrenchKeywords[i][1:1] + "\n","\t" +  keywords[i][1:1] + "\n")
        #\n x __
        data = data.replace("\n" + FrenchKeywords[i][1:], "\n" + keywords[i][1:] )
        #_x\n
        data = data.replace(" " + FrenchKeywords[i][1:1] + "\n", " " + keywords[i][1:1] + "\n")
        #_x:
        data = data.replace(" " + FrenchKeywords[i][1:1] + ":", " " + keywords[i][1:1]+":" )
        #\t x :
        data = data.replace("\t" + FrenchKeywords[i][1:1] + ":","\t" + keywords[i][1:1]+":" )
        #\n x :
        data = data.replace("\n" + FrenchKeywords[i][1:1] + ":","\n" + keywords[i][1:1]+":" )
        # (x)
        data = data.replace("(" + FrenchKeywords[i][1:1] + ")","(" +  keywords[i][1:1] + ")")
        #(x )
        data = data.replace("(" + FrenchKeywords[i][1:],"(" +  keywords[i][1:])
        #( x)
        data = data.replace(FrenchKeywords[i][:1] + ")",keywords[i][:1]+")")
        #(x,
        data = data.replace("(" + FrenchKeywords[i][1:1] + ",","(" +  keywords[i][1:1] + ",")
        #,x)
        data = data.replace("," + FrenchKeywords[i][1:1] + ")","," +  keywords[i][1:1] + ")")
        #,x )
        data = data.replace("," + FrenchKeywords[i][1:1] + " ","," +  keywords[i][1:1] + " ")
        #( x,
        data = data.replace(" " + FrenchKeywords[i][1:1] + ","," " +  keywords[i][1:1] + ",")
        #(x.
        data = data.replace("(" + FrenchKeywords[i][1:1] + ".","(" +  keywords[i][1:1] + ".")
        #.x)
        data = data.replace("." + FrenchKeywords[i][1:1] + ")","." +  keywords[i][1:1] + ")")
        #.x.
        data = data.replace("." + FrenchKeywords[i][1:1] + ".","." +  keywords[i][1:1] + ".")
        #.x 
        data = data.replace("." + FrenchKeywords[i][1:1] + " ","." +  keywords[i][1:1] + " ")
        #.x+
        data = data.replace("." + FrenchKeywords[i][1:1] + "+","." +  keywords[i][1:1] + "+")
        #.x-
        data = data.replace("." + FrenchKeywords[i][1:1] + "-","." +  keywords[i][1:1] + "-")
        #.x/ 
        data = data.replace("." + FrenchKeywords[i][1:1] + "/","." +  keywords[i][1:1] + "/")
        #.x*
        data = data.replace("." + FrenchKeywords[i][1:1] + "*","." +  keywords[i][1:1] + "*")
    
        #_x:
        data = data.replace(" " + FrenchKeywords[i][1:1] +":", " " + keywords[i][1:1] +":")




try:
    fp = open(OutputFileName, 'x')
    fp.close()
except:
    print("Already a file named "+ OutputFileName +", remove the file or move it")
try:
    text_file = open(OutputFileName , 'w+')
    text_file.write(data)
    text_file.close()
except:
    
    print("could not write to file")
    print("====================================================")
    print(data)
    print("====================================================")
    print(str(sys.argv))

try:
    if RunOnExit == "True":
        os.system("python " + OutputFileName)
except:
    print("could not run file")
    sys.exit
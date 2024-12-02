from __future__ import print_function
from typing import List
import subprocess
import sys

wantedName:str = None
isFore:bool = False
isList:bool = False
runOptions:List[str] = []
if True:
    isHelp:bool = False 
    iarg = -1
    # search for options
    for arg in sys.argv:
        iarg+=1
        if iarg==0: continue
        elif arg=="--help" or arg=="-h":
            isHelp=True
            break
        elif arg=="--list" or arg=="-l":
            isList = True
        elif arg=="--foreground" or arg=="-f":
            isFore=True
        elif arg.startswith("--"):
            raise(Exception("Unknown option "+arg))
        else:
            wantedName = arg
            break
    # search for runoptions
    for iopt in range(iarg, len(sys.argv)-1):
        runOptions.append(sys.argv[iopt])
    # display help
    if (isHelp):
        print("\nUsage: flatrun <options> <packname> <runoptions>")
        print((' '*3)+"Options:")
        print((' '*6)+"-h --help        Opens help")
        print((' '*6)+"-f --foreground  Runs the flatpak in foreground instead of hiding its output")
        print((' '*6)+"-l --list        Lists matching flatpaks without running them")
        print((' '*3)+"Run options are parameters you want to add after flatpak run <name>")
        sys.exit()
    elif (wantedName==None):
        raise(Exception( "No name provided."))

type entry = [str, str, str, str]
entries:List[entry] = []

# find all entries using flatpak list
if True:
    outputLines:List[str] = subprocess.run(['flatpak', 'list'], stdout=subprocess.PIPE).stdout.decode("UTF-8").splitlines()
    iline:int = -1
    for lineString in outputLines:
        iline+=1
        if iline==0 and lineString.startswith("Name\t"):
            continue
        linePortions:List[str] = lineString.split('\t')
        entrySegments:entry = []
        for portion in linePortions:
            if (len(portion)==0):
                continue
            entrySegments.append(portion)
        if len(entrySegments)==0:
            continue
        entries.append(entrySegments)

if len(entries)==0:
    raise(Exception( "No flatpak packages found."
    + "Either you haven't installed any packages, or a flatpack update changed the output."
    + "This program relies on \"flatpak list\" to stay consistent to work."))

nameMatches:List[entry] = []
if (len(wantedName)==0):
    nameMatches = entries
else:
    for entry in entries:
        packName:str = entry[0] if not wantedName.find('.') else entry[1]
        if (packName.lower().find(wantedName.lower())!=-1):
            nameMatches.append(entry)

match0MaxLength = 0
match1MaxLength = 0
for entry in nameMatches:
    if (len(entry[0])>match0MaxLength): match0MaxLength=len(entry[0])
    if (len(entry[1])>match1MaxLength): match1MaxLength=len(entry[1])

selected = ""
if len(nameMatches)==0:
    raise(Exception(f"No package {wantedName} found"))
elif len(nameMatches)==1:
    selected = nameMatches[0][1]
    if (isList):
        if len(wantedName)==0:
            print("\nListing all packages:")
        else:
            print(f"\nFound a single package matching {wantedName}:")
        print(selected[0]+' '+selected[1])
        sys.exit()
else:
    while True:
        if len(wantedName)==0:
            print("\nListing all packages:")
        else:
            print(f"\nFound multiple packages matching {wantedName}:")
        ientry = 0
        for entry in nameMatches:
            ientry+=1
            prefixString = str(ientry) + (' '*(len(str(ientry))-len((str(len(nameMatches))))+1))
            match0String = entry[0] + (' '*(match0MaxLength-len(entry[0])+1))
            match1String = entry[1]
            print(prefixString+match0String+match1String)
        if (isList): 
            sys.exit()

        selStr = input("\nType the number before the package you want to run:")
        selNum = 0
        try:
            selNum = int(selStr)-1
            selected = nameMatches[selNum][1]
        except:
            print("Invalid input "+selStr)
            continue
        break

if isFore:
    subprocess.run(["/bin/bash", "-c", f"flatpak run {selected+" "+(" ".join(runOptions))}"])
else: 
    subprocess.run(["/bin/bash", "-c", f"flatpak run {selected+" "+(" ".join(runOptions))} >/dev/null 2>&1 &"])
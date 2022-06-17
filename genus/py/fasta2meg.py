#!/usr/bin/python3

import sys

def ReadSeqsOnSeq(FileName, OnSeq):
	File = open(FileName)
	Label = ""
	Seq = ""
	n = 0
	while 1:
		Line = File.readline()
		if len(Line) == 0:
			if Seq != "":
				n += 1
				OnSeq(Label, Seq)
			return
		Line = Line.strip()
		if len(Line) == 0:
			continue
		if Line[0] == ">":
			if Seq != "":
				OnSeq(Label, Seq)
			Label = Line[1:]
			Seq = ""
		else:
			Line = Line.replace(" ", "")
			Seq += Line

FileName = sys.argv[1]

def OnSeq(Label, Seq):
	print("#" + Label)
	BLOCKLENGTH = 60
	SeqLength = len(Seq)
	BlockCount = int((SeqLength + (BLOCKLENGTH-1))/BLOCKLENGTH)
	for BlockIndex in range(0, BlockCount):
		Block = Seq[BlockIndex*BLOCKLENGTH:]
		Block = Block[:BLOCKLENGTH]
		print(Block)

Name = FileName.split("/")[-1]

print("#Mega")
print("!Title %s;" % Name)
print("")

ReadSeqsOnSeq(FileName, OnSeq)

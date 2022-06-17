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

Labels = []
Seqs = []

n = 0
L = None

def OnSeq(Label, Seq):
	global n
	global L
	global Labels
	global Seqs

	Labels.append(Label)
	Seqs.append(Seq)
	n = max(n, len(Label))
	if L == None:
		L = len(Seq)
	else:
		assert len(Seq) == L

ReadSeqsOnSeq(FileName, OnSeq)

SeqCount = len(Labels)

print(" %u %u" % (SeqCount, L))
for i in range(0, SeqCount):
	Label = Labels[i]
	Label = Label.replace("/", "_")
	Label = Label.replace(".", "_")
	Seq = Seqs[i]
	s = "%-*.*s %s" % (n, n, Label, Seq)
	print(s)

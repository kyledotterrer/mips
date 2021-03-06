# masm.py
# MIPS assembler script, utilizing SPIM assembler.
#
# Input:
# 	Reads from files (located in inputs/ directory)
# Output:
# 	Writes assembled results to stdout
#
# Kyle Dotterrer
#	Adapted from code provided by Onur Mutlu (2015) 
# January, 2019 

import os
import sys
import argparse
import subprocess

# where is our copy of SPIM located? 
SPIM = "/usr/local/bin/spim"

# where should outputs be placed? 
HEX_DIR = "../hex/"

def main():
	# parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("fasm", metavar="input.s", help="the MIPS assembly file (ASCII)")
	args = parser.parse_args()

	fasm = args.fasm
	fhex = os.path.splitext(args.fasm)[0] + ".x"

	# run SPIM (the actual MIPS assembler)
	cmd = [SPIM, "-asm", "-dump", "-f", fasm]
	subprocess.call(cmd)

	# write the contents of assembled file to stdout 
	with open("text.asm", "r") as f:
		for line in f:
			sys.stdout.write(line)

	# all done - remove files generated by SPIM 
	cmd = ["rm", "-f", "data.asm", "text.asm"]
	subprocess.call(cmd)  

	sys.exit(0)

if __name__ == "__main__":
	main()

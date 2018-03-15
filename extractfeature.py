

def parse_fasta(filename):
  filehandle = open(filename,'r')
  text = filehandle.read().splitlines()
  d = dict()
  listi = [0,0]
  for line in text:
      line = line.rstrip('\n\r')
      if line.startswith(">"):
        key = line.strip(">")
        d[key] = ""
      else:
        listi[0] = text[1]
        listi[1] = text[2]
        d[key] = listi
  return(d)

print(parse_fasta("testgram+.txt"))

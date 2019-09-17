from style_rank import rank


def get_midi_paths(folder):
  import os
  return [os.path.join(folder,p) for p in os.listdir(folder) if p.endswith(".mid")]

a = get_midi_paths("/Users/Jeff/sfuvault/MIDI_DATA/CLASSICAL_ARCHIVES/AGUADO")
b = get_midi_paths("/Users/Jeff/sfuvault/MIDI_DATA/CLASSICAL_ARCHIVES/BERLIOZ")

corpus = b[:10]
to_rank = a + b[10:] + ["not_a_mid.pdf"] + ["tests/corrupt.mid"]

# no valid paths for to_rank_paths
try:
  rank(["not_a_mid.pdf"], corpus)
except Exception as e:
  print(e)

# only corrupt paths for to_rank_paths
try:
  rank(["tests/corrupt.mid"], corpus)
except Exception as e:
  print(e)

print( rank(to_rank, corpus) )
import sound #>>

from sound import file1 # -
from sound import file2 # -

from sound.file2 import c # ---

import sound.file1 # --
import sound.file2 # --

print(sound.file1.h) # --
print(sound.file2.a) # --

print(file1.d) # -
print(file2.b) # -

print(c) # ---

print(sound.a) # >>
# print(sound.b) # error
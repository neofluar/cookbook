# You’d like to clean “pýtĥöñ” up somehow.

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# Remove all whitespaces
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None,  # Deleted
}
a = s.translate(remap)
print(a)

# Remove all combining characters
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

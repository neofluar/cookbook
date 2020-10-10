# You want to replace HTML or XML entities such as &entity; or &#code; with their
# corresponding text

import html

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

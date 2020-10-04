from PIL import Image
import sys
sys.path.append('/path/to/dir')

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

txt = tool.image_to_string(
    Image.open('/tmp/ticket/1.jpg').crop((1500, 70, 1850, 170)),
    lang='jpn',
    builder=pyocr.builders.TextBuilder()
)
print(txt)
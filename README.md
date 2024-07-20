# Persian Unicode Py 
.

.

.

.
## WHO NEED THIS?

in any program like Blender or Maya you can't type **Persian/Arabic** , with this library You Can Put Any **Persian/Arabic** Sentence in ANY PROGRAM SUPPORT utf8


This library only solves the problem of reversing the letters, if in your program when you write **Persian/Arabic** , it shows a square for each letter, or it doesn't show anything at all, you should use **Persian/Arabic** font.

Use this if **Persian/Arabic** is not displayed correctly (for example, it is the other way around, or it is an illusion).


## Example Code :
<pre>
  from PersianUnicode import PersianUnicode
  pu = PersianUnicode()
  print(pu.convert("سلام خوبی ؟ "))                                       # Common Use 
  print(pu.convert("12334", arabic_number = True))                      # replace EN number with Arabic Number
  print(pu.convert("سلام خوبی Hello World ؟ ", strip_line = True))        # Use strip() in every line
  print(pu.convert("سلام خوبی Hello World ؟ ", skip_other_char = True))   # skip char exclude persian/arabic, "skip_other_char" skip EN letters too
</pre>

**Important**: Use fonts that support persian/arabic letters in your Terminal/Application.




## The Persian Gulf forever, Arabian Gulf is FAKE

# Persian Unicode Py 
.
.
.
.
## WHY DO YOU NEED THIS

in any program like Blender or Maya you can't type Persian name of your model's , with this library You Can Put Any Persian Sentence in ANY PROGRAM SUPPORT utf8


This library only solves the problem of reversing the letters, if in your program when you write Farsi, it shows a square for each letter, or it doesn't show anything at all, you should use Farsi font.

Use this if Farsi is not displayed correctly (for example, it is the other way around, or it is an illusion).


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

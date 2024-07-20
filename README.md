# Persian Unicode Py 
Type persian in windows terminal or any application can't type arabic/persian




## WHY DO YOU NEED THIS
in any program like Blender or Maya you can't type Persian name of your model's , with this library You Can Put Any Persian Sentence in ANY PROGRAM SUPPORT utf8


این کتابخانه فقط مشکل برعکس شدن حروف رو حل میکنه ، اگ توی برنامه تون وقتی فارسی مینویسید یه مربع به ازای هر حرف نشون میده ، یا اصلا چیزی نشون نمیده باید از فونت فارسی استفاده کنید
این رو در صورتی استفاده کنید که فارسی به صورت درستی نمایش داده نمیشه ( مثلا برعکس باشه ، یا توهم‌-توهم باشه )
## Example Code :
<pre>
  from PersianUnicode import PersianUnicode
  pu = PersianUnicode()
  print(pu.convert("سلام خوبی ؟ "))                                       # Common Use 
  print(pu.convert("12334", arabic_number = True))                      # replace EN number with Arabic Number
  print(pu.convert("سلام خوبی Hello World ؟ ", strip_line = True))        # Use strip() in every line
  print(pu.convert("سلام خوبی Hello World ؟ ", skip_other_char = True))   # skip char exclude persian/arabic, "skip_other_char" skip EN char too
</pre>

**Important**: Use fonts that support persian/arabic character in your Terminal/Application.

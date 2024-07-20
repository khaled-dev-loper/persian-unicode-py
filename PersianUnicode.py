#! python3
class PersianUnicode ():
    makesBeforeChasban = ['ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'ك', 'گ', 'ل', 'م', 'ن', 'ه', 'ی', 'ي', 'ئ'];
    makesAfterChasban = ['ا', 'آ', 'أ', 'إ', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'ك', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی', 'ي', 'ؤ', 'ئ'];
    reqularAlphabet = [
        'ا',
        'آ',
        'أ',
        'إ',
        'ب',
        'پ',
        'ت',
        'ث',
        'ج',
        'چ',
        'ح',
        'خ',
        'د',
        'ذ',
        'ر',
        'ز',
        'ژ',
        'س',
        'ش',
        'ص',
        'ض',
        'ط',
        'ظ',
        'ع',
        'غ',
        'ف',
        'ق',
        'ک',
        'ك',
        'گ',
        'ل',
        'م',
        'ن',
        'و',
        'ؤ',
        'ه',
        'ی',
        'ي',
        'ئ',
        'ء',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
    ];
    arabicAlphabet = [
        ['ﺍ', 'ﺍ', 'ﺎ', 'ﺎ'],
        ['ﺁ', 'ﺁ', 'ﺂ', 'ﺂ'],
        ['ﺃ', 'ﺃ', 'ﺄ', 'ﺄ'],
        ['ﺇ', 'ﺃ', 'ﺈ', 'ﺈ'],
        ['ﺏ', 'ﺑ', 'ﺐ', 'ﺒ'],
        ['ﭖ', 'ﭘ', 'ﭗ', 'ﭙ'],
        ['ﺕ', 'ﺗ', 'ﺖ', 'ﺘ'],
        ['ﺙ', 'ﺛ', 'ﺚ', 'ﺜ'],
        ['ﺝ', 'ﺟ', 'ﺞ', 'ﺠ'],
        ['ﭺ', 'ﭼ', 'ﭻ', 'ﭽ'],
        ['ﺡ', 'ﺣ', 'ﺢ', 'ﺤ'],
        ['ﺥ', 'ﺧ', 'ﺦ', 'ﺨ'],
        ['ﺩ', 'ﺩ', 'ﺪ', 'ﺪ'],
        ['ﺫ', 'ﺫ', 'ﺬ', 'ﺬ'],
        ['ﺭ', 'ﺭ', 'ﺮ', 'ﺮ'],
        ['ﺯ', 'ﺯ', 'ﺰ', 'ﺰ'],
        ['ﮊ', 'ژ', 'ﮋ', 'ﮋ'],
        ['ﺱ', 'ﺳ', 'ﺲ', 'ﺴ'],
        ['ﺵ', 'ﺷ', 'ﺶ', 'ﺸ'],
        ['ﺹ', 'ﺻ', 'ﺺ', 'ﺼ'],
        ['ﺽ', 'ﺿ', 'ﺾ', 'ﻀ'],
        ['ﻁ', 'ﻃ', 'ﻂ', 'ﻄ'],
        ['ﻅ', 'ﻇ', 'ﻆ', 'ﻈ'],
        ['ﻉ', 'ﻋ', 'ﻊ', 'ﻌ'],
        ['ﻍ', 'ﻏ', 'ﻎ', 'ﻐ'],
        ['ﻑ', 'ﻓ', 'ﻒ', 'ﻔ'],
        ['ﻕ', 'ﻗ', 'ﻖ', 'ﻘ'],
        ['ک', 'ﻛ ', 'ﻚ', 'ﻜ'],
        ['ک', 'ﻛ ', 'ﻚ', 'ﻜ'],
        ['ﮒ', 'ﮔ', 'ﮓ', 'ﮕ'],
        ['ﻝ', 'ﻟ', 'ﻞ', 'ﻠ'],
        ['ﻡ', 'ﻣ', 'ﻢ', 'ﻤ'],
        ['ﻥ', 'ﻧ', 'ﻦ', 'ﻨ'],
        ['ﻭ', 'ﻭ', 'ﻮ', 'ﻮ'],
        ['ﺅ', 'ﺅ', 'ﺆ', 'ﺆ'],
        ['ﻩ', 'ﻫ', 'ﻪ', 'ﻬ'],
        ['ى', 'ﯾ', 'ﯽ', 'ﯿ'],
        ['ى', 'ﯾ', 'ﯽ', 'ﯿ'],
        ['ﺉ', 'ﺋ', 'ﺊ', 'ﺌ'],
        ['ﺀ', 'ﺀ', 'ﺀ', 'ﺀ'],
        ['١', '١', '١', '١'],
        ['٢', '٢', '٢', '٢'],
        ['٣', '٣', '٣', '٣'],
        ['٤', '٤', '٤', '٤'],
        ['٥', '٥', '٥', '٥'],
        ['٦', '٦', '٦', '٦'],
        ['٧', '٧', '٧', '٧'],
        ['٨', '٨', '٨', '٨'],
        ['٩', '٩', '٩', '٩'],
        ['٠', '٠', '٠', '٠'],
    ];
    Arabicnumbers = ['١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠'];
    Englishnumber = ["0", "9", "8", "7", "6", "5", "4", "3", "2", "1"];
    def __init__(self, debug = True):
        if debug:
            print("Hello Unicode Translator")
    def convert(self, string = "", arabic_number = True, strip_line = True, skip_other_char = False):
        """
            string: your string msg
            arabic_number: replace EN number with Arabic number
            strip_line: use strip() in line of your input 
            skip_other_char: skip symbol and other character language ( like English Character ), true this return ONLY Persian Text
        """
        if string.strip() == "":
            return "__NO_INPUT__"
        # Split By Line 
        strArray = string.split("\n");
        convertedStrArray = [];
        for j, ej in enumerate(range(0, len(strArray))):
            s = strArray[j]
            if strip_line:
                s = s.strip();
            # Split By Word
            strInner = s.split(" ");
            convertedStr = "";
            for m in strInner:
                # TODO: m is our str
                atleastOne = False
                convertedWord = ''
                for i, ei in enumerate(m):
                    beforeChasban, afterChasban = False, False;
                    try:
                        currentCharPos = self.reqularAlphabet.index(ei)
                        if (i > 0) :
                            if (m[i - 1] in self.makesBeforeChasban):
                                atleastOne = True;
                                beforeChasban = True;
                            else:
                                beforeChasban = False;
                        else :
                            beforeChasban = False;
                        if (i < (len(m) - 1) ) :
                            if (m[i + 1] in self.makesAfterChasban):
                                atleastOne = True;
                                afterChasban = True;
                            else:
                                afterChasban = False;
                        else:
                            afterChasban = False;
                        if (not beforeChasban and not afterChasban):
                            convertedWord = self.arabicAlphabet[currentCharPos][0] + convertedWord;
                        elif (beforeChasban and not afterChasban):
                            convertedWord = self.arabicAlphabet[currentCharPos][2] + convertedWord;
                        elif (not beforeChasban and afterChasban):
                            convertedWord = self.arabicAlphabet[currentCharPos][1] + convertedWord;
                        elif (beforeChasban and afterChasban):
                            convertedWord = self.arabicAlphabet[currentCharPos][3] + convertedWord;
                    except ValueError:
                        # char is not found
                        if not skip_other_char:
                            if atleastOne :
                                convertedWord = m[i] + convertedWord;
                            else :
                                convertedWord += m[i];
                convertedStr = convertedWord + ' ' + convertedStr;
            convertedStrArray.append(convertedStr);
            # Result 
            finalValue = "\n".join(convertedStrArray);
            if arabic_number:
                finalValue.replace(self.Arabicnumbers[0], self.Englishnumber[0]).replace(self.Arabicnumbers[1], self.Englishnumber[1]).replace(self.Arabicnumbers[2], self.Englishnumber[2]).replace(self.Arabicnumbers[3], self.Englishnumber[3]).replace(self.Arabicnumbers[4], self.Englishnumber[4]).replace(self.Arabicnumbers[5], self.Englishnumber[5]).replace(self.Arabicnumbers[6], self.Englishnumber[6]).replace(self.Arabicnumbers[7], self.Englishnumber[7]).replace(self.Arabicnumbers[8], self.Englishnumber[8])
        return finalValue.strip()


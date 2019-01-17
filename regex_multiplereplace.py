import re

str1 ="We have the following pins (ICC_CLK_IN#1), 'ICC_CLK_OUT#4' in REV1"
wordDict = {
    
    "ICC_CLK_IN#1": "STS_IN#0",
    "ICC_CLK_OUT#4": "ICC_CLK_OUT_GND#4"
}


def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]

    return rc.sub(translate, text)

# call the function and get the changed text
str2 = multiwordReplace(str1, wordDict)
print(str2)
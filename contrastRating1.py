'''
Given a contrast ratio and a boolean indicating whether the text is large, return the WCAG rating using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0
'''


def get_contrast_rating(ratio, is_large_text):

    ratio = float(ratio)
    if ratio >= 7.0 and is_large_text == False:
        return "AAA"
    elif ratio >= 4.5 and is_large_text == True:
        return "AAA"
    elif ratio >= 4.5 and is_large_text == False:
        return "AA"
    elif ratio >= 3.0 and is_large_text == True:
        return "AA"
    elif ratio < 4.5 and is_large_text == False:
        return "Fail"
    else:
        return "Fail"


print(get_contrast_rating("7.5", False)) #should return "AAA".
print(get_contrast_rating("4.8", False)) #should return "AA".
print(get_contrast_rating("4.2", False)) #should return "Fail".
print(get_contrast_rating("4.5", True)) #should return "AAA".
print(get_contrast_rating("3.0", True)) #should return "AA".
print(get_contrast_rating("2.7", False)) #should return "Fail".
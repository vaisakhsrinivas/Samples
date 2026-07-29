'''
Given two relative luminance values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:

Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0
'''


def get_contrast_rating(l1, l2, is_large_text):

    newl1 = l1+0.05
    newl2 = l2+0.05
    ratio = newl1/newl2
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


print(get_contrast_rating(1.0, 0.0, False)) #should return "AAA".
print(get_contrast_rating(0.9015, 0.1364, False)) #should return "AA".
print(get_contrast_rating(0.8965, 0.1628, False)) #should return "Fail".
print(get_contrast_rating(0.7469, 0.0957, True)) #should return "AAA".
print(get_contrast_rating(0.7489, 0.2018, True)) #should return "AA".
print(get_contrast_rating(0.6571, 0.1974, True)) #should return "Fail".
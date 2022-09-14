text = "X-DSPAM-Confidence:    0.8475";

num = text.find(':')

number = float(text[num+1:])

print(number)
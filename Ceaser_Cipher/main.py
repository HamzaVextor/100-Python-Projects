def ceaser(txt, n):
    ans = ""
    for i in range(len(txt)):
        ch = txt[i]

        if ch == " ":
            ans += " "

        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)

        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)

    return ans

txt = input("Enter a word or sentence: ")
n = 1
print("Text is:" + " " + txt)
print('Shift pattern is:' + " " + str(n))
print("Cipher Text is:" + " " + ceaser(txt,n))
    

print('\n')


def ceaser_crack(de_txt, gn):
    de_ans = ""
    for i in range(len(de_txt)):
        de_ch = de_txt[i]

        if de_ch == " ":
            de_ans += " "

        elif de_ch.isupper():
            de_ans += chr((ord(de_ch) - gn - 65) % 26 + 65)

        else:
            de_ans += chr((ord(de_ch) - gn - 97) % 26 + 97)

    return de_ans

de_txt = input("Enter a word or sentence: ")
gn = 1
print("Cipher Text is:" + " " + de_txt)
print('Shift pattern is:' + " " + str(gn))
print("Text is:" + " " + ceaser_crack(de_txt,gn))
    


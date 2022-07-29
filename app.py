import random

import streamlit as st


def genarr(mn=1, mx=10, mnv=0, mxv=1000, texpander=st, tc=0, w_s=True):
    if w_s:
        arr = str(tc) + '\n'
    else:
        arr = ''
    tc = int(tc)
    if mn > mx:
        texpander.code('😒Minimum length is greater than Maximum Length 😒')
        return
    if mnv > mxv:
        texpander.code('😒Minimum Value is greater than Maximum Value 😒')
        return
    for _ in range(tc):
        length = random.randint(mn, mx)
        if w_s:
            for i in range(length):
                arr = arr + str(random.randint(mnv, mxv)) + ' '
            arr = arr + '\n'
        else:
            a = []
            for i in range(length):
                a.append(random.randint(mnv, mxv))
            arr = arr + str(a) + '\n'
    texpander.code(arr)


st.title('TestCase Generator')
st.header("String")
expander = st.expander("Expand for a Random String")
c1, c2 = expander.columns([4,4])
case = c1.number_input("No. of Test Cases: ", min_value=1, step=1)
length1 = c2.number_input('Length of String', min_value=1, value=5, step=1)
with_sym = c2.checkbox("Without Symbols")


def gen(leng=5, tc=1, texpander=st, without_s=False):
    s = []
    leng = int(leng)
    tc = int(tc)
    for i in range(tc):
        word = ''
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's',
                   't',
                   'u',
                   'v', 'w', 'x', 'y', 'z']
        for k in range(leng):
            letter = random.randint(0, 26) % 26
            word = word + letters[letter]
        s.append(word)
    if without_s:
        words = str(tc) + '\n'
        for w in s:
            words = words + w + ' '
        texpander.code(words)
    else:
        texpander.code(s)


gen(length1, case, expander, with_sym)

st.header("Array")
expander2 = st.expander("Expand to generate a Random Array")
co1, co2 = expander2.columns([4, 4])
minl = co1.number_input("Min Length", min_value=1,step=1)
maxl = co2.number_input("Max length", min_value=1, step=1)
minv = co1.number_input("Min Value", step=1)
maxv = co2.number_input("Max Value", step=1)
ws = co1.checkbox("Without any symbols")
case = expander2.number_input("Test Cases", step=1)
genarr(minl, maxl, minv, maxv, expander2, case, ws)

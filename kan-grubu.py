mother = input("Lütfen annenizin kan grubunu giriniz: ")
father = input("Lütfen babanızın kan grununu giriniz: ")

yuzde100 = 100
yuzde75 = 75
yuzde50 = 50
yuzde25 = 25

mother1 = mother[0]
mother2 = mother[1]
father1 = father[0]
father2 = father[1]

sonuc = mother1 + father1
sonuc1 = mother1 + father2
sonuc2 = mother2 + father1
sonuc3 = mother2 + father2

sonucTek = sonuc[0]
sonucTek2 = sonuc1[0]
sonucTek3 = sonuc2[0]
sonucTek4 = sonuc3[0]

"""
_/﹋\_
(҂`_`)
<,︻╦╤─ ҉ - - - 
_/﹋\_
"""

if sonucTek == "A" and sonucTek2 == "A" and sonucTek3 == "A" and sonucTek4 == "A":
    print("Kan grubunun 'A' olma ihtimali %{}!".format(yuzde100))

elif sonucTek == "B" and sonucTek2 == "A" and sonucTek3 == "A" and sonucTek4 == "A":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde75, yuzde25))

elif sonucTek == "B" and sonucTek2 == "B" and sonucTek3 == "A" and sonucTek4 == "A":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde50, yuzde50))

elif sonucTek == "B" and sonucTek2 == "B" and sonucTek3 == "B" and sonucTek4 == "A":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde25, yuzde75))
#
elif sonucTek == "B" and sonucTek2 == "B" and sonucTek3 == "B" and sonucTek4 == "B":
    print("Kan grubunun 'B' olma ihtimali %{}!".format(yuzde100))

elif sonucTek == "A" and sonucTek2 == "A" and sonucTek3 == "B" and sonucTek4 == "B":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde50, yuzde50))

elif sonucTek == "A" and sonucTek2 == "A" and sonucTek3 == "A" and sonucTek4 == "B":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde75, yuzde25))

elif sonucTek == "A" and sonucTek2 == "B" and sonucTek3 == "A" and sonucTek4 == "B":
    print("Kan grubunun 'A' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde75, yuzde25))
#
elif sonucTek == "0" and sonucTek2 == "0" and sonucTek3 == "0" and sonucTek4 == "0":
    print("Kan grubunun '0' olma ihtimali %{}!".format(yuzde100))

elif sonucTek == "0" and sonucTek2 == "0" and sonucTek3 == "0" and sonucTek4 == "A":
    print("Kan grubunun 'A' olma ihtimali %{}, 'A' olma ihtimali %{}!".format(yuzde75, yuzde25))

elif sonucTek == "0" and sonucTek2 == "0" and sonucTek3 == "A" and sonucTek4 == "A":
    print("Kan grubunun '0' olma ihtimali %{}, 'A' olma ihtimali %{}!".format(yuzde50, yuzde50))

elif sonucTek == "0" and sonucTek2 == "A" and sonucTek3 == "A" and sonucTek4 == "A":
    print("Kan grubunun '0' olma ihtimali %{}, 'A' olma ihtimali %{}!".format(yuzde25, yuzde75))
#
elif sonucTek == "0" and sonucTek2 == "0" and sonucTek3 == "0" and sonucTek4 == "B":
    print("Kan grubunun '0' olma ihtimali %{}, 'B' olma ihtimali %{}".format(yuzde75, yuzde25))

elif sonucTek == "0" and sonucTek2 == "0" and sonucTek3 == "B" and sonucTek4 == "B":
    print("Kan grubunun '0' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde50, yuzde50))

elif sonucTek == "0" and sonucTek2 == "B" and sonucTek3 == "B" and sonucTek4 == "B":
    print("Kan grubunun '0' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde25, yuzde75))

elif sonucTek == "0" and sonucTek2 == "B" and sonucTek3 == "B" and sonucTek4 == "B":
    print("Kan grubunun '0' olma ihtimali %{}, 'B' olma ihtimali %{}!".format(yuzde25, yuzde75))

# python kan-grubu.py

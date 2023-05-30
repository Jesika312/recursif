def palindrome(kalimat):
    kalimat_balik= kalimat[::-1]
    if kalimat==kalimat_balik:
        return True
    else:
        return False
print(palindrome("kasur rusak"))
print(palindrome("duta wacana"))

def palindrome_rekursif(kalimat,depan,belakang):
    if depan==belakang:
        return True
    elif depan == belakang-1:
        if kalimat[depan] == kalimat[belakang]:
            return True
        else:
            return False
    else:
        if kalimat[depan] == kalimat[belakang]:
            return palindrome_rekursif(kalimat, depan+1, belakang+1)
        else:
            return False
        
kalimat="kasur rusak"
print(palindrome_rekursif(kalimat,0,len(kalimat)-1))
kalimat="duta wacana"
print(palindrome_rekursif(kalimat,0,len(kalimat)-1))

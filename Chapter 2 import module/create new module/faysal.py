def family():
    l = ""
    for i in li:
        l += "\n %s"%i
    return l
li = ["6 member of Faysal's family are:","",
      "Father: Hafez Abdul Latif","Mother: Parvin Akter",
      "Two sisters: Hafsa Akter Eva & Dr. Sayema Jahan",
      "Two brothers: Md. Faysal Ahmed & Md. Jobayer Ahmed Ansary"]    

def about():
    lii = ""
    for i in lf:
        lii += "\n %s"%i
    return lii
lf = ["About Faysal:","",
     "Name : Md. Faysal Ahmed.",
     "Study: Diploma in Computer Technology at Brahmanbaria Polytechnic Institute.",
     "Studied: Homna Islamia Dakhil Madrasah. Homna, Cumilla.",
     "Present Address: Vill- Islampur, Post- Budhanti, Upazila- Bijoynagar, District: Brahmanbaria.",
     "Permanent Address: Vill+Post+Upazilla- Homna, District- Cumilla.",
     "Religion : Islam.",
     "Marital Status: Unmarried.",
     "Website: www.faysalf.me",
     "Learning Website: www.pythoncode.cf",
     "News Portal: www.newsbd21.tk",
     "Facebook : www.facebook.com/faysal.fb",
     "To know more details about Faysal visit www.faysalf.me/about.html"]
if __name__=="__main__":
    print(about())
    print(family())
    

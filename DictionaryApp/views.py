from django.shortcuts import render
from difflib import SequenceMatcher,get_close_matches
import json

def home(req):
    if req.POST:
        data = json.load(open('DictionaryApp\dictionary.json'))
        user_input=req.POST['word'].upper()
        user_input.lstrip()
        if user_input=="":
            return render(req,"home.html",{"description":"Please enter some word then click on search button !!!","req":True})

        keys_dict=[i.upper() for i in data.keys()]
        list_of_match_string=get_close_matches(user_input,keys_dict,cutoff=0.66)
        match_string_dict={}
        for i in list_of_match_string:
            match_string_dict[i]=SequenceMatcher(None,user_input,i).ratio()
        max_ratio_match=int(max(match_string_dict.values()))
        if user_input in keys_dict:
            return render(req,"home.html",{"description":data[user_input].lower(),"req":True})
        elif(len(match_string_dict)>0):
            string=""
            for k,v in match_string_dict.items():
                if(v>max_ratio_match):
                    string=string+"/"+k
            string="Please enter valid word may be like "+string
            return render(req,"home.html",{"description":string.lower(),"req":True})
        else:
            return render(req,"home.html",{"description":"Your word is not present please double check it sorry !!!","req":True})
    return render(req,"home.html",{"req":False})
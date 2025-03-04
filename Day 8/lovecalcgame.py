def calculate_love_score(name1,name2):
    name3= (name1+name2).lower()
    true_list=["t","r","u","e"]
    love_list=["l","o","v","e"]
    count_true=0
    count_love=0
    for letter in name3:
        if letter in true_list:
            count_true+=1
    for letter in name3:
        if letter in love_list:
            count_love+=1
    love_score= int(str(count_true)+str(count_love))
    print(love_score)

calculate_love_score("Kanye West","Kim Kardashian")
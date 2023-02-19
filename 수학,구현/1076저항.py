color_dic={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
sum=0
first=input()
sum=color_dic[first]*10
second=input()
sum+=color_dic[second]
third=input()
sum*=10**color_dic[third]
                                  
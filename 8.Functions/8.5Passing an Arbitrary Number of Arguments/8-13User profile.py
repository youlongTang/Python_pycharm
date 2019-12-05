#user_profile.py
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的关于用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

#改动user_profile的说明
#user_profile = build_profile('albert','einstein',Location='princeton',field='physics')
#print(user_profile)
user_profile = build_profile('Youlong','Tang',appearance = 'handsome',location = 'HuNan',field ='internet' )
print(user_profile)
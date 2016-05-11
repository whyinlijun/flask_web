#!/usr/bin/python env
#coding=utf-8
'''
@author by yin lijun
partition:
        address,str 
功能：将输入的用逗号（可以不区分大小写）分隔的信息，分解为字典数据返回，数据位置任意
示例数据：
        尹礼俊，15357883396，0553-3816932-125,安徽省芜湖市美加印象A5-2-501，241000

'''
import re
def addSpilt(address):
    assert isinstance(address, object)
    address=re.sub(u'\，',',',address)
    count=0
    for i in address:
        if i==',':
            count+=1
    if count<=4:
        address_dict={'address':'','tel':'','zip':'','mobile':'','name':''}
        re_com_mobile=re.compile('(?:(?:86|\+86)-?)?(?:1\d{10})(?:\-\d{3,5})?')
        re_com_tel=re.compile('0\d{2,3}-\d{5,8}(?:\-\d{3,5})?')
        re_com_zip=re.compile('\d{6}')
        if re_com_mobile.search(address):
            address_dict['mobile']=re_com_mobile.search(address).group()
            address=re_com_mobile.sub('',address)
        if re_com_tel.search(address):
            address_dict['tel']=re_com_tel.search(address).group()
            address=re_com_tel.sub('',address)
        if re_com_zip.search(address):
            address_dict['zip']=re_com_zip.search(address).group()
            address=re_com_zip.sub('',address)
        list_address=re.split(',',address)
        sort_list=sorted(list_address,key=lambda x:len(x),reverse=1)
        if len(sort_list)>2:
            address_dict['address']=sort_list[0]
            address_dict['name']=sort_list[1]
    else:
        address_dict=None
    return address_dict

if __name__=="__main__":
    address="尹礼俊，15357883396，0553-3816932-125,安徽省芜湖市美加印象A5-2-501，241000"
    address_dict=addSpilt(address)
    if address_dict:
        for key in address_dict:
            print key+': '+address_dict[key].decode('utf8')
    else:
        print u'分隔符过多，超出预设项，请检查！！'
            


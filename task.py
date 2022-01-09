#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import codecs


# In[3]:
import unicodedata
#print(repr(ite))

#filename = 'F://my_data/work_on_R/Project_vidhan_sabha_election/kerala/cpim_kerala_0804.csv'
#reader = unicode_csv_reader(open(filename))
#print(reader)

# In[92]:


item = "<U+0BAA><U+0BBF><U+0BB0><U+0B9A><U+0BCD><U+0B9A><U+0BBE><U+0BB0><U+0BA4><U+0BCD><U+0BA4><U+0BBF><U+0BB2><U+0BCD> <U+0BB5><U+0BA9><U+0BCD><U+0BAE><U+0BC1><U+0BB1><U+0BC8> <U+0BA4><U+0BC2><U+0BA3><U+0BCD><U+0B9F><U+0BC1><U+0BAE><U+0BCD> <U+0BB5><U+0BBF><U+0BA4><U+0BAE><U+0BBE><U+0B95> <U+0BAA><U+0BC7><U+0B9A><U+0BBF>, <U+0BA4><U+0BC7><U+0BB0><U+0BCD><U+0BA4><U+0BB2><U+0BCD> <U+0BB5><U+0BBF><U+0BA4><U+0BBF><U+0BAE><U+0BC1><U+0BB1><U+0BC8><U+0B95><U+0BB3><U+0BCD> <U+0BAE><U+0BC0><U+0BCD><U+0BB1><U+0BBF><U+0BAF><U+0BA4><U+0BBE><U+0BB2><U+0BCD> <U+0B85><U+0B9F><U+0BC1><U+0BA4><U+0BCD><U+0BA4> 24-<U+0BAE><U+0BA3><U+0BBF> <U+0BA8><U+0BC7><U+0BB0><U+0BAE><U+0BCD> <U+0BAA><U+0BBF><U+0BB0><U+0B9A><U+0BCD><U+0B9A><U+0BBE><U+0BB0><U+0BAE><U+0BCD> <U+0B9A><U+0BC6><U+0BAF><U+0BCD><U+0BAF> <U+0BA4><U+0B9F><U+0BC8>"
item = item.replace("<","\\").replace(">",",").replace("+","").lower()
#print(item)
li = list(item.split(","))
stringS =""

for i in li:
    print(i.encode().decode('unicode_escape'),end="")
#print(u''.join(li))
#print(b'li'.decode('unicode_escape'))
#byte_form = codecs.decode('utf-8')
#byte_form =item.encode(byte_form)
#decoded_value = codecs.decode(byte_form)
#print("decoded string: : \n" + decoded_value)
#print(u''.join(li))
#print(item.encode('utf-8'))
#for c in item:
  #  print(item.encode('utf-8'))
#for c in item:
   # print(u' '.join(item))
#li = list(item.split(" "))

#print(li)

#print(u' '.join(item))
#for c in li:
#    print(repr(c),c,unicodedata.category(c))
#print(repr(item),item,unicodedata.category(item))
#print("item : \n"+u'')
#item1 = item.lower()
#print("original in lower: \n" + item1)

#item2 = item1.replace('>', '')
#print("after replacing > : \n" + item2)
#item3 = item2.replace('+', '')
#print("after replacing + : \n" + item3)
#item4 = item3.replace('<', '\\')
#print("after replacing > by  : \n" + item3)
#print("item 3: \n"+item3)

#print("item3: \n"+item3)
#byte_form = item4.replace("\\","[\]")
#print(byte_form)
#byte_form = item4.encode('utf-8')
#iisue
#print(byte_form)
#decoded_value = codecs.decode(byte_form)
#print("decoded string: : \n" + decoded_value)

#deode should be here
# In[82]:

#item7 = decoded_value
#item7 ="mamata banergee \u0baa\u0bbf\u0bb0\u0b9a\u0bcd\u0b9a\u0bbe\u0bb0\u0ba4\u0bcd\u0ba4\u0bbf\u0bb2\u0bcd \u0bb5\u0ba9\u0bcd\u0bae\u0bc1\u0bb1\u0bc8 \u0ba4\u0bc2\u0ba3\u0bcd\u0b9f\u0bc1\u0bae\u0bcd \u0bb5\u0bbf\u0ba4\u0bae\u0bbe\u0b95 \u0baa\u0bc7\u0b9a\u0bbf, \u0ba4\u0bc7\u0bb0\u0bcd\u0ba4\u0bb2\u0bcd \u0bb5\u0bbf\u0ba4\u0bbf\u0bae\u0bc1\u0bb1\u0bc8\u0b95\u0bb3\u0bcd \u0bae\u0bc0\u0bcd\u0bb1\u0bbf\u0baf\u0ba4\u0bbe\u0bb2\u0bcd \u0b85\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4 24-\u0bae\u0ba3\u0bbf \u0ba8\u0bc7\u0bb0\u0bae\u0bcd \u0baa\u0bbf\u0bb0\u0b9a\u0bcd\u0b9a\u0bbe\u0bb0\u0bae\u0bcd \u0b9a\u0bc6\u0baf\u0bcd\u0baf \u0ba4\u0b9f\u0bc8"
#byte7 = item7.encode('utf-8')
#print(byte7)
#encoding = item.encode('utf-8')
#print("encode : \n"+encoding.)
#decode = encoding.decode('utf-8')
#print("decode : \n"+decode)
#decoded_string =codecs.decode(item)

#print(decoded_string)


# In[97]:






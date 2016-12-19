#/user/bin/env python
# _*_ coding:utf-8 _*_

import json
data = {'k1':123,'k2':'Hello'}
json.dump(data,open('D://temp.txt','w+'))
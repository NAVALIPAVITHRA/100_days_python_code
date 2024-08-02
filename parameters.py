
import math
def cal(height,width,cover):
    number=(height*width)/cover
    round=math.ceil(number)
    print(round)
test_h=int(input())
test_W=int(input())
coverage=5
cal(height=test_h,width=test_W,cover=coverage)
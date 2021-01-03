weight = int(input('請輸入體重: '))
height = int(input('請輸入身高: '))
height = height / 100 # 換成公尺
bmi = weight / height / height  
if bmi >=18.5 and bmi <24:
    print('你的bmi值為', bmi,"體重正常")
elif bmi < 18.5:
    print('你的bmi值為', bmi, '屬體重過輕')
else:
    if bmi >=24 and bmi <=27:
        print('你的bmi值為', bmi,"過重")
    elif bmi>=27 and bmi <=30:
        print('你的bmi值為', bmi,"輕度肥胖")
    elif bmi>=30 and bmi <=35:
        print('你的bmi值為', bmi,"重度肥胖")
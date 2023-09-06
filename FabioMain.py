import discord
from discord.ext import commands
import random
import os
import emoji

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', help_command=None, case_insensitive=True, intents=intents)

#책구절
a1="쉰, 예순에도 그렇지 못하다면\r\n차라리 죽음이 나으리라.\r\n- 워즈워스, 무지개"
a2="나는 틈바구니에서 너를 뽑아\r\n여기 내 손 안에 쥐고 있다.\r\n온통 뿌리째.\r\n- 테니슨, 담 틈에 핀 꽃"
a3="어떠한 입도, 아니 어떠한 정신도 표현하지 않았었지.\r\n마음에 들었던 것, 영혼이 짐작했던 것을.\r\n- 홉킨스, 봄과 가을 - 어린 소녀에게"
a4="아, 저주스런 낭패로다.\r\n그것을 바로잡으려 내가 태어나다니.\r\n- 윌리엄 셰익스피어,햄릿"
a5="그리하여 우리는 조류를 거스르는 배처럼 끊임없이 과거로 떠밀려 가면서도\r\n앞으로, 앞으로 계속 나아가는 것이다.\r\n-F.스콧 피츠제럴드, 위대한 개츠비"
a6="그대여 안녕, 잠시 동안만.\r\n다시 돌아오마, 내 사랑아. 천만리 먼 길이라도.\r\n- 번스, 한 송이 빨간 장미"
a7="그러나 멀지 않아 그녀의 의복이 마신 물로 무거워져, 곱게 노래하는 불쌍한 그 애를 진흙 속으로 끌고 갔지.\r\n- 윌리엄 셰익스피어, 햄릿"
a8="저 거울은 그이의 매무새 비치며 밝게 빛난다.\r\n- 브라우닝, 어느 인생의 사랑"
a9="사나운 소년은 꺾고 말았네, 들에 핀 장미를.\r\n장미는 저항하며 찔렀지만 애원도 한숨도 소용없는 것.\r\n- 괴테, 들장미"
a10="인간이 숨 쉬고 눈으로 보는 한\r\n이 노래 살아서 그대에게 생명 주리.\r\n- 세익스피어, 그대를 여름날에 견주리까"
a11="아, 또 갑자기 쳐든 눈초리에\r\n그의 영혼이 내 영혼과 합하여\r\n마디마디 하소연이 그의 사랑을 더욱 빛나게 할 제.\r\n- 단테 로세티, 사랑의 편지"
a12="어둠 속에 누워 꿈꾸면서 저는 당신을 생각할 겁니다.\r\n아니, 어쩌면 잊을지도 몰라요.\r\n- 크리스티나 로세티, 나 죽거든, 사랑하는 이여"
a13="조금이나마 인간은 참 아름다움을 보고\r\n짧은 인생이지만 완전하게 할 수 있다.\r\n- 존슨, 고귀한 품성"
a14="끝없는 바다로부터 왔던 이 몸이\r\n다시금 고향 향해 돌아갈 때에\r\n움직여도 잔잔해서 거품이 없는 잠든 듯한 밀물이 되어 다오.\r\n- 테니슨, 모래펄을 건너며"
a15="활짝 핀 꽃을 보기에 쉰 봄이 너무나 짧으니\r\n수풀 있는 곳으로 나는 가야지.\r\n- 하우스먼, 나무 중 가장 사랑스러운"
a16="당신이 내 곁을 떠나가 버려도\r\n당신을 그리는 내 마음 위에 사랑은 잠들리라.\r\n- 셸리, 음악은 부드러운 음성 사라져도"
a17="이기심은 사랑을 자극하기 쉬운 성품이다.\r\n이 점을 곰곰이 생각해 봐야 한다.\r\n- 나다니엘 호손, 주홍글씨"
a18="한 쌍의 젊은이가 서로 사랑 하는 것은 놀라운 일이 아니지만,\r\n서로를 사랑하는 한 쌍의 노인을 보는 것은 가장 아름다운 일이다.\r\n- 윌리엄 새커리, 베니티 페어"
a19="이상은 신호등과 같다.\r\n이상이 없다면 확고한 방향이 없고,\r\n방향이 없다면 삶의 의미가 없다.\r\n- 레오 톨스토이, 안나 카레니나"
a20="스스로 가여워하는\r\n야생의 짐승을 본 적 있는가\r\n작은 새 조차 얼어 죽어 가지에서\r\n떨어지더라도 자신을 동정하지 않는다.\r\n- D.H로렌스, 모리와 함께한 화요일"
a21=""

#사랑해
b1="고맙군."
b2="그래."
b3="......."
b4="*(못 들은 듯 창 밖을 보고 있다...)*"
b5="*(책에 시선을 두고 있다...)*"
b6=""

#피셔
c1="...그를 언급하는 이유가 뭐지."
c2="가이 피셔. 내 오랜 벗이여, 언제쯤 온전히 나를 사랑할지."
c3="피셔... 흠, 보고싶군."
c4="그가 어디에 있는지 알고있나."
c5="가이 피셔. 내가 사랑하는 이라네."
c6=""

#뭐 먹었어?
e1=emoji.emojize(":banana:")
e2=emoji.emojize(":mango:")
e3=emoji.emojize(":olive:")
e4=emoji.emojize(":red_apple:")
e5=emoji.emojize(":ear_of_corn:")
e6=emoji.emojize(":potato:")
e7=emoji.emojize(":bacon:")
e8=emoji.emojize(":croissant:")
e9=emoji.emojize(":pancakes:")
e10=emoji.emojize(":cheese_wedge:")
e11=emoji.emojize(":meat_on_bone:")
e12=emoji.emojize(":cut_of_meat:")
e13=emoji.emojize(":pizza:")
e14=emoji.emojize(":hot_dog:")
e15=emoji.emojize(":sandwich:")
e16=emoji.emojize(":taco:")
e17=emoji.emojize(":burrito:")
e18=emoji.emojize(":tamale:")
e19=emoji.emojize(":shallow_pan_of_food:")
e20=emoji.emojize(":green_salad:")
e21=emoji.emojize(":spaghetti:")
e22=emoji.emojize(":steaming_bowl:")
e23=emoji.emojize(":curry_rice:")
e24=emoji.emojize(":sushi:")
e25=emoji.emojize(":moon_cake:")
e26=emoji.emojize(":takeout_box:")
e27=emoji.emojize(":lobster:")
e28=emoji.emojize(":pie:")
e29=emoji.emojize(":ice_cream:")
e30=emoji.emojize(":beer_mug:")
e31=emoji.emojize(":tumbler_glass:")
e32=emoji.emojize(":wine_glass:")
e33=emoji.emojize(":cocktail_glass:")
e34=emoji.emojize(":cigarette:")
e35=""

#만지작
f1="무슨 짓이지."
f2="내게 손을 대지 마. 징그럽군."
f3="애인이 필요한가."
f4="*(말 없이 총을 겨눈다.)*"
f5="어울려 줄까. 내가 그러길 원하나 보군."
f6="내게 바라는 것이 있나."
f7=""

@bot.event
async def on_ready():             # 봇 실행 시 실행되는 함수
    print(f'{bot.user} 에 로그인하였습니다!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('피셔 생각'))

@bot.command()
async def about(ctx):    
    embed = discord.Embed(title='명령어', 
                            description='"책 읽어줘" : 랜덤으로 책의 한 구절을 읽어준다.\r\n"좋은 아침" : 파비오가 아침인사를 해준다.\r\n"좋은 밤" : 파비오가 저녁인사를 해준다.')
    await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg):
    if msg.author.bot: 
        return
        
    if '책 읽어' in msg.content:
        a = random.randrange(1,21)
        if a==1:
            d=a1
        elif a==2:
            d=a2
        elif a==3:
            d=a3
        elif a==4:
            d=a4
        elif a==5:
            d=a5
        elif a==6:
            d=a6
        elif a==7:
            d=a7
        elif a==8:
            d=a8
        elif a==9:
            d=a9
        elif a==10:
            d=a10
        elif a==11:
            d=a11
        elif a==12:
            d=a12
        elif a==13:
            d=a13
        elif a==14:
            d=a14
        elif a==15:
            d=a15
        elif a==16:
            d=a16
        elif a==17:
            d=a17
        elif a==18:
            d=a18
        elif a==19:
            d=a19
        elif a==20:
            d=a20
        else:
            d=a21
        await msg.channel.send(d)

    if '사랑해' in msg.content:
        a = random.randrange(1,6)
        if a==1:
            d=b1
        elif a==2:
            d=b2
        elif a==3:
            d=b3
        elif a==4:
            d=b4
        elif a==5:
            d=b5
        else:
            d=b6
        await msg.channel.send(d)
    
    
    if '피셔' in msg.content:
        a = random.randrange(1,6)
        if a==1:
            d=c1
        elif a==2:
            d=c2
        elif a==3:
            d=c3
        elif a==4:
            d=c4
        elif a==5:
            d=c5
        else:
            d=c6
        await msg.channel.send(d)

    if msg.content == '꿍':
        e=emoji.emojize(":face_with_diagonal_mouth:")
        await msg.channel.send(str(e))

    if msg.content == '꿍!':
        e=emoji.emojize(":confused_face:")
        await msg.channel.send(str(e))

    if msg.content == '꿍!!':
        e=emoji.emojize(":slightly_frowning_face:")
        await msg.channel.send(str(e))

    if msg.content == '꿍!!!':
        e=emoji.emojize(":disappointed_face:")
        await msg.channel.send(str(e))
    
    if msg.content == '꽝!!!':
        e=emoji.emojize(":face_with_spiral_eyes:")
        await msg.channel.send(str(e))

    if '뭐 먹었' in msg.content:
        a = random.randrange(1,35)
        if a==1:
            d=e1
        elif a==2:
            d=e2
        elif a==3:
            d=e3
        elif a==4:
            d=e4
        elif a==5:
            d=e5
        elif a==6:
            d=e6
        elif a==7:
            d=e7
        elif a==8:
            d=e8
        elif a==9:
            d=e9
        elif a==10:
            d=e10
        elif a==11:
            d=e11
        elif a==12:
            d=e12
        elif a==13:
            d=e13
        elif a==14:
            d=e14
        elif a==15:
            d=e15
        elif a==16:
            d=e16
        elif a==17:
            d=e17
        elif a==18:
            d=e18
        elif a==19:
            d=e19
        elif a==20:
            d=e20
        elif a==21:
            d=e21
        elif a==22:
            d=e22
        elif a==23:
            d=e23
        elif a==24:
            d=e24
        elif a==25:
            d=e25
        elif a==26:
            d=e26
        elif a==27:
            d=e27
        elif a==28:
            d=e28
        elif a==29:
            d=e29
        elif a==30:
            d=e30
        elif a==31:
            d=e31
        elif a==32:
            d=e32
        elif a==33:
            d=e33
        elif a==34:
            d=e34
        else:
            d=e35
        await msg.channel.send(str(d))
        
    if '만지작' in msg.content:
        a = random.randrange(1,7)
        if a==1:
            d=f1
        elif a==2:
            d=f2
        elif a==3:
            d=f3
        elif a==4:
            d=f4
        elif a==5:
            d=f5
        elif a==6:
            d=f6
        else:
            d=f7
        await msg.channel.send(d)
    


# 봇 실행
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)

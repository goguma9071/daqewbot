import discord
import asyncio
import random

client = discord.Client()

token = "ODY5NDE4MDA5NjQ1Njk1MDE2.YP96ng.PVT0z6sPAryMJ-3XijMsHWEcLJM"

@client.event
async def on_ready():
    print(client.user.name)
    print("사용법: !dq [명령어]")
    game = discord.Game("!dq 도와줘")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content == "!dq 고구마는":
        await message.channel.send("꼬3븅신")
    if message.content == "!dq 다큐는":
        await message.channel.send("14cm")
    if message.content == "!dq 곤잘은":
        await message.channel.send("본인피셜7.5cm+화풀이심함+나한테 뻐큐100개 날린적있음")
    if message.content == "!dq 로블은":
        await message.channel.send("Идиот Отаку")
    if message.content == "!dq 도와줘":
        await message.channel.send("사용법: !dq [명령어] 명령어: 고구마는 다큐는 곤잘은 로블은 나의 팬티색은? 오팬무 오늘의 곤잘 팬티는? 오늘의 운세")
    if message.content == "!dq 오팬무":
        await message.channel.send("핑크")
    if message.content == "!dq 나의 팬티색은?":
        ran = random.randint(0,9)
        if ran == 0:
            d = "노랑"
        if ran == 1:
            d = "주황"
        if ran == 2:
            d = "파랭"
        if ran == 3:
            d = "하늘색"
        if ran == 4:
            d = "보라"
        if ran == 5:
            d = "검정"
        if ran == 6:
            d = "민트"
        if ran == 7:
            d = "민트색을 입은걸 보니 민초를 사1랑한다는 아주 장한뜻을 품었구나 ㅎㅎㅎㅎ녀석 장하기도 하지"
        if ran == 8:
            d = "빨강색을 입은걸 보니 열렬한 공산당원인가 보군ㅎㅎㅎㅎㅎ 중국의 위구르와 티베트가 독립되길 비네.https://www.youtube.com/watch?v=efDu-KVBz6w"
        if ran == 9:
            d = "빨강"
        await message.channel.send(d)
    if message.content == "!dq 오늘의 곤잘 팬티는?":
        ran = random.randint(0,1)
        if ran == 0:
            d = "노팬티"
        if ran == 1:
            d = "팬티입음"
        await message.channel.send(d)
    if message.content == "!dq 집시는":
        await message.channel.send("씹덕")
    if message.content == "!dq 오늘의 운세":
        ran = random.randint(0,3)
        if ran == 0:
            d = "길가다가 똥밟음"
        if ran == 1:
            d = "니 하고 있는거 다 망함"
        if ran == 2:
            d = "탈모 생김+여친없음"
        if ran == 3:
            d = "pvp 10연패함"
        await message.channel.send(d)
    if message.content == "!dq kt5g는":
        await message.channel.send("여기서 가장 정상적인 사람")
    if message.content == "@ 다큐봇":
        await message.channel.send("핑하지마 병신아")


client.run(token)


import discord
from collections import Counter
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
import asyncio
import datetime
import random
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from PIL import Image, ImageEnhance
import pandas
import numpy
from discord.ext.commands import cooldown, BucketType
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

#testcommand
# defs
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='!', intents=intents, help_command=None)

testlist = []
# Get yesterdays date.
now = datetime.datetime.now()
yesterday1 = now - datetime.timedelta(days=1,hours=2)
twodaysago = yesterday1 - datetime.timedelta(days=1,hours=2)
onehourago = datetime.datetime.now() - datetime.timedelta(hours=2,minutes=30)


@client.event
async def on_ready():
    print('Bot {0.user} is ready xD'.format(client))
    game = discord.Game("!retard for help")
    await client.change_presence(status=discord.Status.idle, activity=game)

    #writes from file to testlist everytime its booted))))
    log = open("spammer.txt", "r")

    for line in log:
        testlist.append(line)


@client.command()
async def retard(ctx):
    embed = discord.Embed(title="Commandlist | <> = req, () = optional", color=0xc32222)
    embed.add_field(name="top <x> (hours)", value="shows top x chatters past 24/y hours", inline=True)
    embed.add_field(name="!addmsg <msg/link>", value="adds custom message to spammer (spammer types msg every hour)", inline=True)
    embed.add_field(name="!printmsglist", value="SENDS 50 DMS TO YOU!", inline=True)
    embed.add_field(name="!mickeymouse (name)", value="adds mickey mouse to pfp ", inline=True)
    embed.add_field(name="!user (name)", value="shows which roles user has ", inline=True)
    embed.add_field(name="!roles <rolename>", value="shows which members have the role", inline=True)
    embed.add_field(name="!nominate <name> <role>", value="vote a role for someone", inline=True)
    embed.add_field(name="!ban <name> <reason>", value="bans user", inline=True)
    embed.add_field(name="!mute <name> <reason>", value="mutes user", inline=True)
    embed.add_field(name="!fakedm <place> <name>, <msg>", value="places = https://imgur.com/a/6p40oOK | default, tobbankzoom, "
    "cage, lms, rope, tobbank, verz, xarp, clanwars, nyloboss, coxbank, edge, tobtele, juice", inline=True)
    embed.add_field(name="other", value="!topall, !apply, !allroles, !timeoutmyself, !imarat, !aooky, !benis, !mobywoby", inline=True)
    embed.add_field(name="!deepfry (user) (\"strong\")",
                    value="deepfry img - if u type \"strong\" after, it will be strong", inline=True)
    await ctx.send(embed=embed)


@client.command()
async def addmsg(ctx, *, arg1):
    writetofile = str(arg1)

    f = open("spammer.txt", "a")
    f.write(writetofile + "\n")
    print(datetime.datetime.now())
    #print(writetofile)
    f.close()
    await ctx.send(f"{arg1} was added to the list", delete_after=5)
    print(f"{arg1} was added to the list by {ctx.message.author}")


@client.command()
async def timeoutmyself(ctx):
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await user.add_roles(role)
    await ctx.send(f"{user.mention} has muted themselves lmao")
    await asyncio.sleep(120)
    await user.remove_roles(role)


@commands.command()
async def servers1(ctx):
    if ctx.user.id == 228143014168625153:
        activeservers = client.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)

@client.event
async def on_member_update(before,after):  # role changes
    channel = client.get_channel(878995328257359952)
    changed_role_set = set(before.roles) ^ set(after.roles)
    if len(changed_role_set) > 0:
        changed_role = next(iter(changed_role_set))
        # and then answer
        await channel.send(f"The role {changed_role.name} got either removed or added to the user {after.name}")


@client.event #gets member roles when they leave
async def on_member_remove(member):
    print(f"{member} left ...!")
    channel = client.get_channel(872830642646302812) #my discord 872830642646302812 sned 783483960889966615
    guild = client.get_guild(783483960889966613) #my disc 305380209366925312 sned 783483960889966613

    rolelist = [r.mention for r in member.roles if r != guild.default_role]
    rolelist3 = [r.name for r in member.roles if r != guild.default_role]
    roles = ", ".join(rolelist)
    roles3 = ", ".join(rolelist3)
    rolesprint = roles.replace('@', '')
    rolesprint = rolesprint.replace('&', '')
    print(rolesprint)

    name = member.id
    if len(rolesprint) > 1:
        f = open("data.txt", "a")
        f.write(str(name) +"," + " " + str(rolesprint + "\n"))
        f.close()

    embed = discord.Embed(title=f"{member} has left and had following roles:",
                          description=f"{roles3}", color=0xc32222)

    await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    f = pandas.read_csv('data.txt', sep=',', header=None, error_bad_lines=False, names = list(range(0,100)))
    rowcount = f[f.columns[0]].count()
    susgeids = []
    for x in range(rowcount):
        susgeids.append(f.at[x,0])

    #print(susgeids)

    if member.id in susgeids:
        column = (f.loc[f[0] == member.id].index.to_numpy()) #gets column number
        #rows = f.shape[int(column)] #number of rows (4 means 0-1-2-3)
        #print(column)

        try:
            for x in range(200):
                roleid = f.at[int(column),x+1]
                #print(roleid)
                roleid = roleid.replace('<', '')
                roleid = roleid.replace('>', '')
                roleid = roleid.replace(' ', '')
                roleid = int(roleid)
                #print(roleid)

                role = discord.utils.get(member.guild.roles, id=roleid) #<@&305384076880117760>
                await member.add_roles(role)
        except: #above errors unless someone has 100+ roles -> comes here and deletes the line with their name/role from file
            with open("data.txt", 'r') as read_file:
                lines = read_file.readlines()

            print(int(column))
            currentLine = 0
            with open("data.txt", 'w') as write_file:
                for line in lines:
                    if currentLine == int(column):
                        pass
                    else:
                        write_file.write(line)

                    currentLine += 1



@client.command()
async def user(ctx,  *, user: discord.Member = None):
    if not user:
        user = ctx.message.author
    rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
    roles = ", ".join(rolelist)
    numberofroles = (roles.count("@"))

    embed = discord.Embed(title=f"{user} has {numberofroles} roles:",
                          description=f"{roles}", color=0xc32222)

    await ctx.send(embed=embed)


@client.command()
async def allroles(ctx):
    embed = discord.Embed(title="All roles :",
                          description=", ".join([str(r.mention) for r in ctx.guild.roles]), color=0xc32222)
    await ctx.send(embed=embed)


@client.command()
async def roles(ctx, *, role : discord.Role):
    embed = discord.Embed(title=f"User with {role.name}",
                          description="\n".join(str(role) for role in role.members), color=0xc32222)
    await ctx.send(embed=embed)

@client.command()
async def fakedm(ctx, test, *arg):
    arg = str(arg)
    print(arg)
    arg = arg.replace("(", "")
    arg = arg.replace(")", "")
    arg = arg.replace("\'", "")
    arg,kwarg = arg.split(",,", 1) #split by "double comma"
    arg = arg.replace(",", "")
    kwarg = kwarg.replace("\"", "")
    kwarg = kwarg.replace(",", "")

    if kwarg[0] == " ":
        kwarg = kwarg[1:]

    kwarg = kwarg.capitalize()
    kwarg = " " + kwarg

    title_font = ImageFont.truetype('osrs-font.ttf', 16) #text and font size
    title_text = str("From " + arg + ":" + kwarg)  #text split up from arg

    randit = random.randint(0,100000)
    a = "fakedm/made/fakedm"
    b = str(randit)
    c = str(ctx.author)
    d = ".png"
    e = a + b + c + d

    if test == "default":
        draw_image = Image.open("fakedm/pm-bg.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 84), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 83), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "coxbank":
        draw_image = Image.open("fakedm/coxbank.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 371), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 370), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "tobtele":
        draw_image = Image.open("fakedm/tobtele.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 374), title_text, fill=(0, 0, 0), font=title_font)  # black shadow/outline
        image_editable.text((5, 373), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "edge":
        draw_image = Image.open("fakedm/edge.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 397), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 396), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "cage":
        draw_image = Image.open("fakedm/cage.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 566), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 565), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "juice":
        draw_image = Image.open("fakedm/juice.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 393), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 392), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "lms":
        draw_image = Image.open("fakedm/lms.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 318), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 317), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "rope":
        draw_image = Image.open("fakedm/rope.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 331), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 330), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "tobbank":
        draw_image = Image.open("fakedm/tobbank.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 375), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 374), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "tobbankzoom":
        title_font = ImageFont.truetype('osrs-font.ttf', 16)  # text and font size
        title_text = str("From " + arg + ":" + kwarg)  # text split up from arg
        draw_image = Image.open("fakedm/tobbankzoom.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 71), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 70), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "nyloboss":
        draw_image = Image.open("fakedm/nyloboss.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 329), title_text, fill=(0, 0, 0), font=title_font)  # black shadow/outline
        image_editable.text((5, 328), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "clanwars":
        draw_image = Image.open("fakedm/clanwars.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 346), title_text, fill=(0, 0, 0), font=title_font)  # black shadow/outline
        image_editable.text((5, 345), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "verz":
        draw_image = Image.open("fakedm/verz.jpg")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 301), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 300), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    if test == "xarp":
        draw_image = Image.open("fakedm/xarp.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 408), title_text, fill=(0, 0, 0), font=title_font)  #black shadow/outline
        image_editable.text((5, 407), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)

    await ctx.send(file=discord.File(e))


@client.command()
@commands.cooldown(1,300, commands.BucketType.guild)
async def nominate(ctx, user : discord.Member, *, role :discord.Role):
    rolelist = [r.id for r in user.roles if r != ctx.guild.default_role]
    roles = "".join(str(rolelist))

    testvvv = str(role.id)
    if testvvv not in roles:
        embed = discord.Embed(title=f"{user} role vote",
                              description=f"{user.mention} has been nominated for {role.mention}. \n 7 🤝 to pass within 90s", color=0xc32222)
        sendmsg = await ctx.send(embed=embed)
        await sendmsg.add_reaction("🤝")


        for x in range(90):
            await asyncio.sleep(1)
            sendmsg = await ctx.channel.fetch_message(sendmsg.id)
            total_count = 0
            for r in sendmsg.reactions:
                total_count += r.count

            #print(sendmsg.reactions)

            if "count=7" in str(sendmsg.reactions) or "count=8" in str(sendmsg.reactions):
                await user.add_roles(role)
                embed = discord.Embed(title=f"{user} role vote passed",description=f"{user.mention} recieved {role.mention}", color=0xc32222)
                await ctx.send(embed=embed)
                break #exit loop

            while x >= 89:
                await sendmsg.delete()
                await ctx.send("vote failed")
    else:
        await ctx.send(f"{user} already has {role}")


@tasks.loop(seconds=3) #keep ROTM role on user id
async def rotm():
    guild = client.get_guild(783483960889966613) #server id
    member = guild.get_member(381646298975043586)#213355912344109056 caps  381646298975043586 horse
    role = get(guild.roles, name="RAT OF THE MONTH")  #  <@&880990822064087070>@MEGA RAT @King Rat @RAT OF THE MONTH @ratshit
    await member.add_roles(role)
@rotm.before_loop
async def before():
    await client.wait_until_ready()
rotm.start()

"""@tasks.loop(seconds=3) #keep ROTM role on user id
async def muted():
    guild = client.get_guild(783483960889966613) #server id
    member = guild.get_member(498314132630667275)#213355912344109056 caps  381646298975043586 horse
    role = get(guild.roles, name="Muted")  #  <@&880990822064087070>@MEGA RAT @King Rat @RAT OF THE MONTH @ratshit
    await member.add_roles(role)
@muted.before_loop
async def before():
    await client.wait_until_ready()
muted.start()"""


@tasks.loop(hours=1) #spammer1
async def spammer():
    onehourago = datetime.datetime.now() - datetime.timedelta(hours=2, minutes=30)
    count = 0
    channel = client.get_channel(783483960889966615)  #783483960889966615 (sned gneral)  872830642646302812 (my general)
    async for message in channel.history(limit=10, after=onehourago):
        if message.author != client.user:
            count += 1
    if count > 5:
        print(str(count) + " " + str(datetime.datetime.now()))
        await channel.send(random.choice(testlist))
    else:
        print(f"{datetime.datetime.now()} {count} messages sent past 30minutes - no spam sent")
@spammer.before_loop
async def before():
    await client.wait_until_ready()
spammer.start()

@client.command()
async def apply(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/783483960889966615/880128897256144917/unknown.png")

@client.command()
async def aooky(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/872830642646302812/880520501309632512/unknown.png")

@client.command()
async def mobywoby(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/610233217659830285.png?v=1")

@client.command()
async def benis(ctx):
    await ctx.send("https://media.discordapp.net/attachments/408495891750584320/853646413702365214/benis_typing.gif")

@client.command()
@commands.has_role("rat")
async def imarat(ctx):
    user = ctx.author
    await ctx.send(f"{user.mention}, you are already a rat", delete_after = 5)

@client.command()
async def ban(ctx, user : discord.Member = None, *, arg = None):
    if arg == None:
        embed = discord.Embed(description=f"_**<:xDSuccess:880972501390360597> {user} was banned**_",
                              color=0x0D8B0D)
    else:
        embed = discord.Embed(description=f"_**<:xDSuccess:880972501390360597> {user} was banned for {arg}**_", color=0x0D8B0D)

    await ctx.send(embed=embed)

@client.command()
async def mute(ctx, user : discord.Member = None, *, arg = None):
    if arg == None:
        embed = discord.Embed(description=f"_**<:xDSuccess:880972501390360597> {user} was muted**_",
                              color=0x0D8B0D)
    else:
        embed = discord.Embed(description=f"_**<:xDSuccess:880972501390360597> {user} was muted for {arg}**_", color=0x0D8B0D)

    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    if "<@!872826125175390300>" in message.content:
        angrymsglist = ["stfu retard", "stop pinging me", "?", "wwd", "wwd", "wwd", "ym"]
        await message.channel.send(random.choice(angrymsglist))
        await client.process_commands(message)

    else:
        await client.process_commands(message)

    """value31 = 0 #spams user everytype they type
    test = message.author.id
    if test == 613289927320272896 or test == 408283605253488643:
        while value31 < 20:
            await message.author.send(f"LOLOLOLOLOLOLOLO {value31}")
            value31 += 1"""


@client.event #errorhandlign
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('This command is on a %.2fs cooldown' % error.retry_after, delete_after=5)
    if isinstance(error, commands.MissingRole):
        member = ctx.author
        await ctx.send(f"{member.display_name} enjoy your rat role")
        member = ctx.author
        role = get(member.guild.roles,name="rat")  # <@&880990822064087070>@MEGA RAT @King Rat @RAT OF THE MONTH @ratshit
        await member.add_roles(role)

    raise error  # re-raise the error so all the errors will still show up in console





@client.command()
async def mickeymouse(ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.message.author

        foreground = Image.open("mickeyface.png")

        asset = user.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        background = Image.open(data)
        background.save("profile12.png")

        imageD = Image.open("profile12.png")
        imageD = imageD.convert('RGBA')

        imageD = imageD.resize((128, 128))
        imageD.paste(foreground, (0, -20), foreground)

        imageD.save("mickeymousePFPSAVED.png")
        await ctx.send(file=discord.File("mickeymousePFPSAVED.png"))


@client.command()
async def deepfry(ctx, user : discord.Member = None, *, arg = None):
    if not user:
        user = ctx.message.author

    asset = user.avatar_url_as(size=256)
    data = BytesIO(await asset.read())
    background = Image.open(data)
    background.save("distort/distort.png") #saves discord user pfp as file


    img = Image.open("distort/distort.png")
    img = img.convert('RGBA')

    img1 = img.filter(BLUR)
    img2 = img1.filter(EDGE_ENHANCE_MORE)
    test = ImageEnhance.Color(img2)
    test = test.enhance(15) #15 decent

    test = ImageEnhance.Brightness(test)
    test = test.enhance(5)

    test = ImageEnhance.Contrast(test)
    test = test.enhance(2)

    if arg == "strong":
        def find_coeffs(pa, pb):
            matrix = []
            for p1, p2 in zip(pa, pb):
                matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
                matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])

            A = numpy.matrix(matrix, dtype=float)
            B = numpy.array(pb).reshape(8)

            res = numpy.linalg.solve(A, B)
            return numpy.array(res).reshape(8)

        coeffs = find_coeffs(
            [(0, 0), (256, 0), (256, 256), (0, 256)],
            [(0, 0), (256, 0), (100, 200), (10, 200)])

        test = test.transform((256, 256), Image.PERSPECTIVE, coeffs,
                               Image.BICUBIC)

    test = test.resize((128,128))

    test.save("distort/distorted.png")
    await ctx.send(file=discord.File("distort/distorted.png"))

    """if test == "default":
        draw_image = Image.open("fakedm/pm-bg.png")
        image_editable = ImageDraw.Draw(draw_image)
        image_editable.text((6, 84), title_text, fill=(0, 0, 0), font=title_font)  # black shadow/outline
        image_editable.text((5, 83), title_text, fill=(0, 255, 255), font=title_font)
        draw_image.save(e)"""



client.command()
async def mickeymouseears(ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.message.author

        foreground = Image.open("mickeymouse.png")

        asset = user.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        background = Image.open(data)

        background = background.resize((128, 128))
        background.paste(foreground, (0, 0), foreground)

        background.save("profile.png")
        await ctx.send(file=discord.File("profile.png"))



@client.command()
async def total(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send(f"A total of {count} messages in {channel.mention}")


@client.command()
async def printmsglist(ctx):
    a_file = open("spammer.txt")
    lines = a_file.readlines()
    counter = 1
    for line in lines:
        await ctx.author.send(str(counter) + " : " + str(line))
        counter += 1

@client.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def top(ctx, arg1, kwarg = None, channel: discord.TextChannel=None):
    if not kwarg == None:
        hours = min(168,int(kwarg))
        now = datetime.datetime.now()
        yesterday1 = now - datetime.timedelta(hours=(2+hours))
        topamount = int(arg1)
        async with ctx.typing():
            await ctx.send("request received...", delete_after=5)
            top = Counter()
            channel = channel or ctx.channel
            # for channel in ctx.guild.text_channels:
            async for message in channel.history(limit=None, after=yesterday1):
                author = message.author
                if not author.bot:
                    top[author.name] += 1

            print(datetime.datetime.now())
            print(top.most_common(100))
            names1, messagecount2 = zip(*top.most_common(100))
            ifLessThan10 = min((len(messagecount2)), topamount, 25)

            embed = discord.Embed(title=f"Top {min(len(messagecount2), topamount, 25)} typers",
                                  description=f"{sum(messagecount2)} messages typed past {kwarg} hours", color=0xc32222)
            for y in range(0, ifLessThan10):
                embed.add_field(name=names1[y], value=messagecount2[y], inline=True)
            await ctx.send(embed=embed)

    else:

        now = datetime.datetime.now()
        yesterday1 = now - datetime.timedelta(days=1, hours=2)
        topamount = int(arg1)
        async with ctx.typing():
            await ctx.send("request received...", delete_after=5)
            top = Counter()
            channel = channel or ctx.channel
            #for channel in ctx.guild.text_channels:
            async for message in channel.history(limit=None,after=yesterday1):
                    author = message.author
                    if not author.bot:
                        top[author.name] += 1

            print(datetime.datetime.now())
            print(top.most_common(100))
            names1,messagecount2 = zip(*top.most_common(100))
            ifLessThan10 = min((len(messagecount2)),topamount,25)

            embed = discord.Embed(title=f"Top {min(len(messagecount2),topamount, 25)} typers", description=f"{sum(messagecount2)} messages typed past 24 hours", color=0xc32222)
            for y in range(0, ifLessThan10):
                embed.add_field(name=names1[y], value=messagecount2[y], inline=True)
            await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1,90, commands.BucketType.user)
async def topall(ctx, channel: discord.TextChannel=None):
    now = datetime.datetime.now()
    yesterday1 = now - datetime.timedelta(days=1, hours=2)
    async with ctx.typing():
        await ctx.send("request received...", delete_after=5)
        top = Counter()
        channel = channel or ctx.channel #channel typed in
        #for channel in ctx.guild.text_channels: #all channels / doesnt work if no perms
        async for message in channel.history(limit=None,after=yesterday1):
                author = message.author
                if not author.bot:
                    top[author.name] += 1

        print(datetime.datetime.now())
        print(top.most_common(100))
        names1,messagecount2 = zip(*top.most_common(100))
        ifLessThan10 = min((len(messagecount2)),100) #

        testvariable1 = str(sum(messagecount2)) #number of messages
        testvariable2 = str(len(names1)) #number of authors / active users

        await ctx.send(f"" + (testvariable1) +"Messages sent by " + (testvariable2) + " users")

        teststring = ""
        for y in range(0, ifLessThan10):
            teststring += (str(names1[y]) + ": " + str(messagecount2[y]) + " | ") #await ctx.send
        await ctx.send(teststring)




def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client.run(token)

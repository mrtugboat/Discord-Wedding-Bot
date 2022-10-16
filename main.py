import discord
from discord.ext import commands
from discord.ui import Button, View, Select



TOKEN = 'ADD YOUR TOKEN IN HERE FRIEND'
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    activity = discord.Activity(name="Wedding Bot", type=3)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    
    print(f"{client.user.name} is online !")


######################
#
# Make a role in your discord called "married" if a user accepts a role they become married
#
####################### 


@client.command()
async def marry(ctx, member : discord.Member):
    select = Select(placeholder=f"{member} Do you wish to get married to {ctx.author}", options=[
        discord.SelectOption(label="yes", emoji="💍", description="You accept there wedding request"),
        discord.SelectOption(label="no", emoji="⛔", description="You reject there wedding request")

    ])
    

    async def my_callback(interaction):
        if select.values[0] == "yes":
            role = discord.utils.get(ctx.guild.roles, name="married")
            await ctx.author.add_roles(role)
            await ctx.member.add_roles(role)
            print("User assigned a role")
            em = discord.Embed(
            title="Congragulations!",
            description=f"{member} and {ctx.author} are now married",
            color=discord.Color(0x00ff00)
            )
            em.set_thumbnail(url="https://www.brides.com/thmb/umh5TKE4fIOD5bbbmfTHzqqj2lM=/735x0/brides-cover-image-36476d79c52f4b6d8bc9894d859649a6.jpeg")
            em.set_image(url="https://media2.giphy.com/media/XH3jHyWBXOQBifW6Fe/giphy.gif")
            await ctx.send(embed=em)

        if select.values[0] == "no":
            em = discord.Embed(
            title="Rejected!",
            description=f"{member} rejected the wedding request",
            color=discord.Color(0x00ff00)
            )
            em.set_thumbnail(url="https://images.huffingtonpost.com/2011-02-27-NO.jpeg")
            em.set_image(url="http://38.media.tumblr.com/64a3744476a2a68bb9612774c14ee37f/tumblr_nwl9r5V2Wi1rlpicfo1_500.gif")
            await ctx.send(embed=em)

       
            
        await interaction.response.send_message(f"{member} said {select.values[0]} to getting married")





    select.callback = my_callback
    view = View()
    view.add_item(select)

    await ctx.send(f'{member} You have just recieved a wedding request from {ctx.author}', view=view)
    em = discord.Embed(
    title="Wedding Request!",
    description=f"",
    color=discord.Color(0x00ff00)
    )
    em.set_image(url="https://i.pinimg.com/originals/ec/da/eb/ecdaeb06d6649ed83d7c7b5caf0f3e24.gif")
    await ctx.send(embed=em)



























client.run(TOKEN)

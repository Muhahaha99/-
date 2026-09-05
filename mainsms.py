import discord,time
import discord
import requests
import time
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import subprocess
import colorama


# icewen_22


blacklist = [
    "191",
    "0657425404",
    "0952146877",
    "0634468945",
    "0996245095",
    "0652845465"
]  # กำหนเบอร์ที่จะไม่ให้ยิงได้



prefix = "!" #เปลี่ยน prefix ได้หากต้องการ
NAME = "ยิงเบอร์" #ชื่อช่องที่ต้องการให้พิม เช่น ยิงเบอร์•

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

        
        
@bot.event
async def on_connect():
    print(f"กำลังล็อกอินบอท : {bot.user}")
    time.sleep(1.0)
    print("ล็อกอินเสร็จสิ้นแล้ว")
    


    


    
    
    
@bot.command()
async def sms(ctx, phone, amount:int):
    # เช็คว่าเป็นช่องที่ถูกต้องหรือไม่
    if ctx.channel.name == NAME:

        if (phone in blacklist):
            await ctx.send(content="เบอร์นี้ยิงไม่ได้นะ")
            return
        
        if (amount < 10001):
            embes = discord.Embed(title="", description=f"`ICE ยิงเบอร์!!`\n ```เบอร์ : {phone}```\n ```จำนวน : {amount} ครั้ง```",color=discord.Color.blue())
						
            embes.set_footer(text="icewen_22")
            
            await ctx.reply(embed=embes)
            
            process = subprocess.Popen(["python", "apisms.py", phone, str(amount)])

        else:
            embed = discord.Embed(title="**ระบบยิงเบอร์ ( ดับยากกั้บบ  )**", description="**กรุณาอย่ายืงเกิน จำนวน 10000 ด้วยนะคะ !!**",color=nextcord.Color.red())
            await ctx.reply(embed=embed)
    else:
        await ctx.reply(f"`❌`  **คำสั่งนี้ไม่สามารถใช้ในช่องนี้ได้\n\nหากต้องการใช้งานโปรดติดต่อแอดมิน**")

    


    
    
    
bot.run("MTU0NDY5NzIzMDY5NzQzOTI0NA.GzZ0d5.4QDUSlVY_5Y5C1SvxRAIGlQ7nhsXbZts7bRmKo") #ใส่โทเค้นบอท
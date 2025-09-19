import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# تحميل بيانات الأبطال
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

CATEGORY_COLORS = {
    "B": 0x3498DB,
    "A": 0x9B59B6,
    "S": 0xF1C40F
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def بالدور(ctx, category: str = "S"):
    category = category.upper()
    for h in data['ابطال']:
        if category not in h['Category']:
            continue

        color = CATEGORY_COLORS.get(category, 0x95A5A6)

        # Embed البطل الأساسي
        embed_hero = discord.Embed(
            title=h['اسم'],
            description=f"**Class:** Main hero\n**Category:** {category}\n**Role:** {h['Role']}",
            color=color
        )
        embed_hero.set_thumbnail(url="https://www.allclash.com/wp-content/uploads/2025/05/Screenshot-294.png")

        # المهارات 1–5
        if h.get('Skills') and category == "S":
            for idx, skill in enumerate(h['Skills'], 1):
                skill_text = f"**Type:** {skill.get('type', '')}\n{skill.get('description', '')}"
                if skill.get('upgrade_preview'):
                    skill_text += f"\n**Upgrade Preview:**\n{skill['upgrade_preview']}"
                embed_hero.add_field(name=f"💥 {idx}. {skill['name']}", value=skill_text, inline=False)

        embed_hero.set_footer(text="Hero lvl: 60 | Stars: 5")
        await ctx.send(embed=embed_hero)

        # Talent 1 Embed
        embed_talent1 = discord.Embed(
            title="Talent 1: Arena",
            color=color
        )
        embed_talent1.set_image(url="https://cdn.discordapp.com/attachments/1414288440819712152/1414288535694868500/image.png?ex=68ced857&is=68cd86d7&hm=f13f892be0678dfed42cb583c87298fb0614f3490d53ffd423f27b28f0300a97&")
        embed_talent1.set_footer(text="Hero lvl: 60 | Stars: 5")
        await ctx.send(embed=embed_talent1)

        # Talent 2 Embed
        embed_talent2 = discord.Embed(
            title="Talent 2: Ancestral Trail",
            color=color
        )
        embed_talent2.set_image(url="https://cdn.discordapp.com/attachments/1414288440819712152/1414288631950086234/image.png?ex=68ced86e&is=68cd86ee&hm=781c16ee40193dadfaebe911014864428c76423a7c5f048031d26c9b40769c93&")
        embed_talent2.set_footer(text="Hero lvl: 60 | Stars: 5")
        await ctx.send(embed=embed_talent2)

        # Talent 3 Embed
        embed_talent3 = discord.Embed(
            title="Talent 3: Hunt",
            color=color
        )
        embed_talent3.set_image(url="https://cdn.discordapp.com/attachments/1414288440819712152/1414288703559303199/image.png?ex=68ced87f&is=68cd86ff&hm=145ce71d47f9b56cefd6964d5ebdbd706a02927ffe9cc9a52d82f42eaff7c096&")
        embed_talent3.set_footer(text="Hero lvl: 60 | Stars: 5")
        await ctx.send(embed=embed_talent3)

bot.run(os.getenv("MTM0MTI3MDE3NjQ2NDkwMDExNw.GC9mL-.N-NlMlNHHkaxog6-Shhk0BHR_FKo126lyXUyxA"))

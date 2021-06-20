from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.gess(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NAOKI Peler☑️**")
    await typew.edit("**NAOKI Peler✅**")
    sleep(1)
    await typew.edit("**ASEP Gilaa☑️**")
    await typew.edit("**ASEP Gilaa✅**")
    sleep(2)
    await typew.edit("**BENI Depresi☑️**")
    await typew.edit("**BENI Depresi✅**")
    sleep(2)
    await typew.edit("**YUHUU Gajelas☑️**")
    await typew.edit("**YUHUU Gajelas✅**")
    sleep(2)
    await typew.edit("**BRAYEN GJM!☑️**")
    await typew.edit("**BRAYEN GJM!✅**")
    sleep(2)
    await typew.edit("**CALA GJB!☑️**")
    await typew.edit("**CALA GJB!✅**")
    sleep(2)
    await typew.edit("**AYYA,MengRibet☑️**")
    await typew.edit("**AYYA,MengRibet✅**")
    sleep(2)
    await typew.edit("**BRILIAN,Mengintil☑️**")
    await typew.edit("**BRILIAN,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA SULTAN YANG BENER!**")

# Create by myself @suppnigga

CMD_HELP.update({
    "Sultanbot":
    "`.gess`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})

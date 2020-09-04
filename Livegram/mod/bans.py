from telethon import events
from Livegram.mod.sql.blacklist_sql import add_user_to_bl, rem_user_from_bl
import shlex
from Livegram import bot

def get_args(message):
    """Get arguments from message (str or Message), return list of arguments"""
    try:
        message = message.message.message
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let's assume that it's just one long message
    return list(filter(lambda x: len(x) > 0, split))

@bot.on(events.NewMessage(pattern='/ban'))
async def _(event):
    args = get_args(event)
    r = False
    user_id = args[0]
    if not user_id:
       await message.reply("/ban user_id reason")
       return
    try:
      reason = " ".join(args[1:])
    except:
      reason = "You are banned."
      
    add_user_to_bl(user_id, reason)
    
  
@bot.on(events.NewMessage(pattern='/unban'))
async def _(event):
    args = get_args(event)
    r = False
    user_id = args[0]
    if not user_id:
       await message.reply("/unban user_id")
       return
  
    rem_user_from_bl(user_id)
   
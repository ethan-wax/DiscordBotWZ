import discord
import vals
import requests
import json

client = discord.Client()

def get_stat(user, platform):
  """
  Retrieves the stats of the given player from the warzone API
  """
  url = 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/{0}/gamer/{1}/profile/type/mp'.format(platform, user)

  headers = {'Cookie': vals.COOKIE}

  response = requests.get(url, headers=headers)
  json_data = json.loads(response.text)
  return json_data['data']['username']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$stat'):
      args = message.content.split()
      await message.channel.send(get_stat(args[1],args[2]))

client.run(vals.TOKEN)
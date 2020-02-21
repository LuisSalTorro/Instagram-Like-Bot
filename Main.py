from LikeAutomation import LikeAutomation
import random

bot = LikeAutomation()
tags = bot.readFile("tags.txt")
searchTag = random.randrange(1,len(tags))
bot.searchBar(tags[searchTag])

print("You liked a total of " + bot.likePosts(50,5) + " posts during this session.")#(likes, seconds)


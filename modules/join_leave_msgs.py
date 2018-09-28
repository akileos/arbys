from client import client
import discord
import key


@client.member_join
async def join_notification(member: discord.Member):
	if member.guild.id == 364480908528451584:
		await client.get_channel(473570993072504832).send(f"New member joined the server! Member {len(member.guild.members)}: {member.mention}")


@client.member_leave
async def leave_notification(member: discord.Member):
	if member.guild.id == 364480908528451584:
		await client.get_channel(473570993072504832).send(f"Member has left the server: {member.name}#{member.discriminator} ({member.display_name}) ({member.id})\nNew member count: {len(member.guild.members)}")

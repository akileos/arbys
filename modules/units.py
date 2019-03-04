from client import client

import asyncio
import discord
import subprocess

client.basic_help(title="unit", desc="Converts units with the `units` Unix command.")
help_dict = {
	"Usage": f"`{client.default_prefix}unit <src units> [dst units]`",
	"Arguments": "`src units` - Source units to convert from. Supports any units the Unix `units` command supports (a *lot*!).\n`dst units` - (optional) Destination units to convert to.",
	"Description": "This units transforms one unit into another unit. The command uses the underlying `units` Unix command, and supports over 3000 different units.\nIf destination units are not provided, the source units will be converted into standard units for length/width/height.",
	"Example": f"`{client.default_prefix}units 1000km mi`\n`{client.default_prefix}units 0.0000026c`",
}
client.long_help(cmd="unit", mapping=help_dict)


@client.command(trigger="unit", aliases=["units", "c", "convert", "u"])
async def convert_units(command: str, message: discord.Message):
	parts = command.split(" ")

	if len(parts) == 1:
		# no args
		await message.channel.send(f"Need more arguments to run command. See command help for help.")
		return
	if len(parts) == 2:
		parts += [""]

	src_unit = parts[1]
	dst_unit = parts[2]
	proc = subprocess.Popen(["units", "-t", src_unit, dst_unit], stdout=subprocess.PIPE)

	await asyncio.sleep(0.25)  # Instead of blocking on a timeout we'll just sleep() and use an instantaneous timeout
	stdout, stderr = proc.communicate(timeout=10**-6)
	await message.channel.send(stdout.decode())
	return

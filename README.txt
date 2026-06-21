================================================================================
                    SPOTIFY PLAYLIST TO FLAC DOWNLOADER
                          Step-by-Step Guide
================================================================================

WHAT THIS DOES:
---------------
Downloads Spotify playlists and converts them to FLAC audio files
for offline listening on your PC.


================================================================================
                        TABLE OF CONTENTS
================================================================================

1.  REQUIREMENTS
2.  INSTALL PYTHON
3.  INSTALL FFMPEG
4.  INSTALL SPOTDL
5.  DOWNLOAD THE SCRIPT
6.  GET YOUR SPOTIFY COOKIE
7.  RUN SETUP
8.  DOWNLOAD A PLAYLIST
9.  FIND YOUR FILES
10. COMMON ERRORS & FIXES
11. TIPS & TRICKS


================================================================================
1.  REQUIREMENTS
================================================================================

Before you start, you need:

  - Windows, macOS, or Linux PC
  - Spotify Premium account (for best quality)
  - Internet connection
  - About 10 minutes for setup


================================================================================
2.  INSTALL PYTHON
================================================================================

WINDOWS:
  1. Open your web browser
  2. Go to: https://www.python.org/downloads/
  3. Click the yellow "Download Python" button
  4. Run the downloaded file (python-3.x.x-amd64.exe)
  5. CHECK THE BOX that says "Add Python to PATH" (bottom)
  6. Click "Install Now"
  7. Wait for installation to finish
  8. Restart your computer

MAC:
  1. Open Terminal (press Cmd+Space, type "Terminal")
  2. Type: brew install python3
  3. Press Enter
  4. Wait for installation to finish

LINUX (Ubuntu/Debian):
  1. Open Terminal
  2. Type: sudo apt update
  3. Press Enter
  4. Type: sudo apt install python3 python3-pip
  5. Press Enter
  6. Wait for installation to finish

VERIFY PYTHON IS INSTALLED:
  1. Open Terminal/Command Prompt
  2. Type: python --version
  3. You should see: Python 3.x.x
  4. If you see "Python not found", restart your computer and try again


================================================================================
3.  INSTALL FFMPEG
================================================================================

FFmpeg is required to convert audio to FLAC format.

WINDOWS:
  Option A (Recommended):
    1. Open Terminal/Command Prompt as Administrator
    2. Type: winget install ffmpeg
    3. Press Enter
    4. Wait for installation to finish

  Option B (Manual):
    1. Go to: https://ffmpeg.org/download.html
    2. Click "Windows"
    3. Click "Windows builds from gyan.dev"
    4. Download "ffmpeg-release-full.7z"
    5. Extract the zip file to C:\ffmpeg
    6. Press Windows + X, click "System"
    7. Click "Advanced system settings"
    8. Click "Environment Variables"
    9. Under "System variables", find "Path"
    10. Click "Edit"
    11. Click "New"
    12. Add: C:\ffmpeg\bin
    13. Click "OK" on all windows
    14. Restart your computer

MAC:
  1. Open Terminal
  2. Type: brew install ffmpeg
  3. Press Enter

LINUX (Ubuntu/Debian):
  1. Open Terminal
  2. Type: sudo apt install ffmpeg
  3. Press Enter

VERIFY FFMPEG IS INSTALLED:
  1. Open Terminal/Command Prompt
  2. Type: ffmpeg -version
  3. You should see version information


================================================================================
4.  INSTALL SPOTDL
================================================================================

spotdl is the tool that actually downloads the music.

  1. Open Terminal/Command Prompt
  2. Type: pip install spotdl
  3. Press Enter
  4. Wait for installation to finish (about 1-2 minutes)
  5. You should see "Successfully installed spotdl"

VERIFY SPOTDL IS INSTALLED:
  1. Type: spotdl --version
  2. You should see a version number


================================================================================
5.  DOWNLOAD THE SCRIPT
================================================================================

  1. Download ALL files from this GitHub repository
  2. Extract them to a folder on your computer
  3. Remember the folder location (example: C:\Users\YourName\Music\SPOTIFLAC)
  
  The folder should contain:
    - spotify_flac.py    (the main script)
    - README.txt         (this file)
    - requirements.txt   (dependencies list)


================================================================================
6.  GET YOUR SPOTIFY COOKIE
================================================================================

You need a "cookie" from Spotify to authenticate. Here's how:

  1. Open GOOGLE CHROME (must be Chrome)
  2. Go to: https://open.spotify.com
  3. LOG IN to your Spotify account
  4. Press F12 on your keyboard (Developer Tools opens)
  5. Look at the top tabs: Elements, Console, Sources, Network, etc.
  6. Click ">>" (double arrows) to see more tabs
  7. Click "Application"
  8. On the left sidebar, find "Cookies"
  9. Click the arrow next to Cookies to expand it
  10. Click on "https://open.spotify.com"
  11. You'll see a table with columns: Name, Value, Domain, etc.
  12. Find the row where Name is "sp_dc"
  13. Double-click the Value column for "sp_dc"
  14. The value will highlight (it's a long string of letters/numbers)
  15. Press Ctrl+C to copy it
  16. SAVE THIS VALUE somewhere safe - you'll need it for setup

  The cookie value looks something like:
  AQAAABcdefghijklmnopqrstuvwxyz1234567890...

  NOTE: Keep this cookie PRIVATE. Anyone with it can access your Spotify account.


================================================================================
7.  RUN SETUP
================================================================================

  1. Open Terminal/Command Prompt
  2. Navigate to your script folder:
     Type: cd C:\Users\YourName\Music\SPOTIFLAC
     (Replace with your actual folder path)
  3. Type: python spotify_flac.py --setup
  4. Press Enter
  5. When prompted, PASTE your sp_dc cookie (Ctrl+V)
  6. Press Enter
  7. You should see: "Setup complete!"

  You only need to do this ONCE. The cookie lasts for several months.


================================================================================
8.  DOWNLOAD A PLAYLIST
================================================================================

HOW TO GET A SPOTIFY PLAYLIST URL:
  1. Open Spotify (desktop or web)
  2. Go to any playlist you want to download
  3. Click the THREE DOTS (...) near the play button
  4. Click "Share"
  5. Click "Copy link to playlist"
  6. The URL is now copied to your clipboard

TO DOWNLOAD:
  1. Open Terminal/Command Prompt
  2. Navigate to your script folder:
     cd C:\Users\YourName\Music\SPOTIFLAC
  3. Type: python spotify_flac.py "PASTE_YOUR_PLAYLIST_URL_HERE"
  4. Press Enter
  5. Wait for download to complete

  Example command:
  python spotify_flac.py "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"

  WHAT YOU'LL SEE:
  - "Found X songs in Playlist Name"
  - Each song downloading one by one
  - Progress indicators
  - "Download complete!" when finished

  DOWNLOAD TIME:
  - Small playlist (10 songs): ~2-5 minutes
  - Medium playlist (50 songs): ~15-30 minutes
  - Large playlist (100+ songs): ~30-60 minutes

  IF DOWNLOAD IS INTERRUPTED:
  - Just run the EXACT same command again
  - Already downloaded songs will be SKIPPED
  - Only missing songs will download


================================================================================
9.  FIND YOUR FILES
================================================================================

Your FLAC files are saved in the "downloads" folder inside your script folder:

  Example: C:\Users\YourName\Music\SPOTIFLAC\downloads\

  Each file is named: Artist - Song Title.flac

  FILE SIZE:
  - FLAC files are HIGH QUALITY (lossless audio)
  - Each song is typically 20-50 MB
  - A 100-song playlist will be about 3-5 GB

  TO PLAY YOUR FILES:
  - Double-click any .flac file
  - It will play in Windows Media Player, VLC, or your default music player
  - You can transfer them to your phone, USB drive, or any music player


================================================================================
10. COMMON ERRORS & FIXES
================================================================================

ERROR: "Python not found"
  FIX: 
  - Restart your computer
  - Reinstall Python and make sure "Add Python to PATH" is checked
  - Try using "python3" instead of "python"

ERROR: "pip not found"
  FIX:
  - Type: python -m pip install spotdl
  - Or reinstall Python with PATH option checked

ERROR: "FFmpeg not found"
  FIX:
  - Install FFmpeg (see Section 3)
  - Make sure it's in your PATH
  - Restart your computer after installing

ERROR: "Cookie file error" or "Netscape format"
  FIX:
  - Run setup again: python spotify_flac.py --setup
  - Make sure you're copying the correct sp_dc value
  - The cookie should be a long string (100+ characters)

ERROR: "Rate limited by YouTube"
  FIX:
  - You're downloading too fast
  - Stop the download (Ctrl+C)
  - Wait 1 hour
  - Use the --threads 1 option (edit the script)

ERROR: "No results found for song"
  FIX:
  - The song isn't available on YouTube
  - Common with classical music and rare tracks
  - The script will skip it and continue
  - No fix available - song simply can't be found

ERROR: "Video unavailable"
  FIX:
  - YouTube blocked the request
  - Wait 1 hour before trying again
  - Use slower download settings

ERROR: "LookupError"
  FIX:
  - The song can't be matched on YouTube
  - Especially common with classical music
  - Script will skip and continue automatically


================================================================================
11. TIPS & TRICKS
================================================================================

DOWNLOAD OVERNIGHT:
  - For large playlists, start the download before bed
  - It will finish by morning
  - Interrupted downloads can be resumed

MULTIPLE PLAYLISTS:
  - Download one playlist at a time
  - Wait for each to finish before starting the next
  - This avoids YouTube rate limiting

COOKIE EXPIRATION:
  - Cookies expire every few months
  - If downloads suddenly stop working, run setup again
  - Get a fresh cookie from Chrome

FILE ORGANIZATION:
  - Create separate folders for different playlists
  - Rename the "downloads" folder after each playlist
  - Example: downloads_jazz, downloads_rock, etc.

UPDATE THE TOOL:
  - Occasionally update spotdl: pip install --upgrade spotdl
  - Check this GitHub repository for script updates

SPOTIFY PREMIUM:
  - Premium account gives better quality downloads
  - Free accounts may have lower quality or restrictions

LEGAL NOTE:
  - Only download music you have the right to download
  - For personal use only
  - Do not distribute downloaded files
  - Respect copyright and Spotify's Terms of Service


================================================================================
                         QUICK REFERENCE CARD
================================================================================

SETUP (First time only):
  python spotify_flac.py --setup

DOWNLOAD A PLAYLIST:
  python spotify_flac.py "PLAYLIST_URL"

GET HELP:
  python spotify_flac.py

CHECK PYTHON:
  python --version

CHECK FFMPEG:
  ffmpeg -version

CHECK SPOTDL:
  spotdl --version

UPDATE SPOTDL:
  pip install --upgrade spotdl


================================================================================
                            NEED HELP?
================================================================================

If you're still having issues:

  1. Read the COMMON ERRORS section above
  2. Make sure you followed ALL steps in order
  3. Try restarting your computer
  4. Check your internet connection
  5. Make sure your Spotify cookie hasn't expired
  6. Open an issue on this GitHub repository


================================================================================
                          DISCLAIMER
================================================================================

This tool is for EDUCATIONAL PURPOSES ONLY.

Downloading copyrighted music without permission may violate:
  - Spotify's Terms of Service
  - Copyright laws in your country
  - YouTube's Terms of Service

Users are responsible for complying with all applicable laws.
The developer is not responsible for misuse of this tool.


================================================================================
                          VERSION HISTORY
================================================================================

Version 1.0.0 - Initial Release
  - Spotify playlist downloading
  - FLAC format conversion
  - Cookie-based authentication
  - Automatic error handling
  - Resume interrupted downloads


================================================================================
                    END OF README - HAPPY DOWNLOADING!
================================================================================
================================================================================
                    SPOTIFY PLAYLIST TO FLAC DOWNLOADER
                          Step-by-Step Guide
                              VERSION 2.0
================================================================================

WHAT THIS DOES:
---------------
Downloads Spotify playlists and converts them to FLAC audio files
for offline listening on your PC.

NEW IN V2.0:
  - Searches YouTube, YouTube Music, AND SoundCloud
  - 3 retry attempts for failed songs
  - Shows more search results (dont-filter-results)
  - Automatically skips already downloaded songs
  - Rate-limit safe (single-threaded downloads)


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
12. ADVANCED FEATURES


================================================================================
1.  REQUIREMENTS
================================================================================

Before you start, you need:

  - Windows, macOS, or Linux PC
  - Spotify Premium account (for best quality)
  - Internet connection
  - About 10 minutes for setup
  - Google Chrome (to get Spotify cookie)


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
  5. If still not found, try: python3 --version


================================================================================
3.  INSTALL FFMPEG
================================================================================

FFmpeg is required to convert audio to FLAC format.

WINDOWS:
  Option A (Recommended - fastest):
    1. Open Terminal/Command Prompt as Administrator
    2. Type: winget install ffmpeg
    3. Press Enter
    4. Wait for installation to finish

  Option B (Manual if winget doesn't work):
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
  3. You should see version information (something like "ffmpeg version 6.x")


================================================================================
4.  INSTALL SPOTDL
================================================================================

spotdl is the tool that actually downloads and converts the music.

  1. Open Terminal/Command Prompt
  2. Type: pip install spotdl
  3. Press Enter
  4. Wait for installation to finish (about 1-2 minutes)
  5. You should see "Successfully installed spotdl"

  If pip doesn't work, try:
    python -m pip install spotdl
    pip3 install spotdl

VERIFY SPOTDL IS INSTALLED:
  1. Type: spotdl --version
  2. You should see a version number

UPDATE SPOTDL (if already installed):
  pip install --upgrade spotdl


================================================================================
5.  DOWNLOAD THE SCRIPT
================================================================================

  1. Download ALL files from this GitHub repository
  2. Extract them to a folder on your computer
  3. Remember the folder location
     (Recommended: C:\Users\YourName\Music\SPOTIFLAC)
  
  The folder should contain:
    - spotify_flac.py    (the main downloader script)
    - README.txt         (this instruction file)
    - requirements.txt   (Python dependencies list)
    - .gitignore         (prevents uploading your cookies)


================================================================================
6.  GET YOUR SPOTIFY COOKIE
================================================================================

You need a "cookie" from Spotify to prove you have an account.
This is like a temporary password that lets the tool access Spotify.

STEP-BY-STEP:

  1. Open GOOGLE CHROME (this must be Chrome, not Edge/Firefox)
  2. Go to: https://open.spotify.com
  3. LOG IN to your Spotify Premium account
  4. Press F12 on your keyboard
     (Developer Tools panel opens at the bottom or side)
  5. Look at the top tabs in Developer Tools:
     Elements | Console | Sources | Network | >>
  6. Click the ">>" (double arrows) to see more tabs
  7. Click "Application" from the expanded list
  8. On the left sidebar, find "Cookies" and click the arrow to expand it
  9. Click on "https://open.spotify.com" under Cookies
  10. You'll see a table with columns: Name | Value | Domain | Path | etc.
  11. Find the row where the Name column says "sp_dc"
  12. Double-click the Value column for "sp_dc"
  13. The entire value will highlight (it's a long random-looking string)
  14. Press Ctrl+C to copy it
  15. SAVE THIS VALUE in a text file temporarily

  The cookie value looks something like:
  AQAAABcdefghijklmnopqrstuvwxyz1234567890ABCDEF...

  IMPORTANT SECURITY NOTES:
  - This cookie is like a password to your Spotify account
  - NEVER share it with anyone
  - NEVER upload it to GitHub or public websites
  - It's stored ONLY on your computer in C:\Users\YourName\.spotdl\
  - The cookie expires after a few months (just get a new one)


================================================================================
7.  RUN SETUP
================================================================================

This saves your cookie so the tool can use it for downloads.

  1. Open Terminal/Command Prompt
  2. Navigate to your script folder:
     cd C:\Users\YourName\Music\SPOTIFLAC
     (Replace with your actual folder path)
  3. Type: python spotify_flac.py --setup
  4. Press Enter
  5. When prompted "Paste your sp_dc cookie:", press Ctrl+V to paste
  6. Press Enter
  7. You should see:
     "Cookie saved!"
     "Setup complete!"

  You only need to do this ONCE.
  The cookie lasts for several months before expiring.
  If downloads stop working suddenly, run setup again with a fresh cookie.


================================================================================
8.  DOWNLOAD A PLAYLIST
================================================================================

HOW TO GET A SPOTIFY PLAYLIST URL:
  1. Open Spotify (desktop app or web player)
  2. Go to any playlist you want to download
  3. Click the THREE DOTS (...) near the play button
  4. Click "Share"
  5. Click "Copy link to playlist"
  6. The URL is now copied to your clipboard

  The URL looks like:
  https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
  (The ?si=... part at the end is optional and can be included)

TO DOWNLOAD:
  1. Open Terminal/Command Prompt
  2. Navigate to your script folder:
     cd C:\Users\YourName\Music\SPOTIFLAC
  3. Type: python spotify_flac.py "PASTE_YOUR_PLAYLIST_URL_HERE"
  4. Press Enter
  5. Wait for download to complete

  Example command:
  python spotify_flac.py "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"

  WHAT YOU'LL SEE DURING DOWNLOAD:
  - "Found X songs in Playlist Name"
  - "DOWNLOADING WITH ALL SOURCES"
  - "Using YouTube + YouTube Music + SoundCloud"
  - Each song being searched and downloaded
  - "Skipping..." for already downloaded songs
  - "Downloading..." for new songs
  - "Download complete!" when finished

  DOWNLOAD TIME (approximate):
  - Small playlist (10 songs):  2-5 minutes
  - Medium playlist (50 songs): 15-30 minutes
  - Large playlist (100+ songs): 30-90 minutes

  The tool uses single-threaded downloads with delays to avoid
  being blocked by YouTube. This means it's slower but more reliable.

  IF DOWNLOAD IS INTERRUPTED (power loss, internet down, Ctrl+C):
  - Just run the EXACT same command again
  - Already downloaded songs will be SKIPPED automatically
  - Only missing songs will download
  - Your existing files are safe and won't be overwritten

  WHAT SONGS MIGHT NOT DOWNLOAD:
  - Classical music with very detailed titles (Mozart, Chopin, etc.)
  - Songs with Korean/Japanese/Chinese titles
  - Very rare or obscure tracks
  - Region-restricted content
  - Songs removed from YouTube
  These will show "LookupError: No results found" and be skipped.


================================================================================
9.  FIND YOUR FILES
================================================================================

Your FLAC files are saved in the "downloads" folder inside your script folder:

  Example path:
  C:\Users\YourName\Music\SPOTIFLAC\downloads\

  Each file is named: Artist - Song Title.flac

  FILE DETAILS:
  - Format: FLAC (Free Lossless Audio Codec)
  - Quality: 320kbps (highest quality)
  - Size per song: 20-50 MB typically
  - 100 songs = approximately 3-5 GB total

  TO PLAY YOUR FILES:
  - Double-click any .flac file to play it
  - Works with: Windows Media Player, VLC Media Player, MusicBee, Foobar2000
  - Can be transferred to: USB drive, external hard drive, Android phone
  - For iPhone: Convert to ALAC first or use VLC app

  TO ORGANIZE BY PLAYLIST:
  - Rename the "downloads" folder after each playlist download
  - Example: downloads -> The Ken-WAY Playlist
  - The next download will create a fresh "downloads" folder


================================================================================
10. COMMON ERRORS & FIXES
================================================================================

ERROR: "Python not found" or "python is not recognized"
  CAUSE: Python is not installed or not in PATH
  FIX:
    1. Restart your computer
    2. Reinstall Python and CHECK "Add Python to PATH"
    3. Try using "python3" instead of "python"
    4. Try using "py" instead of "python"

ERROR: "pip not found" or "pip is not recognized"
  CAUSE: pip is not installed or not in PATH
  FIX:
    - Type: python -m pip install spotdl
    - Or: py -m pip install spotdl
    - Or reinstall Python with PATH option checked

ERROR: "FFmpeg not found"
  CAUSE: FFmpeg is not installed
  FIX:
    - Install FFmpeg (see Section 3 above)
    - Make sure it's in your system PATH
    - Restart your computer after installing

ERROR: "Cookie file error" or "Netscape format cookies"
  CAUSE: Cookie file has wrong format
  FIX:
    - Run setup again: python spotify_flac.py --setup
    - Make sure you're copying the sp_dc value (not sp_t or other cookies)
    - The sp_dc value should be 100+ characters long
    - Delete C:\Users\YourName\.spotdl\cookies.txt and run setup again

ERROR: "Rate limited by YouTube" or "Video unavailable"
  CAUSE: YouTube is blocking you for downloading too fast
  FIX:
    - Stop the download immediately (Ctrl+C)
    - Wait at least 1 hour before trying again
    - The script already uses single-threaded downloads to prevent this
    - If it keeps happening, wait longer between attempts

ERROR: "No results found for song" (LookupError)
  CAUSE: The song can't be found on YouTube/YouTube Music/SoundCloud
  FIX:
    - This is normal for classical music and rare tracks
    - The script automatically skips these and continues
    - No fix available - the song simply isn't on those platforms
    - You can try searching YouTube manually and downloading with yt-dlp

ERROR: "AudioProviderError: YT-DLP download error"
  CAUSE: YouTube download failed for a specific video
  FIX:
    - Usually temporary - run the script again later
    - The video may have been removed from YouTube
    - Try waiting a few hours and retrying

ERROR: "This content isn't available, try again later"
  CAUSE: YouTube rate limit or geo-restriction
  FIX:
    - Wait 1 hour
    - The script will retry up to 3 times automatically
    - If persistent, the content may be blocked in your country


================================================================================
11. TIPS & TRICKS
================================================================================

BEST PRACTICES:

  DOWNLOAD OVERNIGHT:
    - Start large playlists before going to bed
    - They'll finish by morning
    - Interrupted downloads resume automatically

  MULTIPLE PLAYLISTS:
    - Download one playlist at a time
    - Wait for each to finish completely
    - This prevents YouTube rate limiting

  COOKIE MANAGEMENT:
    - Cookies expire every 2-3 months
    - If downloads stop with authentication errors, get a new cookie
    - Run setup again: python spotify_flac.py --setup

  FILE ORGANIZATION:
    - Rename the "downloads" folder after each playlist
    - Example: downloads -> K-Drama OST Collection
    - Create separate folders for different genres

  QUALITY NOTE:
    - Songs download at the highest available quality
    - FLAC is lossless (identical to source)
    - Actual quality depends on YouTube's source audio
    - Most songs will be genuine 320kbps quality

  SPOTIFY PREMIUM:
    - Premium account recommended for best results
    - Free accounts work but may have lower quality sources
    - Some playlists may not be accessible with free accounts

  UPDATING THE TOOL:
    - Update spotdl monthly: pip install --upgrade spotdl
    - Check the GitHub repository for script updates
    - New versions may find more songs

  SUCCESS RATE:
    - Modern/popular music: 90-100% success rate
    - K-pop/J-pop: 60-80% success rate
    - Classical music: 20-40% success rate
    - Rare/obscure tracks: Variable


================================================================================
12. ADVANCED FEATURES
================================================================================

The script searches MULTIPLE sources to maximize downloads:

  AUDIO SOURCES SEARCHED:
    1. YouTube - Largest video library
    2. YouTube Music - Better for Asian music (K-pop, J-pop, C-pop)
    3. SoundCloud - Alternative source for rare tracks

  AUTOMATIC FEATURES:
    - 3 retry attempts for failed downloads
    - Unfiltered search results (finds more matches)
    - Single-threaded (avoids YouTube rate limits)
    - Skips existing files (resume support)
    - Real-time progress display

  TO CHECK WHAT DOWNLOADED:
    Windows:
      dir downloads\*.flac

    macOS/Linux:
      ls downloads/*.flac

  TO COUNT YOUR FILES:
    Windows:
      (dir downloads\*.flac).Count

    macOS/Linux:
      ls downloads/*.flac | wc -l

  TO SEE TOTAL SIZE:
    Windows:
      dir downloads

    macOS/Linux:
      du -sh downloads


================================================================================
                         QUICK REFERENCE CARD
================================================================================

SETUP (first time only, saves your cookie):
  python spotify_flac.py --setup

DOWNLOAD A PLAYLIST (all sources, auto-skip existing):
  python spotify_flac.py "PLAYLIST_URL"

SHOW HELP:
  python spotify_flac.py

CHECK PYTHON VERSION:
  python --version

CHECK FFMPEG VERSION:
  ffmpeg -version

CHECK SPOTDL VERSION:
  spotdl --version

UPDATE SPOTDL:
  pip install --upgrade spotdl

VIEW DOWNLOADED FILES:
  dir downloads\*.flac          (Windows)
  ls downloads/*.flac           (macOS/Linux)

OPEN DOWNLOADS FOLDER:
  explorer downloads            (Windows)
  open downloads                (macOS)
  xdg-open downloads            (Linux)


================================================================================
                            NEED HELP?
================================================================================

STILL HAVING ISSUES? TRY THESE STEPS IN ORDER:

  1. Read the COMMON ERRORS section (Section 10) carefully
  2. Make sure you followed ALL steps in exact order
  3. Restart your computer
  4. Check your internet connection is stable
  5. Verify your Spotify cookie hasn't expired (get a new one)
  6. Make sure spotdl is updated: pip install --upgrade spotdl
  7. Try a different playlist to test if the tool works
  8. Open an issue on this GitHub repository with:
     - Your operating system (Windows 10/11, macOS, Linux)
     - The exact error message
     - What step you were on
     - The playlist URL (if public)


================================================================================
                          LEGAL DISCLAIMER
================================================================================

This tool is for EDUCATIONAL PURPOSES ONLY.

Downloading copyrighted music without permission may violate:
  - Spotify's Terms of Service
  - YouTube's Terms of Service
  - Copyright laws in your country
  - International copyright treaties

Users are solely responsible for:
  - Complying with all applicable laws
  - Obtaining necessary permissions
  - Any consequences of using this tool

The developer:
  - Does not host or distribute copyrighted content
  - Is not responsible for misuse of this tool
  - Does not encourage copyright infringement

By using this tool, you agree that:
  - You will only download content you have rights to
  - You will use downloaded files for personal use only
  - You will not distribute, sell, or share downloaded files
  - You accept full legal responsibility for your actions


================================================================================
                          VERSION HISTORY
================================================================================

Version 2.0 - Major Update
  - Searches YouTube, YouTube Music, AND SoundCloud
  - Added 3 automatic retries for failed downloads
  - Unfiltered search results (finds more songs)
  - Single-threaded downloads (avoids rate limits)
  - Improved error messages and documentation
  - Better handling of already-downloaded files

Version 1.0 - Initial Release
  - Basic Spotify playlist downloading
  - FLAC format conversion
  - Cookie-based authentication
  - Automatic error handling
  - Resume interrupted downloads


================================================================================
                    END OF README - HAPPY DOWNLOADING!
================================================================================

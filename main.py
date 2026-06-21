#!/usr/bin/env python3
"""
Spotify Playlist to FLAC - Slow & Steady (No Rate Limits)
"""

import subprocess
import sys
from pathlib import Path

def setup():
    """Setup Spotify cookies in correct Netscape format"""
    print("\n" + "="*60)
    print("SPOTIFY TO FLAC - SETUP")
    print("="*60)
    
    print("\nHOW TO GET YOUR SPOTIFY COOKIE:")
    print("\n1. Open Chrome and go to: https://open.spotify.com")
    print("2. Log in to your Spotify account")
    print("3. Press F12 > Application > Cookies > open.spotify.com")
    print("4. Find 'sp_dc' and copy its Value")
    
    cookie = input("\nPaste your sp_dc cookie: ").strip()
    
    if cookie:
        config_dir = Path.home() / '.spotdl'
        config_dir.mkdir(exist_ok=True)
        
        cookie_file = config_dir / 'cookies.txt'
        with open(cookie_file, 'w') as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write(".spotify.com\tTRUE\t/\tFALSE\t0\tsp_dc\t" + cookie + "\n")
        
        print(f"\nCookie saved!")
        return True
    return False

def download(playlist_url, output_dir="./downloads"):
    """Download playlist SLOWLY to avoid rate limits"""
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\nDownloading playlist SLOWLY to avoid rate limits...")
    print(f"Saving to: {output_dir}")
    print("This will take longer but won't get blocked\n")
    
    cmd = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube',
        '--threads', '1',           # Download 1 at a time
        '--print-errors'
    ]
    
    try:
        subprocess.run(cmd)
        
        output_path = Path(output_dir)
        flac_files = list(output_path.glob("*.flac"))
        
        print(f"\n{'='*50}")
        print(f"DOWNLOAD COMPLETE!")
        print(f"{'='*50}")
        print(f"Songs downloaded: {len(flac_files)}")
        print(f"Location: {output_path.absolute()}")
        
    except KeyboardInterrupt:
        output_path = Path(output_dir)
        flac_files = list(output_path.glob("*.flac"))
        print(f"\nStopped. {len(flac_files)} songs saved.")

def main():
    if len(sys.argv) < 2:
        print("\nSpotify to FLAC Downloader")
        print("="*40)
        print("\nUSAGE:")
        print("  Setup:    python spotify_flac.py --setup")
        print("  Download: python spotify_flac.py PLAYLIST_URL")
        return
    
    if sys.argv[1] == '--setup':
        setup()
    else:
        download(sys.argv[1])

if __name__ == "__main__":
    main()
    converter.verify_flac_files()

if __name__ == "__main__":
    main()

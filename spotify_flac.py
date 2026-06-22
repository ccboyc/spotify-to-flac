#!/usr/bin/env python3
"""
Spotify Playlist to FLAC - Expanded Search Version
Tries multiple sources and search strategies to find more songs
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
        print("Setup complete!")
        return True
    return False

def download_expanded(playlist_url, output_dir="./downloads"):
    """
    Download playlist with MULTIPLE search strategies to find more songs.
    Runs spotdl 3 times with different audio sources to maximize results.
    """
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\n{'='*60}")
    print("EXPANDED SEARCH MODE")
    print(f"{'='*60}")
    print("Will try 3 different audio sources to find maximum songs:")
    print("  1. YouTube Music (best for K-pop/Asian music)")
    print("  2. YouTube (largest library)")
    print("  3. SoundCloud (alternative source)")
    print(f"\nSaving to: {output_dir}\n")
    
    # Strategy 1: YouTube Music (best for K-pop and Asian music)
    print(f"\n{'='*60}")
    print("PASS 1/3: Searching YouTube Music...")
    print(f"{'='*60}\n")
    
    cmd1 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube-music',
        '--dont-filter-results',      # Show ALL search results
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd1)
    
    # Strategy 2: YouTube (largest video library)
    print(f"\n{'='*60}")
    print("PASS 2/3: Searching YouTube...")
    print(f"{'='*60}\n")
    
    cmd2 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube',
        '--dont-filter-results',      # Show ALL search results
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd2)
    
    # Strategy 3: SoundCloud (alternative source)
    print(f"\n{'='*60}")
    print("PASS 3/3: Searching SoundCloud...")
    print(f"{'='*60}\n")
    
    cmd3 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'soundcloud',
        '--dont-filter-results',
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd3)
    
    # Show final results
    output_path = Path(output_dir)
    flac_files = list(output_path.glob("*.flac"))
    
    print(f"\n{'='*60}")
    print(f"ALL DOWNLOADS COMPLETE!")
    print(f"{'='*60}")
    print(f"Total songs downloaded: {len(flac_files)}")
    print(f"Location: {output_path.absolute()}")
    
    if flac_files:
        total_size = sum(f.stat().st_size for f in flac_files)
        print(f"Total size: {total_size / (1024**3):.2f} GB")
        print(f"\nAll downloaded songs:")
        for f in sorted(flac_files):
            size_mb = f.stat().st_size / (1024*1024)
            print(f"  + {f.stem} ({size_mb:.1f} MB)")

def download_aggressive(playlist_url, output_dir="./downloads"):
    """
    MORE AGGRESSIVE: Use all sources at once and don't filter results.
    This finds the most songs but takes longer.
    """
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\n{'='*60}")
    print("AGGRESSIVE SEARCH MODE")
    print(f"{'='*60}")
    print("Using ALL audio sources simultaneously")
    print("This finds the maximum number of songs!\n")
    
    # ALL sources at once - spotdl will try each
    cmd = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube', 'youtube-music', 'soundcloud',  # ALL sources
        '--dont-filter-results',      # Show ALL possible matches
        '--threads', '1',             # Slow to avoid rate limits
        '--print-errors',
        '--max-retries', '3'          # Retry failed songs 3 times
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        pass
    
    # Show results
    output_path = Path(output_dir)
    flac_files = list(output_path.glob("*.flac"))
    
    print(f"\n{'='*60}")
    print(f"DOWNLOAD COMPLETE!")
    print(f"{'='*60}")
    print(f"Total songs: {len(flac_files)}")
    print(f"Location: {output_path.absolute()}")
    
    if flac_files:
        total_size = sum(f.stat().st_size for f in flac_files)
        print(f"Total size: {total_size / (1024**3):.2f} GB")

def download_playlist(playlist_url, output_dir="./downloads"):
    """
    Download playlist using ALL available sources
    """
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\n{'='*60}")
    print("DOWNLOADING PLAYLIST")
    print(f"{'='*60}")
    print(f"Saving to: {output_dir}")
    print(f"Using ALL audio sources for maximum results")
    print(f"Press Ctrl+C to stop\n")
    
    cmd = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube', 'youtube-music', 'soundcloud',
        '--dont-filter-results',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        pass
    
    # Show results
    output_path = Path(output_dir)
    flac_files = list(output_path.glob("*.flac"))
    
    print(f"\n{'='*60}")
    print(f"DOWNLOAD COMPLETE!")
    print(f"{'='*60}")
    print(f"Songs downloaded: {len(flac_files)}")
    print(f"Location: {output_path.absolute()}")
    
    if flac_files:
        total_size = sum(f.stat().st_size for f in flac_files)
        print(f"Total size: {total_size / (1024**3):.2f} GB")
        print(f"\nFiles:")
        for f in sorted(flac_files)[:20]:
            print(f"  + {f.stem}")
        if len(flac_files) > 20:
            print(f"  ... and {len(flac_files) - 20} more")

def main():
    if len(sys.argv) < 2:
        print("\nSpotify to FLAC Downloader - EXPANDED SEARCH")
        print("="*50)
        print("\nUSAGE:")
        print("  Setup:              python spotify_flac.py --setup")
        print("  Download (normal):  python spotify_flac.py PLAYLIST_URL")
        print("  Download (expanded): python spotify_flac.py --expanded PLAYLIST_URL")
        print("  Download (aggressive): python spotify_flac.py --aggressive PLAYLIST_URL")
        print("\nMODES:")
        print("  normal    - Uses all sources, don't filter results")
        print("  expanded  - Runs 3 passes (YouTube Music, YouTube, SoundCloud)")
        print("  aggressive - All sources, no filtering, retries 3x (SLOWEST but finds most)")
        return
    
    if sys.argv[1] == '--setup':
        setup()
    elif sys.argv[1] == '--expanded':
        if len(sys.argv) < 3:
            print("Please provide a playlist URL")
            return
        download_expanded(sys.argv[2])
    elif sys.argv[1] == '--aggressive':
        if len(sys.argv) < 3:
            print("Please provide a playlist URL")
            return
        download_aggressive(sys.argv[2])
    else:
        download_playlist(sys.argv[1])

if __name__ == "__main__":
    main()

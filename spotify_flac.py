#!/usr/bin/env python3
"""
Spotify Playlist to FLAC - ALL SOURCES VERSION
Uses every available audio platform for maximum coverage
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

def download_all_sources(playlist_url, output_dir="./downloads"):
    """
    Download using EVERY available audio source.
    5 separate passes to maximize coverage and quality.
    """
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\n{'='*60}")
    print("ALL-SOURCE DOWNLOAD - 5 PASSES")
    print(f"{'='*60}")
    print(f"Saving to: {output_dir}")
    print("Using EVERY available platform:\n")
    print("  Pass 1: YouTube Music    (official audio, best quality)")
    print("  Pass 2: Bandcamp         (artist uploads, 320kbps)")
    print("  Pass 3: SoundCloud       (indie artists, remixes)")
    print("  Pass 4: Piped            (YouTube mirror, privacy)")
    print("  Pass 5: YouTube          (largest library, last resort)")
    print("\n")

    # Pass 1: YouTube Music (BEST quality, official audio)
    print(f"{'='*60}")
    print("PASS 1/5: YouTube Music (Official Audio)")
    print(f"{'='*60}\n")
    
    cmd1 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube-music',
        '--only-verified-results',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd1)
    
    # Pass 2: Bandcamp (artist direct uploads)
    print(f"\n{'='*60}")
    print("PASS 2/5: Bandcamp (Artist Uploads)")
    print(f"{'='*60}\n")
    
    cmd2 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'bandcamp',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd2)
    
    # Pass 3: SoundCloud (indie, remixes, rare tracks)
    print(f"\n{'='*60}")
    print("PASS 3/5: SoundCloud (Indie & Remixes)")
    print(f"{'='*60}\n")
    
    cmd3 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'soundcloud',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd3)
    
    # Pass 4: Piped (YouTube mirror, privacy-focused)
    print(f"\n{'='*60}")
    print("PASS 4/5: Piped (YouTube Mirror)")
    print(f"{'='*60}\n")
    
    cmd4 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'piped',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    subprocess.run(cmd4)
    
    # Pass 5: YouTube (largest library, last resort)
    print(f"\n{'='*60}")
    print("PASS 5/5: YouTube (Largest Library)")
    print(f"{'='*60}\n")
    
    cmd5 = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube',
        '--only-verified-results',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors',
        # Quality filters for YouTube pass:
        '--yt-dlp-args', '--match-filter', 'title!*=-live',
        '--yt-dlp-args', '--match-filter', 'title!*=-reaction',
        '--yt-dlp-args', '--match-filter', 'duration > 120',
    ]
    subprocess.run(cmd5)
    
    # Final results
    output_path = Path(output_dir)
    flac_files = list(output_path.glob("*.flac"))
    
    print(f"\n{'='*60}")
    print(f"ALL 5 PASSES COMPLETE!")
    print(f"{'='*60}")
    print(f"Total songs downloaded: {len(flac_files)}")
    print(f"Location: {output_path.absolute()}")
    
    if flac_files:
        total_size = sum(f.stat().st_size for f in flac_files)
        print(f"Total size: {total_size / (1024**3):.2f} GB")
        print(f"\nComplete song list:")
        for i, f in enumerate(sorted(flac_files), 1):
            size_mb = f.stat().st_size / (1024*1024)
            print(f"  {i:3d}. {f.stem} ({size_mb:.1f} MB)")

def download_fast_all(playlist_url, output_dir="./downloads"):
    """
    Download using ALL sources in ONE pass (faster but less coverage).
    """
    cookie_file = Path.home() / '.spotdl' / 'cookies.txt'
    
    if not cookie_file.exists():
        print("\nNo cookies found!")
        print("Run setup first: python spotify_flac.py --setup")
        return
    
    print(f"\n{'='*60}")
    print("ALL SOURCES - SINGLE PASS")
    print(f"{'='*60}")
    print(f"Saving to: {output_dir}")
    print("Using: YouTube Music + Bandcamp + SoundCloud + Piped + YouTube\n")
    
    cmd = [
        'spotdl', 'download',
        playlist_url,
        '--output', output_dir,
        '--format', 'flac',
        '--bitrate', '320k',
        '--cookie-file', str(cookie_file),
        '--audio', 'youtube-music', 'bandcamp', 'soundcloud', 'piped', 'youtube',
        '--only-verified-results',
        '--dont-filter-results',
        '--max-retries', '3',
        '--threads', '1',
        '--print-errors'
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nStopped by user")
    
    output_path = Path(output_dir)
    flac_files = list(output_path.glob("*.flac"))
    
    print(f"\n{'='*60}")
    print(f"DOWNLOAD COMPLETE!")
    print(f"{'='*60}")
    print(f"Songs downloaded: {len(flac_files)}")
    print(f"Location: {output_path.absolute()}")

def main():
    if len(sys.argv) < 2:
        print("\n" + "="*60)
        print("SPOTIFY TO FLAC - ALL SOURCES DOWNLOADER")
        print("="*60)
        print("\nMODES:")
        print("  5-Pass Mode (MAXIMUM coverage, slower):")
        print("    python spotify_flac.py PLAYLIST_URL")
        print("    Runs 5 separate passes on every platform")
        print("    Best for: classical, K-pop, rare music")
        print("\n  Fast Mode (all sources at once):")
        print("    python spotify_flac.py --fast PLAYLIST_URL")
        print("    Single pass with all sources")
        print("    Best for: popular music, modern playlists")
        print("\n  Setup:")
        print("    python spotify_flac.py --setup")
        print("\n  SOURCES USED:")
        print("    YouTube Music | Bandcamp | SoundCloud | Piped | YouTube")
        return
    
    if sys.argv[1] == '--setup':
        setup()
    elif sys.argv[1] == '--fast':
        if len(sys.argv) < 3:
            print("Please provide a playlist URL")
            return
        download_fast_all(sys.argv[2])
    else:
        download_all_sources(sys.argv[1])

if __name__ == "__main__":
    main()

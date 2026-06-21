#!/usr/bin/env python3
"""
Spotify Playlist to FLAC Downloader
Downloads Spotify playlists and converts them to FLAC format
"""

import os
import subprocess
import sys
import json
from pathlib import Path
import argparse
from typing import Optional

class SpotifyToFlac:
    def __init__(self, output_dir: str = "./downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        dependencies = {
            'spotdl': 'spotdl',
            'ffmpeg': 'ffmpeg'
        }
        
        missing = []
        for name, cmd in dependencies.items():
            if not self._command_exists(cmd):
                missing.append(name)
        
        if missing:
            print(f"Missing dependencies: {', '.join(missing)}")
            print("\nPlease install them using:")
            print("pip install spotdl")
            print("And install ffmpeg from: https://ffmpeg.org/download.html")
            return False
        return True
    
    def _command_exists(self, cmd: str) -> bool:
        """Check if a command exists in PATH"""
        try:
            subprocess.run([cmd, '--version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def download_playlist(self, playlist_url: str, bitrate: str = "320k"):
        """
        Download playlist using spotdl
        
        Args:
            playlist_url: Spotify playlist URL
            bitrate: Audio bitrate (not used for FLAC, but spotdl needs it)
        """
        print(f"Downloading playlist: {playlist_url}")
        print(f"Output directory: {self.output_dir}")
        print("This may take a while depending on playlist size...")
        
        try:
            # Use spotdl to download the playlist
            cmd = [
                'spotdl',
                'download',
                playlist_url,
                '--output',
                str(self.output_dir),
                '--format',
                'flac',
                '--bitrate',
                '320k'
            ]
            
            subprocess.run(cmd, check=True)
            print("✓ Download completed successfully!")
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Error downloading playlist: {e}")
            sys.exit(1)
    
    def verify_flac_files(self):
        """Verify that downloaded files are in FLAC format"""
        flac_files = list(self.output_dir.glob("*.flac"))
        
        if not flac_files:
            print("⚠ No FLAC files found in output directory")
            return
        
        print(f"\n✓ Found {len(flac_files)} FLAC files:")
        for file in flac_files:
            size_mb = file.stat().st_size / (1024 * 1024)
            print(f"  - {file.name} ({size_mb:.1f} MB)")

def setup_spotdl():
    """First-time setup for spotdl"""
    print("Setting up spotdl for first use...")
    print("You'll need to provide Spotify API credentials.")
    print("\nFollow these steps:")
    print("1. Go to https://developer.spotify.com/dashboard")
    print("2. Create a new application")
    print("3. Get your Client ID and Client Secret")
    
    client_id = input("\nEnter your Spotify Client ID: ").strip()
    client_secret = input("Enter your Spotify Client Secret: ").strip()
    
    try:
        # Set up spotdl with credentials
        subprocess.run([
            'spotdl',
            '--client-id', client_id,
            '--client-secret', client_secret
        ], check=True)
        
        # Save credentials to config file
        config_dir = Path.home() / '.spotdl'
        config_dir.mkdir(exist_ok=True)
        
        config = {
            'client_id': client_id,
            'client_secret': client_secret,
            'format': 'flac',
            'bitrate': '320k'
        }
        
        with open(config_dir / 'config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("✓ Setup completed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Setup failed: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Download Spotify playlists and convert to FLAC',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
  %(prog)s --setup
  %(prog)s --output ./my_music playlist_url
        """
    )
    
    parser.add_argument(
        'playlist_url',
        nargs='?',
        help='Spotify playlist URL'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='./downloads',
        help='Output directory (default: ./downloads)'
    )
    
    parser.add_argument(
        '--setup',
        action='store_true',
        help='Run first-time setup'
    )
    
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Verify FLAC files in output directory'
    )
    
    args = parser.parse_args()
    
    # Initialize converter
    converter = SpotifyToFlac(args.output)
    
    # Handle setup
    if args.setup:
        setup_spotdl()
        return
    
    # Handle verification only
    if args.verify:
        if not args.playlist_url:
            converter.verify_flac_files()
            return
    
    # Check if playlist URL is provided
    if not args.playlist_url:
        parser.print_help()
        print("\n✗ Error: Playlist URL is required")
        sys.exit(1)
    
    # Check dependencies
    if not converter.check_dependencies():
        sys.exit(1)
    
    # Download playlist
    converter.download_playlist(args.playlist_url)
    converter.verify_flac_files()

if __name__ == "__main__":
    main()
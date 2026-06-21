#!/bin/bash
# Installation script for Spotify to FLAC downloader

echo "Installing Spotify to FLAC Downloader Dependencies..."
echo "======================================================"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

echo "✓ Python 3 found"

# Install spotdl
echo "Installing spotdl..."
pip3 install spotdl --upgrade

# Check and install FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠ FFmpeg not found"
    echo ""
    echo "Please install FFmpeg manually:"
    echo "  macOS:   brew install ffmpeg"
    echo "  Ubuntu:  sudo apt-get install ffmpeg"
    echo "  Windows: Download from https://ffmpeg.org/download.html"
    echo ""
    echo "Or visit: https://ffmpeg.org/download.html"
else
    echo "✓ FFmpeg found"
fi

echo ""
echo "✓ Installation complete!"
echo ""
echo "To set up Spotify API credentials, run:"
echo "python3 spotify_to_flac.py --setup"
echo ""
echo "To download a playlist:"
echo "python3 spotify_to_flac.py 'https://open.spotify.com/playlist/PLAYLIST_ID'"
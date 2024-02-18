# get_cover_art

### THE PROBLEM
Missing cover art for large imported music libraries.  

### EXISTING SOLUTIONS

1. Apple's Music App (and its predecessor iTunes) has a "Get Album Artwork" feature, but it isn't reliable and doesn't actually embed cover art into your audio files.  That means if you move your music library elsewhere, you'll be missing all your album artwork.

2. Metadata utilities like Metadatics are great (and cheap if not free), but they can require a lot of manual interaction to go through each album and select artwork from search results.  This can be forbidding for large libraries of thousands of albums.

### THIS SOLUTION
This Python package will batch-update your entire library without manual interaction for each album.

It uses Apple Music's artwork, which is already standardized and high-quality.  It also embeds the artwork directly into your audio files, so that it's independent of your player.

## Supported formats (so far)
- MP3
- MP4 (.m4a, .m4b)
- FLAC
- DSF
- Ogg Vorbis
- Opus
- WAV*

(* NOTE: Apple Music and other players may not recognize ID3 tags on WAV files.)

## Setup

### Requirements
- Python 3.5 or greater
- Python packages: [mutagen](https://pypi.org/project/mutagen/)
  - automatically installed if you use `pip install` below

### Installation

You can download this repository from GitHub, or grab it from [PyPI](https://pypi.org/project/get-cover-art/) using pip:

```
$ pip install get_cover_art
```

To upgrade existing installations:
```
$ pip install --upgrade get_cover_art
```

## Usage

### From the Command Line
```
[python -m] get_cover_art [--path=<path_to_audio_file_or_folder>] [--options]

  --path PATH           audio file, or folder of audio files (recursive)

artwork options:
  --art-size ART_SIZE   square dimensions of artwork (default: 500)
  --art-quality ART_QUALITY
                        jpeg compression quality (1-100, default: auto)
  --art-dest DEST       set artwork destination folder
  --art-dest-inline     set artwork destination folder to same folders as audio files
  --art-dest-filename ART_DEST_FILENAME
                        set artwork destination filename format. Accepts
                        {artist}, {album}, {album_or_title}, {filename}, and
                        {title}. Default is '{artist} - {album_or_title}.jpg'
  --external-art-mode {before,after,none}
                        Use images from local disk: "before" prevents
                        downloads, "after" downloads as a fallback. Default is none.
  --external-art-filename EXTERNAL_ART_FILENAME [EXTERNAL_ART_FILENAME ...]
                        Filename(s) of folder art to use. Accepts {artist},
                        {album}, and {title} for replacement: e.g. cover.jpg
                        or {album}-{artist}.jpg ; this does not affect the filename
                        for art that must be fetched (use --art-dest-filename for
                        that).

behavior options:
  --test, --no-embed    scan and download only, don't embed artwork
  --no-download         embed only previously-downloaded artwork
  --clear               clear artwork from audio file (regardless of finding art)
  --cleanup             remove downloaded artwork files afterward
  --force               process files regardless of existing artwork
  --verbose             print verbose logging
  --no-skip             don't skip previously-scanned files
  --throttle THROTTLE   number of seconds to wait if request is rejected

filter options:
  --skip-artwork SKIP_ARTWORK
                        (maintained between runs) file listing destination art files to skip
  --skip-artists SKIP_ARTISTS
                        file listing artists to skip
  --skip-albums SKIP_ALBUMS
                        file listing albums to skip
```
if you omit `path`, it will scan the current working directory

_Pro Tip:_ You can run with `--test` first, then browse/prune the downloaded artwork, then run again with `--no-download` to embed only the artwork you didn't prune.

### From the Python Environment
```python
from get_cover_art import CoverFinder

finder = CoverFinder(OPTIONS)

# then you can run either of these:
finder.scan_folder(PATH_TO_AUDIO_LIBRARY)
finder.scan_file(PATH_TO_AUDIO_FILE)
```

- `OPTIONS` is a dict of the same options listed for the commandline, e.g. `--verbose` -> `{'verbose': True}`
- you can omit `PATH_TO_AUDIO_LIBRARY` to default to your current directory
- your `CoverFinder` object keeps a list of files_processed, files_skipped, files_failed, files_invalid

## How it works
1. First, it recursively scans your provided folder for supported files.
  - Step 1 is skipped if you specified a single file instead of a folder.
2. For each file without embedded artwork (or all files if `--force` is used), attempts to download from Apple Music based on artist and album metadata.
  - Step 2 is skipped if it had already downloaded (or attempted to download) the image file.
    - This works by caching a list of previously downloaded/attempted artwork (using `skip_artwork.txt`)
    - You can ignore the cached list by using `--no-skip`
  - Step 2 is also skipped based on `--no-download` or other `--skip-*` options.
3. If artwork is found, it's embedded into the audio file.

### Why do you download from Apple Music and not Google image search?
1. Google's Image Search API requires a dev token (so does Apple Music's API, but not its public web query URL).
2. Google search queries are heavily throttled.
3. Apple Music's cover sizes are standardized and sufficiently large.

### Using external art sources

The external-art options allow you to fall back on local folder art.
Some other scraping systems may have created cover art: for instance, some
Kodi scrapers create a "cover.jpg" image in each album directory.

Specifying "--external-art-mode before" will use these existing images, and only
download images if there is no existing image. Specifying "--external-art-mode
after" will attempt to download artwork as usual, only falling back on the
existing images if the download is unable to locate new art.

The "--external-art-filename" option allows you to specify the filename(s) to use
for this existing folder art. It defaults to "cover.jpg \_albumcover.jpg folder.jpg", which are 3 filenames commonly used by other scraping programs. You
can also use bracket formatting with the artist, album, and title fields:
for instance, --external-art-filename "{artist}-{album}-cover.jpg" would create
filenames such as "The Beatles-Abbey Road-cover.jpg".

The "--art-dest-filename" option allows you to specify the filename used to
store downloaded files, for interoperability with other systems. You __must__
be careful to avoid collisions between different albums: The default is
"{artist} - {album_or_title}.jpg". If you know that all of the albums you're running
against have their own directories _and_ you are using "--art-dest-inline", then you
could use something more generic (such as "cover.jpg").  A note about the format:
- {album_or_title} falls back on the title tag if the album tag is blank
- {filename} uses the filename of the source audio file (minus the extension)

_Pro Tip:_ If you have a cover.jpg in each album directory, you can use:
"--external-art-mode before --external-art-filename cover.jpg --art-dest-inline"
and the local images will be used when present (avoiding network lookups).
You could also specify "--art-dest-filename cover.jpg" if you want to store the
newly downloaded covers in a similar location (again, this is only sane
in combination with --art-dest-inline, in cases where each album is stored in 
a separate directory).

## Troubleshooting

### The artwork is embedded now, but Apple's Music App still won't show it.
Try re-importing one of your embedded files.  If the re-imported version shows artwork, you need to reimport your music library.  You can do this without losing your playlists as follows:
1. File->Library->Export Library... and name your exported library file.
2. Visit Music->Preferences...->Files and screenshot your options.  You'll need to restore them later.
3. Quit the app and relaunch while holding down the Option key.
4. Choose "Create Library..." and pick a new location.
5. Visit Music->Preferences...->Files and restore your desired options.
6. File->Library->Import Playlist... and choose your library file from step 1.  (Yes, it's called "Import Playlist..." but you actually use this to import your library.)

Step 6 will take a while.

### The artwork appears in Apple's Music App but not my iOS device.
You'll have to unsync all your music and re-sync it again.  Try it with a single file first.

""" Music Search
    Created by Dane (Sara) Wright
    03/24/2024

    Made with the intent of tracking down which Artists/Albums/Songs from my collection of Music has broken metadata"""

import fnmatch
import os
import time
from tinytag import TinyTag


def find_music(search_location):
    """ Searches for Music in the default Windows location, with folder/file structure similar to:
        root directory:     C:\\Users\\<username>\\Music
        inner directories:  ArtistName1\\
                            ArtistName1\\Album1
                            ArtistName1\\Album2
                            ArtistName1\\Album2\\song1.m4a

        Outputs metadata to a .csv file that is delimited with the TAB character """

    accepted_filetypes = ["*.flac", "*.mp3", "*.m4a", "*.wav", "*.wma"]
    last_album = None

    with open("music.csv", "w") as csv_file:
        # Adding heading; Separating by Tab character because some songs have other separators in them
        csv_file.write(
            "Filename\tTrackNum\tTitle\tArtist\tAlbum\tGenre\tYear\tComposer\tFilesize(MB)\tDuration\tFileExt\n"
        )

        # Going through specified Music directory, looking for Music files and getting the Metadata
        for root, dirs, files in os.walk(search_location):

            for filetype in accepted_filetypes:
                for file in fnmatch.filter(files, filetype):
                    location = os.path.join(root, file)

                    try:
                        # Getting metadata attributes
                        metadata = TinyTag.get(location)

                        if metadata.album != last_album:
                            # Printing the directory for each album
                            csv_file.write("\t\t\t" + root + "\n")

                            last_album = metadata.album

                        # Making duration attr easier to read
                        duration = metadata.duration
                        convert_duration = time.strftime("%H:%M:%S", time.gmtime(duration))

                        # Converting filesize attr to MB
                        filesize = metadata.filesize
                        convert_filesize = round(((filesize / 1024) / 1024), 1)

                        # Getting the file extension
                        split_filetype = filetype.split(".")
                        clean_filetype = split_filetype[-1]

                        csv_file.write(
                            "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                                file,
                                metadata.track,
                                metadata.title,
                                metadata.artist,
                                metadata.album,
                                metadata.genre,
                                metadata.year,
                                metadata.composer,
                                convert_filesize,
                                convert_duration,
                                clean_filetype,
                            )
                        )

                    except Exception as e:
                        print("Error in getting metadata for music file.")


if __name__ == "__main__":
    starting_directory = input("Enter the Directory to Search for Music Metadata: ")

    if os.path.exists(starting_directory):
        find_music(starting_directory)

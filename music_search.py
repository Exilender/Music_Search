""" Music Search
    Created by Dane (Sara) Wright
    03/24/2024

    Terminal program that searches the default Windows Music directory for Artists, Albums, and Song metadata.
    Made with the intent of tracking down which Artists/Albums/Songs from my collection of Music has broken metadata"""

import fnmatch
import os
import time
from tinytag import TinyTag


def find_music():
    """ Searches for Music in the default Windows location, with folder/file structure of:
        root directory:     C:\\Users\\<username>\\Music
        inner directories:  ArtistName1\\
                            ArtistName1\\Album1
                            ArtistName1\\Album2
                            ArtistName1\\Album2\\song1.m4a

        Outputs metadata to a .csv file that is delimited with the TAB character """
    username = os.environ.get("USERNAME")
    search_location = "C:\\Users\\{}\\Music".format(username)
    accepted_filetypes = ["*.flac", "*.mp3", "*.m4a", "*.wav", "*.wma"]
    found_album_dirs = []

    with open("music.csv", "w") as csv_file:
        # Adding heading; Separating by Tab character because some songs have other separators in them
        csv_file.write(
            "Filename\tTrackNum\tTitle\tArtist\tAlbum\tGenre\tYear\tComposer\tFilesize(MB)\tDuration\tFileType\n"
        )

        remove_search_location = search_location.split("\\")

        for root, dir, files in os.walk(search_location):
            root_split = root.split("\\")
            for file in files:

                file_location = root + "\\" + file
                clean_location = root_split[-2] + "\\" + root_split[-1]

                # This If block is trying to avoid 'User\Music' being first element in list/csv
                if (
                    (root_split[-2] and root_split[-1])
                    != (remove_search_location[-2] and remove_search_location[-1])
                ) and (clean_location not in found_album_dirs):

                    found_album_dirs.append(clean_location)

                    csv_file.write("\t\t\t" + clean_location + "\n")

                for filetype in accepted_filetypes:
                    # setting filetype attribute
                    split_filetype = filetype.split(".")
                    clean_filetype = split_filetype[-1]

                    if fnmatch.fnmatch(file, filetype):
                        # getting metadata attributes
                        metadata = TinyTag.get(file_location)

                        # making duration attr easier to read
                        duration = metadata.duration
                        convert_duration = time.strftime(
                            "%H:%M:%S", time.gmtime(duration)
                        )

                        # converting filesize attr to MB
                        filesize = metadata.filesize
                        convert_filesize = round(((filesize / 1024) / 1024), 1)

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


if __name__ == "__main__":
    find_music()

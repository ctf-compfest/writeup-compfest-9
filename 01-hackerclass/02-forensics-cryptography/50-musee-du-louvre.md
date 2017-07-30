Musee du Louvre (50)
====================

## Description

![musee-du-louvre.png](https://ctf-class.compfest.web.id/files/baee1faaab980ff46b6c6d29cacc674f/musee-du-louvre.jpg)

## Write Up
If we open it with Hex Editor, we will see that it is a JPEG file, so it should start with the hex `FF D8` and end with `FF D9` (see [JPEG File format structure](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)). But we see the file end with the ascii `IEND` which maps to a PNG file.

If we search for the hex `FF D9` we will see that it is appended with `0x89` and then `PWN`, while for a PNG file it should be `0x89` and `PNG`, so if we just change it to `PNG` and then copy the remaining to a new file, we will see the image showing the flag: `COMPFEST9{dont_trust_the_end}`

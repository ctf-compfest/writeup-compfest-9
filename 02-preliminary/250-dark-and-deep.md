Dark and Deep (250)
=============

## Description
[https://www.dropbox.com/s/iqe6egt23iffsy9/darkdeep.tar?dl=0](https://www.dropbox.com/s/iqe6egt23iffsy9/darkdeep.tar?dl=0)

## Write up

1. `tar -tvf darkdeep.tar` outputs `.dockerenv` and bunch of alpine filesystem
2. `docker import darkdeep.tar compfest9/darkdeep`
3. `docker run -it compfest9/darkdeep sh --name darkdeep`
4. `find / -type d \( -path /sys -o -path /proc \) -prune -o -type f -exec stat -c "%y %n" {} + | sort -r | head`
5. `docker cp darkdeep:/tmp/.broken.zip broken.zip`
6. fix broken zip ([reference][1]):
    - corrects local file header -> filename length (offset 0x1A)
    - missing end of central directory -> `jar xvf broken.zip`
7. extract: indexed png (color type 3, [reference](2))
    - analyze: all 0 palette
    - fill with some different colors
8. get the flag: `COMPFEST9{how_can_you_digging_this_deep}`

![Solved Image](https://s28.postimg.org/7zlem83el/darkdeep-solved.png)

[1]: https://en.wikipedia.org/wiki/ZIP_(file_format)
[2]: https://en.wikipedia.org/wiki/Portable_Network_Graphics

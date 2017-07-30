Can You Get The Image? (75)
===========================

## Description

[flag.png](https://ctf-class.compfest.web.id/files/d8600c539f8e732f0f3d0d41aa6a51f1/flag.png)

## Write Up
- If we open that image in HxD, we will find:
> .IEND®B\`‚ÿÿØØÿÿàà....JJFFIIFF..........\`\`..\`\`....ÿÿÛÛ..CC.......

- It seems that two jpg image (based on jpg file signature) appended with pattern:
> 12121212.... 

- We can use this script to get that two image:

```python
file = open('flag.png', 'r')
file_one = open('jpg_one.jpg', 'w')
file_two = open('jpg_two.jpg', 'w')

data = file.read()

for i in range(0x47B9, len(data)):
    if i % 2 == 0:
        file_one.write(data[i])
    else:
        file_two.write(data[i])

file.close()
file_one.close()
file_two.close()
```

- Open the image and we will get the flag: `COMPFEST9{tw0_1m493_1n_0n3_f1l3}`
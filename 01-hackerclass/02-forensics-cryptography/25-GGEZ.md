GGEZ (25)
=========

## Description

![GGEZ.svg](https://ctf-class.compfest.web.id/files/92be836b8789acead8e4c6f581b02ca8/ggez.svg)

## Write Up

This is straightforward. If we open the image, we see:

```xml
<?xml version="1.0" standalone="no"?><!-- Generator: Gravit.io --><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate" viewBox="0 0 500 500" width="500" height="500"><path d=...(truncated)..." fill-rule="evenodd" fill="rgb(0,0,0)"/><rect x="0" y="0" width="500" height="500" transform="matrix(1,0,0,1,0,0)" fill="rgb(255,255,255)"/></svg>
```

We can see that there's a big white rectangle hiding the path below it. If you remove the dom (for example with Chrome Dev Tool), you will get the flag: `COMPFEST9{too_ez_fore_me}`

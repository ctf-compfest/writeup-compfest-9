Weird Characters (25)
=====================

## Description

I want to give the flag but why is it broken?...
`COMPFEST9{â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;½â&nbsp;â&nbsp;â&nbsp;â&nbsp;}`

> Note: valid flag format is `COMPFEST9{plain_text}` where plain_text is a set of alphanumeric (a-z and A-Z) and/or underscore

## Write Up

> `â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;â&nbsp;½â&nbsp;â&nbsp;â&nbsp;â&nbsp;`

Those characters seems like broken unicode, what if we convert it from UTF-8 to Unicode (and replacing `&nbsp;` with actual space)

> ⠙⠕⠞⠎⠙⠕⠞⠎⠎⠕⠍⠁⠝⠽⠙⠕⠞⠎

Those looks like a braille, lets [decode it](https://duckduckgo.com/?q=%E2%A0%99%E2%A0%95%E2%A0%9E%E2%A0%8E%E2%A0%99%E2%A0%95%E2%A0%9E%E2%A0%8E%E2%A0%8E%E2%A0%95%E2%A0%8D%E2%A0%81%E2%A0%9D%E2%A0%BD%E2%A0%99%E2%A0%95%E2%A0%9E%E2%A0%8E&atb=v73-3__&ia=answer)

> dotsdotssomanydots

Thus, the flag is `COMPFEST9{dotsdotssomanydots}`.

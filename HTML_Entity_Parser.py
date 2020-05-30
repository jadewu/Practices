# 简单的python replace做法，得把&放在最后改，不然会重复改
class Solution:
    def entityParser(self, text: str) -> str:
        # 不能直接用html函数
        # import html
        # s = html.escape(text)
        # print(s)
        # from html.parser import HTMLParser
        # res = HTMLParser().unescape(text)
        # # print(res)
        text = text.replace('&quot;', '"')
        text = text.replace('&apos;', "'")
        text = text.replace('&gt;', '>')
        text = text.replace('&lt;', '<')
        text = text.replace('&frasl;', '/')
        text = text.replace('&amp;', '&')
        return(text)

# 自己写的比较方法
class Solution:
    def entityParser(self, text: str) -> str:
        start = 0
        l = list(text)
        res = ''
        i = 0
        while i < len(l):
            if i < len(l) - 3:
                word = l[i] + l[i+1] + l[i+2] + l[i+3]
                if word == '&gt;':
                    res += '>'
                    i += 4
                    continue
                elif word == '&lt;':
                    res += '<'
                    i += 4
                    continue
                if i < len(l) - 4:
                    if word + l[i+4] == '&amp;':
                        res += '&'
                        i += 5
                        continue
                if i < len(l) - 5:
                    if word + l[i+4] + l[i+5] == '&quot;':
                        res += '"'
                        i += 6
                        continue
                    elif word + l[i+4] + l[i+5] == '&apos;':
                        res += "'"
                        i += 6
                        continue
                if i < len(l) - 6:
                    if word + l[i+4] + l[i+5] + l[i+6] == '&frasl;':
                        res += '/'
                        i += 7
                        continue
            res += l[i]
            i += 1
           # print(res)
        return res

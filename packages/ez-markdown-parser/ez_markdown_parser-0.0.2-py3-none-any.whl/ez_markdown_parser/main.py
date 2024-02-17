import re

class EzMarkdownParser:
    escaper = '\\'
    special_chars = ['#']
    
    #def __init__(self):
        #self.md = md
        # print('aaaa')
        # print(self.escaper)
        # self.mainn(md)
        
        # if '\n' in md:
        #     print('aaaminirjirg')
        
        # https://www.markdownguide.org/cheat-sheet/
        # https://www.dataquest.io/blog/regex-cheatsheet/
        # https://www.markdownguide.org/basic-syntax/
        # https://www.w3schools.com/python/gloss_python_string_slice.asp
        # https://www.w3schools.com/python/python_ref_string.asp
        
        
       # ^#{1,6} .+$|\*{2}.+\*{2}|^- .+$|    |^.+$
    def htmlify(self, md):
        result = ''
        # Titulos | negritas | listas desordenadas | Links
        # \*{2}.+\*{2}|    |\[.+?\]\(.+?\)
        
        # Hay problemas con detectar por ejemplo negrita o links si estan dentro de un heading
        # Falta capturar el texto normal
        
        
        # Replace with html tags on lines that md must be at the begining (headings, list items, and well... paragraphs)
        # pattern = re.compile(r'^#{1,6} .+$|^- .+$|.+', re.MULTILINE)
        # matches = pattern.findall(md)
        #print(matches)
        
        str_list = md.split('\n')
        
        for text in str_list:
            if re.findall(r'^#{1,6} .+$', text):
                result = result + self.processHeadings(text) + '\n'
            elif re.findall(r'^- .+$|^\* .+$', text):
                result = result + self.processListItems(text) + '\n'
            elif text != '':
                result = result + self.processParagraphs(text) + '\n'
                
        # Now replace the parts that can be anywhere in the text (boldface text, links)
        
        result = self.processBoldies(result)
        #print(result)
        result = self.processLinks(result)
        return result
        # pattern = re.compile(r'\*{2}.+?\*{2}|\[.+?\]\(.+?\)', re.MULTILINE)
        # matches = pattern.findall(result)
        
        # for match in matches:
        #     if 
            
        # print(result)
    
    # Methods for tags that DO need md to be at the begining of the line:                
    def processHeadings(self, text):
        count = 0
        for i in range(6):
            if (text[i] == '#'):
                count += 1
            else:
                break
        return text.replace(text[0:count+1], f'<h{count}>') + f'</h{count}>'
        # headingTag = withoutNumerals + f'</h{count}>'
        # print("1..."+text, "2..."+text[0:count+1], "3..."+str(count), '4...'+withoutNumerals, "      "+headingTag)
        #return headingTag
    
    def processListItems(self, text):
        return text.replace(text[0:2], '<li>') + '</li>'
    
    def processParagraphs(self, text):
        return f'<p>{text}</p>'
    
    # Methods for tags that doesnt need md to be at the begining of the line:
    def processBoldies(self, html):
        pattern = re.compile(r'\*{2}.+?\*{2}', re.MULTILINE)
        matches = pattern.findall(html)
        for match in matches:
            htmlTag = '<strong>' + match[2:-2] + '</strong>'
            html = html.replace(match, htmlTag, 1) # might be optimized if 1 is removed           
        return html
    
    def processLinks(self, html):
        pattern = re.compile(r'\[.+?\]\(.+?\)', re.MULTILINE)
        matches = pattern.findall(html)
        for match in matches:
            parts = match.split('](')
            htmlTag = f'<a href="{parts[1][:-1]}">{parts[0][1:]}</a>'
            html = html.replace(match, htmlTag, 1) # might be optimized if 1 is removed 
        return html
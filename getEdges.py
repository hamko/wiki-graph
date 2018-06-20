import sys
import urllib.parse


memo = set()
with open(sys.argv[1]) as f:
    ss = f.readlines();
    for _ in range(0, len(ss)):
        s = ss[_]
        openbraces = 0
        for i in range(0, len(s)):
            if s[i] == '[':
                openbraces += 1
            else:
                openbraces = 0;
                continue;

            contents = "";
            if openbraces == 2: 
                openbraces = 0
                pos = s[i+1:].find("]]")
                if pos != -1:
                    contents = s[i+1:i+1+pos]

                if contents.find(">") != -1:
                    continue

                basename = sys.argv[1][0:-4]
                url = ""
                for j in range(0, len(basename)//2):
                    url += '%' + basename[2*j:2*j+2]

                title = urllib.parse.unquote(url)
                if len(contents.strip()) == 0: 
                    continue;
                if len(title.strip()) == 0: 
                    continue;
                forbidden = ["[", "]", ":", "FormattingRules", "InterWiki", "PukiWiki/"]
                goNext = 0
                for j in range(len(forbidden)):
                    if title.find(forbidden[j]) != -1:
                        goNext = 1
                        break;
                    if contents.find(forbidden[j]) != -1:
                        goNext = 1
                        break;
                if goNext == 1: 
                    continue;
                
                pair = title+"##########"+contents
                if pair in memo:
                    continue;
                memo.add(pair)

                print("\""+title+"\"->\""+contents+"\";")


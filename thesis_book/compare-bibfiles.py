# module that compares bib files


bibfiles = ['hbc-references.bib','intro-discussion-refs.bib']

bibfile1 = bibfiles[0]
bibfile2 = bibfiles[1]
# code based on the example in : https://www.codegrepper.com/code-examples/python/how+to+compare+two+text+files+in+python

with open(bibfile1, 'r',encoding='utf8') as file1:
    with open(bibfile2, 'r',encoding='utf8') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('bibfile-commonlines.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
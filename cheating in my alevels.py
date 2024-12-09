# Python script to format f.txt into the desired type() format

with open('f.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()

paragraphs = content.strip().split('\n')

with open('output_hidscript.txt', 'w', encoding='utf-8') as outfile:
    outfile.write('type(\n\n')
    for i, para in enumerate(paragraphs):
        escaped_para = para.replace('"', '\\"')
        ending = ' +\n\n' if i < len(paragraphs) - 1 else '\n\n'
        outfile.write(f'    "{escaped_para}\\n\\n"{ending}')
    outfile.write(');')
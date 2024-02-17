import os
import subprocess


def extract_tokens(line_str):
    res = ""
    i1 = line_str.index('=')
    i2 = line_str.index('.')
    if i1 != -1 and i2 != -1:
        res = line_str[i1 + 1:i2]
    return res.replace(',', '').strip().split()


def tokenize(lang, input_file, output_file_name):
    subprocess.Popen(
        ['perl', f'{os.path.dirname(__file__)}/perl_word_tokenizer/tokenizer_indic_pkg.pl', f"-l={lang}", f"-i={input_file}", f"-o={output_file_name}.txt"]).communicate()

    result = ''
    with open(f"{output_file_name}.txt", encoding='utf-8') as fp:
        while True:
            lines = fp.readline()
            result += f"{lines.strip()}\n"
            if lines and 'wtok' in lines:
                count = 1
                for line in extract_tokens(lines):
                    result += f"{count} {line.strip()} unk\n"
                    count += 1
            if not lines:
                break
    return result


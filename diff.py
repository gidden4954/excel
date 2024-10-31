import pandas as pd
import sys
import os
import subprocess

def main(argv):
    file_path1 = argv[1]
    file_path2 = argv[2]

    file1 = read_file(file_path1)
    print('첫번째 파일읽기 완료')

    file2 = read_file(file_path2)
    print('두번째 파일읽기 완료')

    print('파일 merge 시작')
    merged_df = pd.merge(file1, file2, how='outer', indicator=True)

    diff_df = merged_df[merged_df['_merge'] != 'both']
    print('파일 merge 완료')

    diff_filename = 'diff_' + extract_filename(file_path1) + '_' + file_path2
    diff_df.to_excel(diff_filename,index=False)
    print('쓰기완료')

    output_file = os.path.abspath(diff_filename)

    if os.path.exists(output_file):
        if sys.platform == 'darwin':
            subprocess.call(('open', output_file))
        elif sys.platform == 'win32':
            os.startfile(output_file)
        else:
            subprocess.call(('xdg-open', output_file))


def extract_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def extract_filename(file_path):
    file_name = os.path.basename(file_path)
    filename_without_extension, _ = os.path.splitext(file_name)
    return filename_without_extension


def read_file(file_path):
    extension = extract_extension(file_path)
    if ".xlsx" == extension:
        return pd.read_excel(file_path)
    if ".csv" == extension:
        return pd.read_csv(file_path)


if __name__ == '__main__':
    main(sys.argv)

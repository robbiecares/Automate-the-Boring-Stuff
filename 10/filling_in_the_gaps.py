# ! python3

import os
import shutil
from pathlib import Path

"""filling_in_the_gaps.py"""

"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single
folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
"""


class FileSet:

    def __init__(self, prefix, directory, num_files):
        self.prefix = prefix
        self.directory = Path(directory)
        self.num_files = num_files
        self.create_files()
        self.file_names = self.get_filenames()

    def create_files(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        for i in range(1, self.num_files + 1):
            formatted_num = str(i).rjust(len(str(self.num_files)), '0')
            base_name = self.prefix + formatted_num + '.txt'
            f_path = os.path.join(self.directory, base_name)
            with open(f_path, 'w') as f:
                f.write(f'this file is named {base_name}')

    def get_filenames(self):
        file_names = [file_name for file_name in os.listdir(self.directory) if file_name.startswith(self.prefix)]
        file_names.sort()
        return file_names

    def delete_file(self, nums=['003']):
        for num in nums:
            path = os.path.join(self.directory, f'{self.prefix}{num}.txt')
            os.unlink(path)
        print(f'file(s) {nums} deleted')

    def get_file_num(self, file_name):
        num = file_name.split('.')[0]
        num = num[len(self.prefix):]
        num = int(num.lstrip('0'))
        return num

    def has_gaps(self):
        files = self.get_filenames()
        last_file_num = self.get_file_num(files[-1])

        if len(files) != last_file_num:
            print("there's a gap")
            return True
        else:
            print('the list of files has no gaps')
            return False

    def format_file_num_as_string(self, num):
        last_num = str(self.get_file_num(self.file_names[-1]))
        num = str(num)
        while len(num) < len(last_num):
            num = str(0) + num
        return num

    def update_file_number(self, file_name, new_num):
        # todo: use 'p.' syntax for referencing file sections (will need to pass full path)

        file_name, ext = file_name.split('.')
        prefix, num = file_name[:len(self.prefix)], file_name[len(self.prefix):]
        if new_num:
            file_name = file_name.replace(num, new_num)

        return f'{file_name}.{ext}'

    def correct_gaps(self):
        if self.has_gaps:
            print('correcting gaps')
            correct_num_files = len(self.get_filenames())
            formatted_nums = [self.format_file_num_as_string(i) for i in range(1, correct_num_files + 1)]
            for file_name, correct_file_num in zip(self.get_filenames(), formatted_nums):
                if file_name.split('.')[0].endswith(correct_file_num):
                    # print(f'same - {file_name}, {correct_file_num}')
                    continue
                else:
                    # print(f'diff - {file_name}, {correct_file_num}')
                    new_file_name = self.update_file_number(file_name, correct_file_num)
                    # print(rf'{self.directory}\{file_name}')
                    # print(rf'{self.directory}\{new_file_name}')
                    shutil.move(rf'{self.directory}\{file_name}', rf'{self.directory}\{new_file_name}')

    def insert_gap(self, num):
        # pick a location between two numbers (e.g. 55)

        # start a loop at the index of that file
        os.mkdir(os.path.join(self.directory, 'temp'))
        og_file = os.path.join(self.directory, self.file_names[num-1])
        temp_dir = os.path.join(self.directory, 'temp')

        # renames every file from 'x' to 'x' + 1
        for file_name in self.file_names[num-1:]:
            new_num = self.get_file_num(file_name) + 1
            new_num = self.format_file_num_as_string(new_num)
            new_file_name = self.update_file_number(file_name, new_num)
            # print(os.path.join(self.directory, file_name))
            # print(os.path.join(self.directory, new_file_name))
            shutil.move(os.path.join(self.directory, file_name), os.path.join(temp_dir, new_file_name))

        # move files from temp dir and remove it
        for file in Path(temp_dir).glob('*.txt'):
            shutil.move(file.__str__(), self.directory)
        os.rmdir(temp_dir)

        # create one new file with the original number (i.e. fill the new gap)
        with open(og_file, 'w') as f:
            f.write(f'this file is named {og_file}')
        # sort the list

    def delete_directory(self):
        shutil.rmtree(self.directory)


directory = r'C:\Users\Betty\Desktop\temp'
if os.path.exists(directory):
    shutil.rmtree(directory)

fileset = FileSet(prefix='spam', directory=directory, num_files=100)

fileset.delete_file()
fileset.has_gaps()
fileset.correct_gaps()
fileset.has_gaps()
# fileset.insert_gap(7)
# fileset.has_gaps()


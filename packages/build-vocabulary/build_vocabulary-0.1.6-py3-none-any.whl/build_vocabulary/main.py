import argparse
import logging
import math
import os.path
import pprint
import re
import time
from datetime import datetime
from functools import reduce
from multiprocessing.pool import Pool

import tqdm
from nltk import pos_tag, WordNetLemmatizer

from build_vocabulary.file_reader import Reader

with open(os.path.join(os.path.dirname(__file__), ".assert", "60000.txt"), encoding="utf-8") as f:
    COCA_LIST = f.read().split()

# 配置日志
logging.basicConfig(level=logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
NOW = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
msg = "处理后的文件存放于{}。"


class TextProcessor:
    @classmethod
    def run(cls, text):
        words_list = dict.fromkeys(re.findall("([a-zA-Z]+)", text.lower()))
        words_list = cls.lemmatize_tokens(words_list)
        return words_list

    @staticmethod
    def lemmatize_tokens(words_list):
        wnl = WordNetLemmatizer()
        tokens = {}
        tagged = pos_tag(words_list)
        for token, tag in tqdm.tqdm(tagged, "lemmatize_tokens"):
            if tag.startswith(("N", "V")):
                a = wnl.lemmatize(token, tag[0].lower())
                tokens[a] = None
            tokens[token] = None
        return tokens


def _find_start_and_end_indexes(text, start_marker, end_marker):
    start_index = None
    end_index = None
    if start_marker:
        head = re.search(start_marker, text)
        if not head:
            logging.warning("头部没有匹配到。")
        else:
            start_index = head.span()[0]
    if end_marker:
        tail = re.search(end_marker, text)
        if not tail:
            logging.warning("尾部没有匹配到。")
        else:
            end_index = tail.span()[1]
    return start_index, end_index


def _process_and_save_word_set(word_dict, save_path):
    string_lists = [item for item in word_dict if item in COCA_LIST]
    string_list_group = [string_lists[i * 5000:(i + 1) * 5000] for i in
                         range(math.ceil(len(string_lists) / 5000))]
    flag = False
    for index, group in enumerate(string_list_group):
        index = "" if len(string_list_group) == 1 else f"_{index}"
        with open(save_path + f"{index}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(group))
        flag = True
    return flag


def process_and_save_text_segment(save_path, text, start, end, exclude_set):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    start_index, end_index = _find_start_and_end_indexes(text, start, end)
    word_dict = TextProcessor.run(text[start_index:end_index])
    word_dict = {item: None for item in word_dict if item not in exclude_set}
    flag = _process_and_save_word_set(word_dict, save_path)
    if flag:
        logging.info(msg.format(save_path))
    else:
        logging.info("没有新增的词语。")


def process_directory_files(directory):
    string_lists, paths = Reader.read_directory(directory)
    if len(string_lists) > 261:
        pool = Pool()
        async_results = []
        for single_string in string_lists:
            async_results.append(
                pool.apply_async(TextProcessor.run, args=(single_string,)))
        results = [item.get() for item in
                   tqdm.tqdm(async_results, desc="Directory processing")]
    else:
        results = [TextProcessor.run(single_string) for single_string in
                   tqdm.tqdm(string_lists)]
    return results, paths


def merge_or(x, y):
    return x | y


def recursive_merge_or(results, pool):
    if len(results) <= 65:
        return reduce(lambda x, y: x | y, tqdm.tqdm(results, desc="integrating"))
    else:
        if len(results) % 2 == 1:
            results.append(set())
        apply_results = []
        for i in range(len(results) // 2):
            apply_results.append(pool.apply_async(func=merge_or, args=(results[i * 2:(i + 1) * 2])))
        results = [item.get() for item in tqdm.tqdm(apply_results, desc="integrating")]
        return recursive_merge_or(results, pool)


def main(text=None, file_path=None, directory=None, start=None, end=None, file_filter=None, record_exclude=None,
         integrate=None, exclude=None):
    t0 = time.time()
    parser = argparse.ArgumentParser(
        description="这个程序能够将英文文本拆分成单个单词，并可以通过过滤功能来专注于学习不熟悉的单词。")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("file_path", default="", type=str,
                       help="指定单个文件的路径，该文件可以是pdf、pptx、docx或文本格式。如果未指定，程序将等待进一步的指令。",
                       nargs="?")
    group.add_argument("-r", "--directory", default="", type=str,
                       help="指定一个文件夹路径，程序将会处理该文件夹内所有支持的文本文件。")
    group.add_argument("-t", "--text", default="", type=str, help="直接提供一大段文本进行处理，而不是通过文件路径。")
    group.add_argument("--info", action="store_true", help="显示已经学过的单词的位置")
    parser.add_argument("-s", "--start", default="", type=str,
                        help="在处理单个文件或大段文本时，指定正则表达式匹配的起始点。留空则从文本的开始处处理。")
    parser.add_argument("-e", "--end", default="", type=str,
                        help="在处理单个文件或大段文本时，指定正则表达式匹配的结束点。留空则处理到文本的结束处。")
    parser.add_argument("-i", "--integrate", action="store_true",
                        help="在指定一个文件夹路径时, 是否将该文件夹内所有的结果整合到一起。")
    parser.add_argument("-f", "--file_filter", default="", type=str,
                        help="指定一个文件路径，程序会在最终生成的单词列表中排除掉这个文件中出现的单词。\n"
                             "这个选项适用于想要创建一个不含特定单词的单词列表的情况。")
    parser.add_argument("--record_exclude", action="store_true", help="将任意方式生成的词汇表写到文件里，下次生成词汇表时，使用--exclude来激活排除。\n"
                                                                      "该单词本中的词汇将不会再出现再新的词汇表里。使用--info可以查看不被包括的单词。")
    parser.add_argument("-ex", "--exclude", action="store_true", help="激活排除。\n")
    args = parser.parse_args()
    directory = args.directory or directory
    text = args.text or text
    file_path = args.file_path or file_path
    start = args.start or start
    end = args.end or end
    file_filter = args.file_filter or file_filter
    info = args.info
    exclude = args.exclude or exclude
    record_exclude = args.record_exclude or record_exclude
    integrate = args.integrate or integrate
    exclude_file_root = os.path.abspath(os.path.expanduser(os.path.join("~", ".vocabulary")))

    exclude_word_set = set()
    if file_filter and os.path.isfile(file_filter):
        exclude_text = Reader.read(file_filter)
        exclude_word_set = TextProcessor.run(exclude_text)
    learned_words_root = os.path.expanduser(os.path.join("~", ".vocabulary"))
    if exclude:
        if os.path.isdir(learned_words_root):
            results, _ = process_directory_files(learned_words_root)
            if results:
                exclude_word_set.update(reduce(lambda x, y: x | y, results))
    default_save_name = NOW
    if record_exclude:
        integrate = True
        save_root = exclude_file_root
    else:
        save_root = "vocabulary"
    if text:
        save_path = os.path.join(save_root, default_save_name)
        process_and_save_text_segment(save_path, text, start, end, exclude_word_set)

    elif file_path:
        if not os.path.isfile(file_path):
            logging.error(f"文件路径:{file_path}不正确。")
            return -2
        if record_exclude:
            file_name = default_save_name
        else:
            file_name = re.sub("(.[^.]+)$", "", os.path.basename(file_path))
        text = Reader.read(file_path)
        save_path = os.path.join(save_root, file_name)
        process_and_save_text_segment(save_path, text, start, end, exclude_word_set)

    elif directory:
        if not os.path.isdir(directory):
            logging.error(f"文件夹路径:{directory}不正确。")
            return -2
        results, paths = process_directory_files(directory)
        if integrate:
            save_path = os.path.join(save_root, default_save_name)
            pool = Pool()
            word_dict = recursive_merge_or(results, pool)
            word_dict.difference_update(exclude_word_set)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            _process_and_save_word_set(word_dict, save_path)
            if word_dict:
                logging.info(msg.format(save_path))
            else:
                logging.info("没有新增的词语。")
        else:
            commonpath = os.path.commonpath(paths)
            flag = False
            for word_dict, path in zip(results, paths):
                save_path, suffix = os.path.splitext(path)
                save_path = save_path.replace(commonpath, save_root)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                word_dict.difference_update(exclude_word_set)
                flag = (_process_and_save_word_set(word_dict, save_path) or flag)
            if flag:
                logging.info(msg.format(save_root))
    elif info:
        info_msg = pprint.pformat({
            "exclude dir": exclude_file_root,
            "exclude_words": list(exclude_word_set)
        })
        logging.info(info_msg)
    else:
        parser.print_help()
    print(time.time() - t0)


if __name__ == "__main__":
    main()

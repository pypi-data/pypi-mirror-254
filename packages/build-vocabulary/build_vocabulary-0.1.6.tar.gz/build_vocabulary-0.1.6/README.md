# 英文单词书制作

### 介绍
这是一个自然语言处理工具集，主要用于文本处理、分词、词形还原等任务。该工具集可以处理英文文本，提取英文文本中的单词生成单词书，并支持文本的批量处理和保存。


### 安装教程

```bash
pip install -r requirements.txt
```
或者, 当前需要在官方源
```bash
pip install build_vocabulary
```

### 使用说明
```bash
usage: main.py [-h] [-r DIRECTORY] [-t TEXT] [--info] [-s START] [-e END] [-i]
               [-f FILE_FILTER] [--record_exclude] [--exclude]
               [file_path]

这个程序能够将英文文本拆分成单个单词，并可以通过过滤功能来专注于学习不熟悉的单词。

positional arguments:
  file_path             指定单个文件的路径，该文件可以是pdf、pptx、docx或文本格式。如果未指定，程序将等待进一步的指令。

optional arguments:
  -h, --help            show this help message and exit
  -r DIRECTORY, --directory DIRECTORY
                        指定一个文件夹路径，程序将会处理该文件夹内所有支持的文本文件。
  -t TEXT, --text TEXT  直接提供一大段文本进行处理，而不是通过文件路径。
  --info                显示已经学过的单词的位置
  -s START, --start START
                        在处理单个文件或大段文本时，指定正则表达式匹配的起始点。留空则从文本的开始处处理。
  -e END, --end END     在处理单个文件或大段文本时，指定正则表达式匹配的结束点。留空则处理到文本的结束处。
  -i, --integrate       在指定一个文件夹路径时, 是否将该文件夹内所有的结果整合到一起。
  -f FILE_FILTER, --file_filter FILE_FILTER
                        指定一个文件路径，程序会在最终生成的单词列表中排除掉这个文件中出现的单词。
                        这个选项适用于想要创建一个不含特定单词的单词列表的情况。
  --record_exclude      将任意方式生成的词汇表写到文件里，下次生成词汇表时，使用--exclude来激活排除。
                        该单词本中的词汇将不会再出现再新的词汇表里。使用--info可以查看不被包括的单词。
  --exclude             激活排除。
```
或者安装到环境后
```bash
build_vocabulary.exe
```
### 注意事项
在使用该工具集之前，请确保已经安装了所有必要的Python库。
COCA列表应该是一个文本文件，其中每行包含一个单词。
该工具集默认使用UTF-8编码处理文本。
### 贡献
欢迎任何形式的贡献，包括代码、文档、建议等。请通过GitHub上的issues或者pull requests与我联系。
### 许可证
该软件使用MIT许可证发布。请确保在分发或使用该软件时遵守相应的许可协议。

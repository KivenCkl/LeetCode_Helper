'''
@Author: KivenChen
@Date: 2019-04-27
@LastEditTime: 2019-05-05
'''

# 根目录下的 README 英文模板
TEMPLATE_README_EN = '''
| English | [简体中文](README.md) |

<p align="center"><img width="300" src="https://raw.githubusercontent.com/KivenCkl/LeetCode_Helper/master/imgs/leetcode-logo.png"></p>
<p align="center">
    <img src="https://img.shields.io/badge/User-{user_name}-blue.svg?" alt="">
    <img src="https://img.shields.io/badge/Solved-{num_solved}/{num_total}-blue.svg?" alt="">
    <img src="https://img.shields.io/badge/Easy-{ac_easy}-green.svg?" alt="">
    <img src="https://img.shields.io/badge/Medium-{ac_medium}-orange.svg?" alt="">
    <img src="https://img.shields.io/badge/Hard-{ac_hard}-red.svg?" alt="">
</p>
<h1 align="center">My LeetCode Solutions</h1>

<p align="center">
    <br>
    <b>Last updated: {time}</b>
    <br>
</p>
<!--请保留下面这行信息，让更多用户了解到这个小爬虫，衷心感谢您的支持-->
<p align="center">The source code is fetched using the tool <a href="https://github.com/KivenCkl/LeetCode_Helper">LeetCode_Helper</a>.</p>

| # | Title | Solutions | Acceptance | Difficulty | Tags |
|:--:|:-----|:---------:|:----:|:----:|:----:|
'''

# 根目录下的 README 中文模板
TEMPLATE_README_CN = '''
| [English](README_EN.md) | 简体中文 |

<p align="center"><img width="300" src="https://raw.githubusercontent.com/KivenCkl/LeetCode_Helper/master/imgs/leetcode-logo.png"></p>
<p align="center">
    <img src="https://img.shields.io/badge/用户-{user_name}-blue.svg?" alt="">
    <img src="https://img.shields.io/badge/已解决-{num_solved}/{num_total}-blue.svg?" alt="">
    <img src="https://img.shields.io/badge/简单-{ac_easy}-green.svg?" alt="">
    <img src="https://img.shields.io/badge/中等-{ac_medium}-orange.svg?" alt="">
    <img src="https://img.shields.io/badge/困难-{ac_hard}-red.svg?" alt="">
</p>
<h1 align="center">LeetCode 的解答</h1>

<p align="center">
    <br>
    <b>最近一次更新: {time}</b>
    <br>
</p>
<!--请保留下面这行信息，让更多用户了解到这个小爬虫，衷心感谢您的支持-->
<p align="center">The source code is fetched using the tool <a href="https://github.com/KivenCkl/LeetCode_Helper">LeetCode_Helper</a>.</p>

| # | 题名 | 解答 | 通过率 | 难度 | 标签 |
|:--:|:-----|:---------:|:----:|:----:|:----:|
'''

# 根目录下 README 中的题目概要信息
TEMPLATE_README_APPEND = '|{frontend_id}|{title}{paid_only}{is_favor}|{solutions}|{ac_rate}|{difficulty}|{tags}|\n'

# 题目描述 README 英文模板
TEMPLATE_DESC_EN = '''
| English | [简体中文](README.md) |

# {title_en}

## Description

{content_en}

## Related Topics

{tags_en}

## Similar Questions

{similar_questions_en}
'''

# 题目描述 README 中文模板
TEMPLATE_DESC_CN = '''
| [English](README_EN.md) | 简体中文 |

# {title_cn}

## 题目描述

{content_cn}

## 相关话题

{tags_cn}

## 相似题目

{similar_questions_cn}
'''

# 题目代码模板
TEMPLATE_CODE = '''
{style} @Title: {title_cn} ({title_en})
{style} @Author: {author}
{style} @Date: {timestamp}
{style} @Runtime: {runtime}
{style} @Memory: {memory}

{code}
'''

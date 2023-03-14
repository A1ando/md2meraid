# _*_ coding: utf-8 _*_

"""
本质是定位当前标题级别的索引和距离它最近的上一级索引，
最近的上一级索引可以在历遍的时候通过字典实时更新
"""


def parse(lst):
	"""
	lst: 每行文本的标题级别列表
	fmt = '{} --> {};'
	返回需要格式化的索引元组
	"""
	groups = []
	register = {}
	for index, rank in enumerate(lst):
		register[rank] = index
		if rank > 1:
			groups.append((register[rank-1], index))
	return groups


if __name__ == '__main__':
	# 读取xmind导出的md文本
	with open('xxx.md', 'r', encoding='utf8') as f:
		contentList = f.read().split('\n\n')
		
	# 需要格式化的文本
	texts = [i.split('# ')[-1] for i in contentList]

	# 使用'# '找出每行文本的标题级别，正文为0
	ranks = [i.find('# ')+1 for i in contentList]

	fmt = '{} --> {};'
	for i, j in parse(ranks):
		print(fmt.format(texts[i], texts[j]))

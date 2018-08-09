import sys
sys.path.append("..")
import Statistics
import 图表.Chart as tb

s = Statistics.Statistics('../other/西游记.txt')
print(s)
tb.histogram(s,15,'西游记','出现最多的字','出现的次数')
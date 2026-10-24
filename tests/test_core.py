import unittest
from referrer_attribution_bounds import run
class Tests(unittest.TestCase):
 def test_known_frechet_bounds_and_constructive_collapsed_margins(self):
  r=run({'row_margins':{'a':70,'b':30},'column_margins':{'x':60,'y':40},'focus':{'row':'a','column':'x'}});cell=next(x for x in r['cell_bounds']if x['row']=='a'and x['column']=='x');self.assertEqual((cell['minimum'],cell['maximum']),(30,60))
  for name in ('minimum_collapsed_coupling','maximum_collapsed_coupling'):
   m=r['focus'][name];self.assertEqual([sum(row)for row in m],[70,30]);self.assertEqual([sum(m[i][j]for i in range(2))for j in range(2)],[60,40]);self.assertTrue(all(v>=0 for row in m for v in row))
 def test_all_feasible_two_by_two_integer_tables_match_bounds(self):
  for total in range(10):
   for a in range(total+1):
    for b in range(total+1):
     feasible=[x for x in range(total+1)if min(x,a-x,b-x,total-a-b+x)>=0];r=run({'row_margins':{'a':a,'other':total-a},'column_margins':{'b':b,'other':total-b}})['cell_bounds'][0];self.assertEqual((r['minimum'],r['maximum']),(min(feasible),max(feasible)))
 def test_marginals_cannot_invent_joint_conversion_rate(self):
  r=run({'row_margins':{'docs':30,'other':70},'column_margins':{'download':20,'other':80}})['cell_bounds'][0];self.assertEqual((r['minimum'],r['maximum']),(0,20))

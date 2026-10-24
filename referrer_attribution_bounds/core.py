from .common import integer,identifier

def run(data):
 rows=data['row_margins'];columns=data['column_margins']
 if not isinstance(rows,dict)or not isinstance(columns,dict)or not 1<=len(rows)<=50 or not 1<=len(columns)<=50:raise ValueError('margins')
 for margin in(rows,columns):
  for key,v in margin.items():identifier(key);integer(v,0,10**12)
 total=sum(rows.values())
 if sum(columns.values())!=total:raise ValueError('inconsistent_totals')
 bounds=[{'row':r,'column':c,'minimum':max(0,rv+cv-total),'maximum':min(rv,cv)}for r,rv in sorted(rows.items())for c,cv in sorted(columns.items())];focus=data.get('focus',{'row':sorted(rows)[0],'column':sorted(columns)[0]});r=focus['row'];c=focus['column']
 if r not in rows or c not in columns:raise ValueError('focus')
 rv=rows[r];cv=columns[c];low=max(0,rv+cv-total);high=min(rv,cv)
 def witness(x):return [[x,rv-x],[cv-x,total-rv-cv+x]]
 return {'total':total,'cell_bounds':bounds,'focus':{'row':r,'column':c,'minimum_collapsed_coupling':witness(low),'maximum_collapsed_coupling':witness(high),'matrix_axes':'focus_vs_all_other_rows_and_columns'},'model':'frechet_marginal_count_bounds_no_joined_identity_or_causal_attribution'}

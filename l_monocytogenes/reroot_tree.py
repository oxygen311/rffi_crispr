from ete3 import Tree, TreeStyle

from glob import glob

tree_file = glob('*_21.newick')[0]
t = Tree(tree_file)


circular_style = TreeStyle()
circular_style.mode = "c" # draw tree in circular mode
circular_style.show_branch_support = True
# circular_style.scale = 20

# t.set_outgroup(t.get_common_ancestor(t & 'LEPN.0521.00010', t & 'LEPN.0521.00006'))
# t.set_outgroup(t.get_common_ancestor(t & 'PSAE.0521.00253', t & 'PSAE.0521.00085'))
# t.set_outgroup(t.get_common_ancestor(t & 'PSAE.0521.00253', t & 'PSAE.0521.00148'))
# t.set_outgroup(t.get_common_ancestor(t & 'BUMA.0521.00012', t & 'BUMA.0521.00005'))
t.set_outgroup(t.get_common_ancestor(t & 'CP002816.1', t & 'CP030809.1'))

t.render("test.pdf", tree_style=circular_style)
t.write(outfile=tree_file.replace('_21', '_21_reroot'))

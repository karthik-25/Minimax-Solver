import sys

from tree import Tree, TreeNode
from io_processor import IO_Processor

def main():
    iop = IO_Processor()
    iop.parse_input(sys.argv[1:])
    
    gt = Tree()
    gt.build_tree(iop.input_file)

    gt.perform_minimax(gt.root_node, iop.is_root_max, iop.is_ab_pruning, iop.max_cutoff)

    iop.print_output(gt.output_list)

if __name__ == "__main__":
    main()
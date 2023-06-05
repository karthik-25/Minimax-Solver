import sys

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.children = []
        self.is_child = False
        self.is_leaf = False
        
class Tree:
    def __init__(self):
        self.nodes = {}
        self.root_node = None
        self.output_str = "{0}({1}) chooses {2} for {3}"
        self.tree_build_fail_str = "Error: Tree build failed."
        self.output_list = []
    
    def build_tree(self, input_file):
        with open(input_file, "r") as f:
            for line in f:
                if ":" in line:
                    self.process_internal_node_line(line)                                         
                
                elif "=" in line:
                    self.process_leaf_node_line(line)
                
                else:
                    print(self.tree_build_fail_str, "Input line does not follow expected format: {0}".format(line))
                    sys.exit()
                    
        self.validate_tree()
        
    def process_internal_node_line(self, line):
        parent_name = line.split(":")[0]
        if parent_name not in self.nodes:
            self.nodes[parent_name] = TreeNode(parent_name)

        children_names = line.split(":")[1].strip()[1:-1].split(", ")
        for child_name in children_names:
            if child_name not in self.nodes:
                self.nodes[child_name] = TreeNode(child_name)

            self.nodes[child_name].is_child = True
            self.nodes[parent_name].children.append(self.nodes[child_name])
            
    def process_leaf_node_line(self, line):
        node_name = line.split("=")[0]
        node_value = int(line.split("=")[1])
        if node_name not in self.nodes:
            print(self.tree_build_fail_str, "Node {0} must be defined before assigning value.".format(node_name))
            sys.exit()

        self.nodes[node_name].value = node_value
        self.nodes[node_name].is_leaf = True
                    
    def validate_tree(self):
        # check if leaf nodes have values
        leaf_no_val = [n.name for n in self.nodes.values() if not n.children and n.value is None]
        if leaf_no_val:
            print(self.tree_build_fail_str, "Following leaf nodes have no child or value assigned: {0}".format(leaf_no_val))
            sys.exit()
            
        root_node = [n for n in self.nodes.values() if not n.is_child]
        if len(root_node)==1:
            self.root_node = root_node[0]
        else:
            if not root_node:
                print(self.tree_build_fail_str, "No root node found.")
            else:
                print(self.tree_build_fail_str, "Multiple roots found: {0}".format([n.name for n in root_node]))
            
            sys.exit()
            # raise Exception("Root node not found. Check input.")
    
    def print_tree(self):
        print("Root Node: {0}".format(self.root_node.name))
        for name, node in self.nodes.items():
            print("{0} - {1} - {2}".format(name, [c.name for c in node.children], node.value))


    def perform_minimax(self, current_node, is_max_player, ab_pruning, max_cutoff, alpha=-float('inf'), beta=float('inf'), add_output=True):
        if current_node.is_leaf:
            return current_node.value

        if is_max_player:
            best_max = -float('inf')
            for child in current_node.children:
                value = self.perform_minimax(child, False, ab_pruning, max_cutoff, alpha, beta)
                if value > best_max:
                    best_max = value
                    best_max_choice = child.name

                if best_max > max_cutoff:
                    add_output = False
                    break

                if ab_pruning:
                    alpha = max(alpha, best_max)
                    if beta <= alpha:
                        add_output = False
                        break
            
            if add_output:
                self.output_list.append(self.output_str.format("max", current_node.name, best_max_choice, best_max))
            
            add_output = True

            return best_max
        else:
            best_min = float('inf')
            for child in current_node.children:
                value = self.perform_minimax(child, True, ab_pruning, max_cutoff, alpha, beta)
                if value < best_min:
                    best_min = value
                    best_min_choice = child.name

                if best_min < -max_cutoff:
                    add_output = False
                    break

                if ab_pruning:
                    beta = min(beta, best_min)
                    if beta <= alpha:
                        add_output = False
                        break

            if add_output:
                self.output_list.append(self.output_str.format("min", current_node.name, best_min_choice, best_min))

            add_output = True

            return best_min

import sys

class IO_Processor:
    def __init__(self):
        self.is_verbose = False
        self.is_ab_pruning = False
        self.max_cutoff = None
        self.is_root_max = None
        self.input_file = None
        self.input_parse_fail_str = "Error: Input parsing failed."

    def parse_input(self, args):
        if len(args) < 3:
            print(self.input_parse_fail_str, "Invalid arguments. Sample command: python minimax.py [-v] [-ab] n min/max input_file")
            sys.exit()

        if "-v" in args:
            self.is_verbose = True

        if "-ab" in args:
            self.is_ab_pruning = True

        if "max" in args:
            self.is_root_max = True
        elif "min" in args:
            self.is_root_max = False
        else:
            print(self.input_parse_fail_str, "Invalid input: max or min not specified.")
            sys.exit()
        
        self.input_file = [arg for arg in args if ".txt" in arg][0]
        if not self.input_file:
            print(self.input_parse_fail_str, "Invalid input: input txt file not specified.")
            sys.exit()

        self.max_cutoff = int([arg for arg in args if arg not in ["max", "min", "-ab", "-v", self.input_file]][0])
        if not self.max_cutoff:
            print(self.input_parse_fail_str, "Invalid input: max value not specified.")
            sys.exit()

    def print_output(self, output_list):
        if self.is_verbose:
            for line in output_list:
                print(line)
        else:
            print(output_list[-1])
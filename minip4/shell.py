import argparse
from p4topo import P4Topo


class Shell(object):
    """ Mininet network based on P4 switches """

    def __init__(self):
        self.prog = 'minip4'

        parser = argparse.ArgumentParser(description='MiniP4 utility')
        parser.add_argument('-t', '--topology',
                            help='Topology yaml file. Default; p4-topo.yml',
                            type=str,
                            action="store",
                            default='p4-topo.yml',
                            required=False)
        parser.add_argument('-s', '--p4src',
                            help='Path to p4 source file',
                            type=str,
                            action="store",
                            required=False)

        args = parser.parse_args()

        p4topo = P4Topo(args.topology,
                        p4src=args.p4src)

        p4topo.start()


def main():
    Shell()

if __name__ == "__main__":
    main()

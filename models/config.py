import argparse
import os


class Config(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        
        self.parser.add_argument('in_planes', help='input channels number')
        self.parser.add_argument('planes', help='output channels')
        self.parser.add_argument('stride', help='no. of strides')
        self.parser.add_argument('downsample', default=None, help='downsampling')
        self.parser.add_argument('dilation', help='dilation instead of stride')
        self.parser.add_argument('norm_layer', default=None, help='norm layer added or not')
        self.parser.add_argument('group_width', help='group_width for the resnet block')
        
    def parse(self, args=''):
        args = self.parser.parse_args(args)
        args.in_planes = 3
        args.planes = 9
        args.stride = 1
        args.downsample = None
        args.group_width = 1
        args.dilation = 1 
        args.norm_layer = None
        
        return args
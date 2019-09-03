#!/usr/bin/env python

import sys
import json
from Functions import GetTokenCognito

def main(args):
    print(args)

if __name__ == '__main__':
    tokens = GetTokenCognito()
    print(tokens)

import numpy as np
from functools import partial
import PIL.Image
import tensorflow as tf
import urllib.request
import os
import zipfile

def main():
    # Step 1 - download Google's pre-trained neural network
    

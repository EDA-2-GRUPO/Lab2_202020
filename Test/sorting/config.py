import os
import sys
file_path = os.path.join(os.path.dirname(__file__), '../..')
os.chdir('..')
os.chdir('..')
file_dir = os.getcwd()
sys.path.insert(0, os.path.abspath(file_path))
data_dir = file_dir + '/Data/'

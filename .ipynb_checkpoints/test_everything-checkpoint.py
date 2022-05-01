from DSP539_tyler_t4 import *

def test_obs():
    assert observed_kmer(9,'ATTTGGATT') == 1
    
def test_obs_letter():
    assert observed_kmer(9,'ATTTGGETT') == None
    
def test_obs_bigK():
    assert observed_kmer(10,'ATTTGGATT') == None
    
def test_pos():
    assert possible_kmer(6,'ATTTGGATT') == 4
    
def test_complexity():
    assert complexity(9,'ATTTGGATT') == .875
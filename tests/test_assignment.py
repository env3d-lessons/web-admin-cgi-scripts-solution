import os
import shutil
import subprocess
import pathlib
import re
import pytest
import time

answer_url_prefix = 'learn.operatoroverload.com/~jmadar/1280'

@pytest.fixture
def check_correct_directory():
    os.popen('cp /usr/lib/cgi-bin/web-admin-cgi-scripts/q*.sh .').read()
    assert 'ubuntu' or 'codespace' in os.popen('whoami').read(), "This repo must be called using the ubuntu user"
    assert '/home/ubuntu/web-admin-cgi-scripts' or '/workspaces/web-admin-cgi-scripts' in os.popen('pwd').read(), (
        "The assignment repo must be clone into your ubuntu user root directory")
    return True

@pytest.fixture
def my_url_prefix(check_correct_directory):
    if not pathlib.Path('my_ip.txt').is_file():
        f = open('my_ip.txt','w')
        f.write(os.popen('curl ident.me').read())
        f.close()

    return open('my_ip.txt').read()+'/cgi-bin/web-admin-cgi-scripts'

def check_cgi_script_setup(f):
    with open(f) as test_sh:
        content = test_sh.read()
        assert '#!/bin/bash' in content
        assert re.search(r'content-type:.*',content, re.IGNORECASE)

def test_q1_file(check_correct_directory):
    check_cgi_script_setup('q1.sh')
    
def test_q2_file(check_correct_directory):
    check_cgi_script_setup('q2.sh')
    
def test_q3_file(check_correct_directory):
    check_cgi_script_setup('q3.sh')
    
def test_q4_file(check_correct_directory):
    check_cgi_script_setup('q4.sh')
    
def test_q5_file(check_correct_directory):
    check_cgi_script_setup('q5.sh')
    
def test_q6_file(check_correct_directory):
    check_cgi_script_setup('q6.sh')
    
def test_q7_file(check_correct_directory):
    check_cgi_script_setup('q7.sh')
    
def test_q1_exec(my_url_prefix):    
    assert 'Hello World' in os.popen(f'curl -L -s {my_url_prefix}/q1.sh').read()

def test_q2_content(my_url_prefix):
    with open('q2.sh') as test_sh:
        content = test_sh.read()
        assert re.search(r'curl.*icanhazdadjoke.com',content), "must curl to the correct service"
        
def test_q2_exec(my_url_prefix):        
    content = os.popen(f'curl -L -s {my_url_prefix}/q2.sh').read()
    assert re.search(r'I have a joke for you: .+',content, re.IGNORECASE)

@pytest.fixture
def q3_content(my_url_prefix):
    content = os.popen(f'curl -L -s {my_url_prefix}/q3.sh').read()
    return content

def test_q3_first_line(q3_content):
    assert re.search(r'current slugs',q3_content, re.IGNORECASE)

def test_q3_exec(q3_content):
    expected = os.popen(f'curl -L -s {answer_url_prefix}/q3.sh').read()
    answers = q3_content.split('\n')
    for i in range(-1, -11, -1):
        assert answers[i] in expected
    
@pytest.fixture
def q4_content(my_url_prefix):
    content = os.popen(f'curl -L -s {my_url_prefix}/q4.sh?15').read()
    return content

def test_q4_exec(q4_content):
    expected = os.popen(f'curl -L -s {answer_url_prefix}/q4.sh?15').read()
    answers = q4_content.split('\n')
    for i in range(-1, -16, -1):
        assert answers[i] in expected
    
@pytest.fixture
def q5_content(my_url_prefix):
    content = subprocess.run(['curl', '-L', '-s', f'{my_url_prefix}/q5.sh?lion'], capture_output=True)
    return content.stdout

def test_q5_exec(q5_content):
    assert b'Google' in q5_content
    assert b'Lion' in q5_content
    assert b'Animal' in q5_content

@pytest.fixture
def q6_content(my_url_prefix):
    content = os.popen(f'curl -L -s {my_url_prefix}/q6.sh?Chadwick%20Boseman').read()
    return content

def test_q6_exec(q6_content):
    assert 'Black Panther' in q6_content

@pytest.fixture
def q7_content(my_url_prefix):
    content = os.popen(f'curl -L -s {my_url_prefix}/q7.sh?Chadwick%20Boseman').read()
    return content

def test_q7_exec(q7_content):
    assert 'Black Panther' in q7_content
    assert re.search(r'img.*media-amazon.*jpg', q7_content, re.IGNORECASE)

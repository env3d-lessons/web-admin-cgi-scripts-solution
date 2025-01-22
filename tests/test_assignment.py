import os
import shutil
import subprocess
import pathlib
import re
import pytest
import time

answer_url_prefix = 'learn.operatoroverload.com/~jmadar/1280'

@pytest.fixture(scope="session", autouse=True)
def global_setup():
    assert 'ubuntu' or 'codespace' in os.popen('whoami').read(), "This repo must be called using the ubuntu user"
    assert '/home/ubuntu/web-admin-cgi-scripts' or '/workspaces/web-admin-cgi-scripts' in os.popen('pwd').read(), (
        "The assignment repo must be clone into your ubuntu user root directory")    
    if 'ubuntu' in os.popen('whoami').read():
        print("\n[Fixture] Copy all answers to repo")
        os.popen('cp /usr/lib/cgi-bin/web-admin-cgi-scripts/q*.sh .').read()
        os.popen('cp ./tests/*.tsv .').read()
        print(os.popen('ls -al').read())
    # Example: Connect to a database or start a service
    yield
    print("\n[Fixture] Cleaning up global resources")
    # Example: Close connections or shut down a service

def check_cgi_script_setup(f):
    with open(f) as test_sh:
        content = test_sh.read()
        assert '#!/bin/bash' in content
        assert re.search(r'content-type:.*',content, re.IGNORECASE)

def test_q1_file():
    check_cgi_script_setup('q1.sh')
    
def test_q2_file():
    check_cgi_script_setup('q2.sh')
    
def test_q3_file():
    check_cgi_script_setup('q3.sh')
    
def test_q4_file():
    check_cgi_script_setup('q4.sh')
    
def test_q5_file():
    check_cgi_script_setup('q5.sh')
    
def test_q6_file():
    check_cgi_script_setup('q6.sh')
    
def test_q7_file():
    check_cgi_script_setup('q7.sh')

    
def test_q1_exec():    
    assert 'Hello World' in os.popen('./q1.sh').read()

def test_q2_content():
    with open('q2.sh') as test_sh:
        content = test_sh.read()
        assert re.search(r'curl.*icanhazdadjoke.com',content), "must curl to the correct service"
        
def test_q2_exec():        
    content = os.popen('./q2.sh').read()
    assert re.search(r'I have a joke for you: .+',content, re.IGNORECASE)

@pytest.fixture(scope='session')
def q3_content():
    content = os.popen(f'./q3.sh').read()
    return content

def test_q3_first_line(q3_content):
    assert re.search(r'current slugs',q3_content, re.IGNORECASE)

def test_q3_exec(q3_content):
    expected = os.popen(f'curl -L -s {answer_url_prefix}/q3.sh').read()
    answers = q3_content.split('\n')
    for i in range(-1, -11, -1):
        assert answers[i] in expected
    
@pytest.fixture(scope='session')
def q4_content():
    content = os.popen(f'./q4.sh 15').read()
    return content

def test_q4_exec(q4_content):
    expected = os.popen(f'curl -L -s {answer_url_prefix}/q4.sh?15').read()
    answers = q4_content.split('\n')
    for i in range(-1, -16, -1):
        assert answers[i] in expected
    
def test_q5_exec():
    content = os.popen('./q5.sh lion').read()
    assert 'Microsoft' in content
    assert 'Lion' in content

def test_q6_exec():
    content = os.popen("./q6.sh 'Chadwick Boseman'").read()    
    assert 'Black Panther' in content

def test_q7_exec():
    content = os.popen("./q7.sh 'Chadwick Boseman'").read()    
    assert 'Black Panther' in content
    assert re.search(r'img.*media-amazon.*jpg', content, re.IGNORECASE)

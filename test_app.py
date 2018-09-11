import pytest
from calculadora import soma
def test_app():
 assert soma(1,1) == 2
 assert soma(0,0) == 0


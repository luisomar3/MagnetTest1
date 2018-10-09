# -*- coding: utf-8 -*-
"""
Created on Tuesday Oct 8 12:22:50 2018
Author: luisomar3
Python Version: 3.6.2

"""
import pytest

from MagnetFilter1 import validar

@pytest.mark.parametrize("test_input,expected", [
    ("(2+4)-3*(2+(4-5))", True),
    ("(2+5)-)(3))", False),
    ("((2*3))", True),
    ("((",False),   
])

def test_validar(test_input, expected): #Valido mi funcion con los resultados esperados
    assert validar(test_input) == expected

def test_validar_TypeError():#Valido que mi funcion regrese error en caso de no ser un str su entrada
    with pytest.raises(Exception) as e_info:
        validar(1)
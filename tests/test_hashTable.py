from HashTable_chains import *
from methods_of_hash import *

def test_size():
    hash_table_chained = HashTableC()
    assert hash_table_chained.size == 0
    assert hash_table_chained.size != 10
    assert hash_table_chained.size != "s"

def test_insert_on_correct_position():
    hash_table_chained = HashTableC(60)
    hash_table_chained.put(10, 10, 1)
    hash_table_chained.put(33, 30, 1)
    assert hash_table_chained.get(10, 1) == 10
    assert hash_table_chained.get(10, 1) != False
    assert hash_table_chained.get(33, 1) == 30
    assert hash_table_chained.get(33, 1) != False

def test_get_values():
    hash_table_chained = HashTableC(60)
    hash_table_chained.put(10, 6, 1)
    hash_table_chained.put(33, 30, 1)
    assert hash_table_chained.get(10, 1) == 6
    assert hash_table_chained.get(10, 1) != False
    assert hash_table_chained.get(33, 1) == 30
    assert hash_table_chained.get(33, 1) != False
    assert hash_table_chained.get(40, 1) == False

def test_delete_key():
    hash_table_chained = HashTableC(60)
    hash_table_chained.put(10, 6, 1)
    hash_table_chained.put(33, 30, 1)
    assert hash_table_chained.delete(10, 1) == 'The element was successfully deleted'
    assert hash_table_chained.delete(10, 1) == 'Key was not found'
    assert hash_table_chained.delete(10, 1) != 'Delete Error'
    assert hash_table_chained.delete(33, 1) == 'The element was successfully deleted'
    assert hash_table_chained.delete(33, 1) == 'Key was not found'
    assert hash_table_chained.delete(33, 1) != 'Delete Error'
    assert hash_table_chained.delete(2, 1) == 'Key was not found'

def test_delete_all_hash():
    hash_table_chained = HashTableC(60)
    hash_table_chained.put(10, 6, 1)
    hash_table_chained.put(33, 30, 1)
    hash_table_chained.delete_all()
    assert hash_table_chained.size == 0

def test_hash_functions():
    assert hash_function_ost(10, 89) == 10
    assert hash_function_ost(10, 5) == 0
    assert hash_fun_additive(14, 50) == 5
    assert hash_fun_additive(10, 5) == 1
    assert hash_fun_square(4) == 6
    assert hash_fun_square(7) == 9





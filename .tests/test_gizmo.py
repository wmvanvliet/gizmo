def test_ex1():
    """Ex1: create a module called gizmo"""
    import gizmo  # noqa

def test_ex2():
    """Ex2: create a class called Gizmo"""
    import gizmo
    assert type(gizmo.Gizmo) == type

def test_ex3():
    """Ex3: create a constructor for Gizmo"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert type(g) == gizmo.Gizmo
    assert g.name == 'Frankfurter'

def test_ex4(capsys):
    """Ex4: let Gizmo say its name"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'speak')
    assert g.speak
    g.speak()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Frankfurter'

def test_ex5(capsys):
    """Ex5: add a property to the Gizmo class"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'friendship_name')
    assert g.friendship_name == 'Retrufknarf'
    g.name = 'Test'
    assert g.friendship_name == 'Tset'

def test_ex10():
    """Ex10: Add a NumPy array"""
    import numpy as np
    from numpy.testing import assert_equal
    import gizmo
    assert hasattr(gizmo, 'multiplication_table')
    assert hasattr(gizmo.multiplication_table, '__call__')
    prod_table = gizmo.multiplication_table()
    assert type(prod_table) == np.ndarray
    ref_table = np.outer(np.arange(1, 13), np.arange(1, 13))
    assert_equal(prod_table, ref_table)

def test_ex11():
    """Ex11: Numpy fancy indexing"""
    import numpy as np
    from numpy.testing import assert_equal
    import gizmo
    assert hasattr(gizmo, 'multiplication_table')
    assert hasattr(gizmo.multiplication_table, '__call__')
    prod_table = gizmo.multiplication_table()
    assert type(prod_table) == np.ndarray
    ref_table = np.outer(np.arange(1, 13), np.arange(1, 13))
    assert_equal(prod_table, ref_table)

    # Test zero_out_multiples parameter
    assert_equal(prod_table, gizmo.multiplication_table(None))
    prod_table_without_3 = gizmo.multiplication_table(zero_out_multiples=3)
    assert type(prod_table_without_3) == np.ndarray
    ref_table_without_3 = ref_table.copy()
    ref_table_without_3[ref_table_without_3 % 3 == 0] = 0
    assert_equal(prod_table_without_3, ref_table_without_3)

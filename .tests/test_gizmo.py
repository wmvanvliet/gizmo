def test_ex1():
    """Ex1: Create a module called gizmo"""
    import gizmo  # noqa

def test_ex2(capsys):
    """Ex2: Create a function"""
    import gizmo
    assert hasattr(gizmo, 'hello')
    assert gizmo.hello
    gizmo.hello('Gizmo', 'Germany')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello Gizmo, how are things in Germany?'
    gizmo.hello('Gizmo')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello Gizmo, how are things in Finland?'
    gizmo.hello('foo', 'bar')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello foo, how are things in bar?'
    gizmo.hello('foo')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello foo, how are things in Finland?'

def test_ex3(capsys):
    """Ex3: Use a loop"""
    import gizmo
    assert hasattr(gizmo, 'spell')
    assert gizmo.spell
    gizmo.spell('Frankfurter')
    captured = capsys.readouterr()
    assert captured.out.strip() == "F.r.a.n.k.f.u.r.t.e.r"

def test_ex4():
    """Ex4: Use string formatting"""
    import gizmo
    subjects = ['subj1', 'subj2']
    flist = gizmo.relative_path(subjects)
    assert flist[0] == "./subjects/mock_recording_subj1.rec"
    assert flist[1] == "./subjects/mock_recording_subj2.rec"
    subjects = ['subj1', 'subj2', 'subj3', 'subj4']
    flist = gizmo.relative_path(subjects)
    assert flist[0] == "./subjects/mock_recording_subj1.rec"
    assert flist[1] == "./subjects/mock_recording_subj2.rec"
    assert flist[2] == "./subjects/mock_recording_subj3.rec"
    assert flist[3] == "./subjects/mock_recording_subj4.rec"

def test_ex5():
    """Ex5: Create a class"""
    import gizmo
    assert type(gizmo.Gizmo) == type

def test_ex6():
    """Ex6: Add an attribute to your class"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert type(g) == gizmo.Gizmo
    assert g.name == 'Frankfurter'

def test_ex7(capsys):
    """Ex7: Add a method to your class"""
    import gizmo
    g = gizmo.Gizmo('Frankfurter')
    assert hasattr(g, 'speak')
    assert g.speak
    g.speak()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Frankfurter'

def test_ex8():
    """Ex8: Add a NumPy array"""
    import numpy as np
    from numpy.testing import assert_equal
    import gizmo
    assert hasattr(gizmo, 'multiplication_table')
    assert hasattr(gizmo.multiplication_table, '__call__')
    prod_table = gizmo.multiplication_table()
    assert type(prod_table) == np.ndarray
    ref_table = np.outer(np.arange(1, 13), np.arange(1, 13))
    assert_equal(prod_table, ref_table)

def test_ex9():
    """Ex9: Use Numpy's fancy indexing"""
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

def test_ex10():
    """Ex10: Document your function using numpydoc"""
    from numpydoc.docscrape import FunctionDoc
    import gizmo
    assert hasattr(gizmo, 'multiplication_table')
    assert hasattr(gizmo.multiplication_table, '__doc__')
    doc = FunctionDoc(gizmo.multiplication_table)
    assert doc['Summary'] != ''
    assert doc['Extended Summary'] != ''
    assert len(doc['Parameters']) == 1
    assert doc['Parameters'][0].name != ''
    assert doc['Parameters'][0].type != ''
    assert doc['Parameters'][0].desc != ''
    assert len(doc['Returns']) == 1
    assert doc['Returns'][0].name != ''
    assert doc['Returns'][0].type != ''
    assert doc['Returns'][0].desc != ''

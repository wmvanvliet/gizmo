import pytest


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
    import inspect
    assert hasattr(gizmo, 'spell')
    assert gizmo.spell
    code = inspect.getsource(gizmo.spell)
    if 'split' in code or 'join' in code:
        raise RuntimeError('No split() or join() allowed')
    if 'for' not in code:
        raise RuntimeError('Use a for-loop to solve this exercise')
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
    """Ex8: Build a generator"""
    import gizmo
    assert hasattr(gizmo, 'generate_fibonacci_sequence')
    assert hasattr(gizmo.generate_fibonacci_sequence, '__call__')
    assert list(gizmo.generate_fibonacci_sequence(0)) == []
    assert list(gizmo.generate_fibonacci_sequence(1)) == [0]
    assert list(gizmo.generate_fibonacci_sequence(2)) == [0, 1]
    assert list(gizmo.generate_fibonacci_sequence(3)) == [0, 1, 1]
    first10 = list(gizmo.generate_fibonacci_sequence(10))
    assert first10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    first100 = list(gizmo.generate_fibonacci_sequence(100))
    assert first100 == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
        2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
        317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
        14930352, 24157817, 39088169, 63245986, 102334155, 165580141,
        267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073,
        4807526976, 7778742049, 12586269025, 20365011074, 32951280099,
        53316291173, 86267571272, 139583862445, 225851433717, 365435296162,
        591286729879, 956722026041, 1548008755920, 2504730781961,
        4052739537881, 6557470319842, 10610209857723, 17167680177565,
        27777890035288, 44945570212853, 72723460248141, 117669030460994,
        190392490709135, 308061521170129, 498454011879264, 806515533049393,
        1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757,
        8944394323791464, 14472334024676221, 23416728348467685,
        37889062373143906, 61305790721611591, 99194853094755497,
        160500643816367088, 259695496911122585, 420196140727489673,
        679891637638612258, 1100087778366101931, 1779979416004714189,
        2880067194370816120, 4660046610375530309, 7540113804746346429,
        12200160415121876738, 19740274219868223167, 31940434634990099905,
        51680708854858323072, 83621143489848422977, 135301852344706746049,
        218922995834555169026
    ]
    with pytest.raises(StopIteration):
        next(gizmo.generate_fibonacci_sequence(0))


#def test_ex9():
#    """Ex9: Document your function using numpydoc"""
#    from numpydoc.docscrape import FunctionDoc
#    import gizmo
#    assert hasattr(gizmo, 'generate_fibonacci_sequence')
#    assert hasattr(gizmo.generate_fibonacci_sequence, '__doc__')
#    doc = FunctionDoc(gizmo.generate_fibonacci_sequence)
#    assert doc['Summary'] != ''
#    assert doc['Extended Summary'] != ''
#    assert len(doc['Parameters']) == 1
#    assert doc['Parameters'][0].name != ''
#    assert doc['Parameters'][0].type != ''
#    assert doc['Parameters'][0].desc != ''
#    assert len(doc['Yields']) == 1
#    assert doc['Yields'][0].name != ''
#    assert doc['Yields'][0].type != ''
#    assert doc['Yields'][0].desc != ''

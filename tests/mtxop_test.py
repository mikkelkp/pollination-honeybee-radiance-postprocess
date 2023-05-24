from pathlib import Path
from shutil import rmtree

from pollination.honeybee_radiance_postprocess.mtxop import OperateTwo, \
    OperateThree

from queenbee.plugin.function import Function


def test_operatre_two():
    function = OperateTwo()
    qb_function = function.queenbee
    assert qb_function.name == 'operate-two'
    assert isinstance(qb_function, Function)


def test_operate_two_default():
    function = OperateTwo()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sun.ill')
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_two_operator():
    function = OperateTwo()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sun.ill'),
        'operator': '*'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_two_ascii():
    function = OperateTwo()
    inputs = {
        'first_mtx': Path('./tests/assets/ascii/sky.ill'),
        'second_mtx': Path('./tests/assets/ascii/sun.ill'),
        'binary': 'ascii'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_two_conversion():
    function = OperateTwo()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sun.ill'),
        'conversion': '47.4 119.9 11.6'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operatre_three():
    function = OperateThree()
    qb_function = function.queenbee
    assert qb_function.name == 'operate-three'
    assert isinstance(qb_function, Function)


def test_operate_three_default():
    function = OperateThree()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sky_dir.ill'),
        'third_mtx': Path('./tests/assets/binary/sun.ill')
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_three_operator():
    function = OperateThree()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sky_dir.ill'),
        'third_mtx': Path('./tests/assets/binary/sun.ill'),
        'operator-one': '-',
        'operator-two': '+'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_three_ascii():
    function = OperateThree()
    inputs = {
        'first_mtx': Path('./tests/assets/ascii/sky.ill'),
        'second_mtx': Path('./tests/assets/ascii/sky_dir.ill'),
        'third_mtx': Path('./tests/assets/ascii/sun.ill'),
        'binary': 'ascii'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)


def test_operate_three_conversion():
    function = OperateThree()
    inputs = {
        'first_mtx': Path('./tests/assets/binary/sky.ill'),
        'second_mtx': Path('./tests/assets/binary/sky_dir.ill'),
        'third_mtx': Path('./tests/assets/binary/sun.ill'),
        'conversion': '47.4 119.9 11.6'
    }
    folder = Path('./tests/assets/temp')
    output_file = folder.joinpath('output.npy')
    if not folder.exists():
        folder.mkdir(parents=True)
    function._try(inputs, folder=folder)
    assert output_file.is_file()

    for path in folder.glob('*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)

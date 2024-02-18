import shutil
from unittest import TestCase
import filecmp
import os.path

class dircmp(filecmp.dircmp):
    """
    Compare the content of dir1 and dir2. In contrast with filecmp.dircmp, this
    subclass compares the content of files with the same path.
    """
    def phase3(self):
        """
        Find out differences between common files.
        Ensure we are using content comparison with shallow=False.
        """
        fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files,
                                 shallow=False)
        self.same_files, self.diff_files, self.funny_files = fcomp

def is_same(dir1, dir2):
    """
    Compare two directory trees content.
    Return False if they differ, True is they are the same.
    """
    import glob
    for f1 in glob.glob(dir1+"/**/*.*"):
        rp = os.path.relpath(f1, dir1)
        f2 = dir2 + "/"+rp

        with open(f1, 'r') as f:
            s1 = f.read()
        with open(f2, 'r') as f:
            s2 = f.read()

        if s1 != s2:
            print("*"*50)
            print(f1)
            print(s1)
            print("-"*5)
            print(s2)
            return False

    compared = dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files
        or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True


dir = os.path.dirname(__file__)

class TestPython(TestCase):
    def test_demo1(self):
        # return
        from setup_test_files import setup, setup_keep
        setup(dir+"/demo1", dir+"/demo1_tmp")
        report = filecmp.dircmp(dir+"/demo1_correct", dir+"/demo1_tmp")
        print("Different", report.report())
        self.assertTrue(is_same(dir+"/demo1_correct", dir+"/demo1_tmp"))

    def test_demo2(self):
        # return
        from setup_test_files import setup, setup_keep
        setup_keep(dir+"/demo2/framework.py", dir+"/demo2/framework_tmp.txt")
        with open(dir+"/demo2/framework_tmp.txt") as f:
            tmp = f.read()

        with open(dir+"/demo2/framework_correct.txt") as f:
            correct = f.read()

        self.assertEqual(tmp, correct)


def snipit(code, dest):
    # base = os.path.dirname(__file__)
    dest = os.path.abspath(dest)

    if not os.path.isdir(d_ := os.path.dirname(dest)):
        os.makedirs(d_)
    with open(dest, 'w') as f:
        f.write(code)

    # if os.path.isdir(dest):
    #     shutil.rmtree(dest)
    # os.mkdir(dest)
    # os.mkdir(dest + "/output")
    from snipper import snip_dir
    dest_dir = d_ +"/dest"
    odir =d_ + "/output"
    if os.path.isdir(odir):
        shutil.rmtree(odir)
    os.makedirs(odir)
    import glob
    snap = snip_dir(d_, dest_dir=dest_dir, clean_destination_dir=True, output_dir=odir)
    rs = {}
    for f in glob.glob(odir + "/*"):
        with open(f, 'r') as ff:
            rs[os.path.basename(f)] = trim(ff.read())
    return rs

def trim(s):
    # s.rstrip()
    return "\n".join( [l.rstrip() for l in s.rstrip().splitlines()] )



def process_blocks(blocks):
    pass

class TestError(TestCase):
    def test_error(self):
        example = """
#!i
s = (1, 2)
s[0] = 1
#!i
"""
        if os.path.isdir("tmp"):
            shutil.rmtree("tmp")
        rs = snipit(example, "tmp/code.py")
        print(rs['code.shell'])
        # print(rs['code_a.shell'])
        def mcmp(a, b):
            if a == b:
                self.assertEqual(a,b)
            else:
                aa = a.splitlines()
                bb = b.splitlines()
                self.assertEqual(len(aa), len(bb), msg="wrong number of lines")
                for a_, b_ in zip(aa, bb):
                    if a_ != b_:
                        print("not the same")
                        print(a_)
                        print(b_)
                    self.assertEqual(a_, b_)
            self.assertEqual(a,b)

        mcmp(rs['code.shell'], """
>>> s = (1, 2)
>>> s[0] = 1
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment        
        """.strip())




class TestInteractiveMode(TestCase):
    def test_snip(self):
        example = """
#!i
print("i=23")        
#!i

#!i=a
for i in range(2):
    print(i)

#!i=a

#!i=c
print("hello")
a = 234
#!i=c

        """
        if os.path.isdir("tmp"):
            shutil.rmtree("tmp")
        rs = snipit(example, "tmp/code.py")

        # print(rs['code_a.shell'])

        self.assertEqual(rs['code.shell'], """>>> print("i=23")
i=23""")
        b = trim(""">>> for i in range(2):
...     print(i)
...
0
1""")

        self.assertEqual(rs['code_a.shell'],""">>> for i in range(2):
...     print(i)
...
0
1""")

        self.assertEqual(rs['code_c.shell'], """>>> print("hello")
hello
>>> a = 234""")
        return
        # import code
        # ita = code.interact()

        import sys
        from code import InteractiveInterpreter, InteractiveConsole
        # from snipper.snip_dir import
        console = InteractiveInterpreter()
        source = ""

        cc = InteractiveConsole()

        def _runblock(console, block):
            source_lines = (line.rstrip() for line in block)
            # console = InteractiveInterpreter()
            source = ""
            out = []
            try:
                while True:
                    source = next(source_lines)
                    # Allow the user to ignore specific lines of output.
                    if not source.endswith("# ignore"):
                        out.append(f">>> {source}")
                    more = console.runsource(source)
                    while more:
                        next_line = next(source_lines)
                        out.append(f"... {next_line}")
                        source += "\n" + next_line
                        more = console.runsource(source)
            except StopIteration:
                if more:
                    print("... ")
                    out.append("... ")
                    more = console.runsource(source + "\n")
        from snipper.block_parsing import full_strip
        # full_strip(example)
        ex2 = full_strip(example.splitlines(), ("#!i",) )

        # _runblock(console, ex2)

        # from contextlib import redirect_stdout
        # import io
        # f = io.StringIO()
        #
        # with redirect_stdout(f):
        #     print("hello world")
        # a = f.getvalue()
        #
        # s = redirect_stdout(f)
        # obj = s.__enter__()
        # print("hello")
        # s.__exit__()
        # f.getvalue()
        # print("\n".join( out['a'] ) )

        for k in out:
            # print("a:")
            print("".join( out[k] ) )
            print("-"*10)
        pass

        a = 234


        try:
            while True:
                source = next(source_lines)
                # Allow the user to ignore specific lines of output.
                if not source.endswith("# ignore"):
                    print(">>>", source)
                more = console.runsource(source)
                while more:
                    next_line = next(source_lines)
                    print("...", next_line)
                    source += "\n" + next_line
                    more = console.runsource(source)
        except StopIteration:
            if more:
                print("... ")
                more = console.runsource(source + "\n")

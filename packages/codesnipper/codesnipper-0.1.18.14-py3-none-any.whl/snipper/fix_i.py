import code
import traceback
import functools
import textwrap
from snipper.legacy import block_process
from snipper.block_parsing import full_strip
import sys
from snipper.block_parsing import block_split, block_join

import os
# if os.name == 'nt':
#     import wexpect as we
# else:
#     import pexpect as we

# def rsession(analyzer, lines, extra):
#     l2 = []
#     dbug = False
#     # analyzer = we.spawn("python", encoding="utf-8", timeout=20)
#     # analyzer.expect([">>>"])
#     if "b = make_square(5)" in "\n".join(lines): # in "\n".join(lines):
#         print("\n".join(lines))
#         print("-"*50)
#         for k in extra['session_results']:
#             print(k['input'])
#             print(k['output'])
#
#         import time
#         an = we.spawn(sys.executable, encoding="utf-8", timeout=20)
#         try:
#             an.setwinsize(400, 400) # set window size to avoid truncated output or input.
#         except AttributeError as e:
#             print("> Mulble pexpect('pyhon',...) does not support setwinsize on this system (windows?). Ignoring")
#
#         an.expect([">>>"])
#         l3 = """
# 2 + 4 # Add two integers
# 50 - 5 * 6
# (2 + 2) * (3 - 1) # You can group operations using parenthesis
# width = 20 # Assign the variable 'width' to a value of 20
# height = 5*9 # And also height is assigned the value of 5 * 9 = 45
# area = 2*3 # Compute the area of a rectangle and assign it to area now the text will be longer is that an issue
# area # This line shows us the value of 'area' #!i=b
# """
#         lines2 = l3.strip().splitlines()
#         from collections import defaultdict
#         dd = defaultdict(list)
#
#         for l in lines2:
#             dd['code'].append(l)
#             an.sendline(l.rstrip())
#             an.expect_exact([">>>", "..."])
#             dd["output"].append(an.before.strip())
#             # print(">>>", an.before.strip())
#             if len(an.after.strip()) > 4:
#                 print(">>>>>>>>>>>>> That was a long after?")
#             # analyzer.be
#
#         print('*' * 50)
#         # analyzer = an
#         dbug = True
#         import tabulate
#         print(tabulate.tabulate(dd, headers='keys'))
#
#     lines = "\n".join(lines).replace("\r", "").splitlines()
#
#     for i, l in enumerate(lines):
#         l2.append(l)
#         if l.startswith(" ") and i < len(lines)-1 and not lines[i+1].startswith(" "):
#             if not lines[i+1].strip().startswith("else:") and not lines[i+1].strip().startswith("elif") :
#                 l2.append("") # Empty line instead?
#
#     lines = l2
#     alines = []
#     in_dot_mode = False
#     if len(lines[-1]) > 0 and (lines[-1].startswith(" ") or lines[-1].startswith("\t")):
#         lines += [""]
#
#
#     for i, word in enumerate(lines):
#         if dbug:
#             print("> Sending...", word)
#         analyzer.sendline(word.rstrip())
#         import time
#         before = ""
#         while True:
#             time.sleep(0.05)
#             analyzer.expect_exact([">>>", "..."])
#             # if dbug and "total_cost" in word:
#             #     aaa = 23234
#             before += analyzer.before
#             # if dbug:
#             # print(">  analyzer.before...", analyzer.before.strip(), "...AFTER...", analyzer.after.strip())
#             # AFTER =
#             if analyzer.before.endswith("\n"):
#                 # print("> BREAKING LOOP")
#                 break
#             else:
#                 before += analyzer.after
#             break
#
#         # print("Before is", before)
#         abefore = analyzer.before.rstrip()
#         # Sanitize by removing garbage binary stuff the terminal puts in
#         abefore = "\n".join([l for l in abefore.splitlines() if not l.startswith('\x1b')] )
#
#         dotmode = analyzer.after == "..."
#         if 'dir(s)' in word:
#             pass
#         if 'help(s.find)' in word:
#             pass
#         if dotmode:
#             alines.append(">>>" +abefore.rstrip() if not in_dot_mode else "..." + abefore.rstrip())
#             in_dot_mode = True
#         else:
#             alines.append( ("..." if in_dot_mode else ">>>") + abefore.rstrip())
#             in_dot_mode = False
#     if dbug:
#         print("-"*50)
#         print("\n".join(alines))
#     extra['session_results'].append({'input': '\n'.join(lines), 'output': '\n'.join(alines)})
#     return alines


def run_i(lines, file, output):
    return new_run_i(lines, file, output)
    # return
    #
    # if 'python0A' in str(file):
    #     print(234)
    # extra = dict(python=None, output=output, evaluated_lines=0, session_results=[])
    # def block_fun(lines, start_extra, end_extra, art, head="", tail="", output=None, extra=None):
    #     outf = output + ("_" + art if art is not None and len(art) > 0 else "") + ".shell"
    #     lines = full_strip(lines)
    #     s = "\n".join(lines)
    #     s.replace("...", "..") # passive-aggressively truncate ... because of #issues.
    #     lines = textwrap.dedent(s).strip().splitlines()
    #     # an.setecho(True) # TH January 2023: Seems to fix an issue on linux with truncated lines. May cause problems on windows?
    #
    #     if extra['python'] is None:
    #         an = we.spawn(sys.executable, encoding="utf-8", timeout=20)
    #         try:
    #             an.setwinsize(400, 400)  # set window size to avoid truncated output or input.
    #         except AttributeError as e:
    #             print("> Mulble pexpect('pyhon',...) does not support setwinsize on this system (windows?). Ignoring")
    #
    #         an.expect([">>>"])
    #         extra['python'] = an
    #
    #     # analyzer = extra['python']
    #     # What does this do?
    #     # for l in (head[extra['evaluated_lines']:] + ["\n"]):
    #     #     analyzer.sendline(l)
    #     #     analyzer.expect_exact([">>>", "..."])
    #     alines = rsession(extra['python'], lines, extra) # give it the analyzer
    #     extra['evaluated_lines'] += len(head) + len(lines)
    #     lines = alines
    #     return lines, [outf, lines]
    # try:
    #     a,b,c,_ = block_process(lines, tag="#!i", block_fun=functools.partial(block_fun, output=output, extra=extra))
    #     if extra['python'] is not None:
    #         extra['python'].close()
    #
    #     if len(c)>0:
    #         kvs= { v[0] for v in c}
    #         for outf in kvs:
    #             out = "\n".join( ["\n".join(v[1]) for v in c if v[0] == outf] )
    #             out = out.replace("\r", "")
    #             # if outf.endswith("python0B_e4.shell"):
    #             #     print(outf)
    #
    #             with open(outf, 'w') as f:
    #                 f.write(out)
    #
    # except Exception as e:
    #     print("lines are")
    #     print("\n".join(lines))
    #     print("Bad thing in #!i command in file", file)
    #     raise e
    # return lines

class FileConsole(code.InteractiveConsole):
    """Emulate python console but use file instead of stdin
    See https://tdhock.github.io/blog/2021/python-prompt-commands-output/
    """
    def __init__(self, *args, lines=None, **kwargs):
        super().__init__(*args, **kwargs)
        # self.lines = lines.splitlines()
        # self.output = {'a': []}
        pass

    def raw_input(self, prompt):
        while True:
            if len(self.blocks) == 0:
                raise EOFError
            k = next(self.blocks.__iter__())
            self.k = k
            if len(self.blocks[k]) == 0:
                self.output[self.k].append(self.f.getvalue().rstrip())
                self.f.truncate(0)
                self.f.seek(0)
                del self.blocks[k]
            else:
                line = self.blocks[k].pop(0)
                break
        # if line == "":
        #     raise EOFError()
        # print(prompt, line.replace("\n", ""))
        sval = self.f.getvalue()
        if sval != '':
            self.output[self.k].append(self.f.getvalue())
            self.f.truncate(0)
            self.f.seek(0)
        # self.f.
        o_ = prompt.replace("\n", "") + (" " if prompt != "... " else "") + line +"\n"
        # print(o_)
        self.output[self.k].append(o_)
        # print(line)

        return line

    def write(self, str):
        print(str)
        pass

        # self.output[self.k].append(str)
    # def showtraceback(self):
    #     """Display the exception that just occurred.
    #
    #     We remove the first stack item because it is our own code.
    #
    #     The output is written by self.write(), below.
    #
    #     """
    #     sys.last_type, sys.last_value, last_tb = ei = sys.exc_info()
    #     sys.last_traceback = last_tb
    #     try:
    #         lines = traceback.format_exception(ei[0], ei[1], last_tb.tb_next)
    #         if sys.excepthook is sys.__excepthook__:
    #             self.write(''.join(lines))
    #         else:
    #             # If someone has set sys.excepthook, we let that take precedence
    #             # over self.write
    #             sys.excepthook(ei[0], ei[1], last_tb)
    #     finally:
    #         last_tb = ei = None

    def run_blocks(self, blocks):
        from collections import defaultdict
        self.blocks = {k: v.splitlines() for k, v in blocks.items()}
        self.output = defaultdict(list)
        self.k = "startup"
        from contextlib import redirect_stdout
        import io
        self.f = io.StringIO()
        eh = sys.excepthook
        sys.excepthook = sys.__excepthook__

        try:

            with redirect_stdout(self.f):
                # print("hello world")
                self.interact()
        except Exception as e:
            print("Snipper encountered a fatal problem. ")
            print("I was processing")
            print(blocks)
            print("And encountered", e)
            raise e
        finally:
            sys.excepthook = eh

        return self.output


def new_run_i(lines, file, output):
    # Create a database of all output.
    # cutouts = []
    l0 = lines
    cutouts = {}
    # id = ""
    while True:
        b = block_split(lines, tag="#!i")
        if b == None:
            break
        # id = b['arg1']
        art = b['name']
        outf = output + ("_" + art if art is not None and len(art) > 0 else "") + ".shell"
        # print(outf)
        # id = os.path.basename(outf)
        cutouts[os.path.basename(outf)] = {'first': b['first'], 'block': b['block'], 'last': []}
        lines = b['last']
        #
        # continue
        # args = {k: v for k, v in b['start_tag_args'].items() if len(k) > 0}
        # cutout.append(b['block'])
        # b['block'], dn = _block_fun(b['block'], start_extra=b['arg1'], end_extra=b['arg2'], **args, keep=keep)
        # # cutout += b['block']
        # # method = b['start_tag_args'].get('', 'remove')
        # # b['block'], dn = _block_fun(b['block'], start_extra=b['arg1'], end_extra=b['arg1'], **args, keep=keep)
        # lines = block_join(b)
        # # cutout +_=
        # n += dn
    # if len(cutouts) > 0:
    #     cutouts[id]['last'] = lines
    if len(cutouts) == 0:
        return
    import sys

    def run_code_blocks(blocks):
        # p_ = sys.ps1
        try:
            sys.ps1 = ">>>"
            fc = FileConsole()
            out = fc.run_blocks(blocks)
        except Exception as e:
            raise e
        finally:
            pass
            # sys.ps1 = p_
        return out

    blks = {}
    for id, block in cutouts.items():
        dx = min( [k for k, l in enumerate(block['block']) if len(l.strip()) != 0] )
        blks[id +"_pre"] = "\n".join( block['first'] + block['block'][:dx] )
        blks[id] = "\n".join(block['block'][dx:])


    out = run_code_blocks(blks)

    for id in cutouts:
        # print("-"*5, id, "-"*5)
        # print("".join(out[id]))
        with open(f"{os.path.dirname(output)}/{id}", 'w') as f:
            f.write("".join(out[id]))
    return l0

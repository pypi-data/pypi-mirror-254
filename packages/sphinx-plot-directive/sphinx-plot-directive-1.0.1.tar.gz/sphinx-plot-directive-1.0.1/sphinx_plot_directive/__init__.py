# -*- coding: utf-8 -*-
"""
    sphinx-plot-directive
    ~~~~~~~~~~~~~~~~~~~~~

    An extension providing a reStructuredText directive .. plot:: for including a plot in a Sphinx document.

    See the README file for details.

    :author: Yongping Guo <guoyoooping@163.com>
    :license: MIT
"""

import re, os, sys
import posixpath
from os import path
import shutil
import copy
from subprocess import Popen, PIPE
from PIL import Image
import shlex
import imghdr

try:
    # Python 2.
    from StringIO import StringIO
    # Python 3.
except ImportError:
    from io import StringIO

try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.errors import SphinxError
from sphinx.util import ensuredir, relative_uri

OUTPUT_DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None)
OWN_OPTION_SPEC = dict( {
    'caption': str,
    'size': str,
    'plot_format': str,
    'annotate': str,
    'show_source': str,
    'hidden': str,
    'latex_show_max_png': int,
    #'background': str,
    })

def plot_image (app, plot):
    '''
    always plot it in this function, should check if the target exists before calling me.
    '''
    if app.builder.config.plot_log_level > 1:
        print("%s(), plot is:" %(sys._getframe().f_code.co_name))
        for k,v in plot.items():
            print("    %s: %s" %(k, v))
    cmd = plot['cmd']
    args = shlex.split(cmd)
    text = plot['text']
    options = plot['total_options']
    rel_imgpath = relative_uri(app.builder.env.docname, app.builder.imagedir)
    hashkey = str(cmd) + str(options) + str(plot['text'])
    hashkey = sha(hashkey.encode('utf-8')).hexdigest()
    infname = '%s-%s.%s' % (args[0], hashkey, plot['directive'])
    infullfn = path.join(app.builder.outdir, app.builder.imagedir, infname)
    ensuredir(path.join(app.builder.outdir, app.builder.imagedir))
    #Record the current dir and return here afterwards
    currpath = os.getcwd()
    #plot_format option must be set before.
    plot_format = options.get("plot_format", None)
    outfname = '%s-%s.%s' %(args[0], hashkey, plot_format)
    out = dict(outrelfn = posixpath.join(rel_imgpath, outfname),
        outfullfn = path.join(app.builder.outdir,
            app.builder.imagedir, outfname),
        outreference = None)

    #print("cmd: %s" %(cmd))
    if "ditaa" in cmd:
        if (not options.get("annotate", None)):
            #to support Chinese, draw it always with --svg.
            args.insert(1, "--svg")
        args.extend([infname, outfname])
        # Ditaa must work on the target directory.
        os.chdir(os.path.dirname(out["outfullfn"]))
    elif "seqdiag" in cmd or "blockdiag" in cmd \
            or "actdiag" in cmd or "nwdiag" in cmd:
        #seqdiag ... etc, only support svg, convert it to pdf automatically.
        if (plot_format in ["svg", "pdf"]) and ("-Tsvg" not in cmd):
            #ditaa support vector output by --svg parameter.
            args.insert(1, "-Tsvg")
            os.chdir(os.path.dirname(out["outfullfn"]))
        args.extend([infname, '-o', outfname])
    elif args[0] == "dot":
        # dot -Tpng in_file -o out_file
        args.extend([infullfn, '-o', out["outfullfn"]])
    elif "python" in args[0]:
        pylib = "pyplot"
        lines = StringIO(text).readlines()
        for l in lines:
            if (not l.lstrip().startswith('#')) and \
                    ("import matplotlib.pyplot" in l):
                # Find out pyplot module name, use pyplot if not found.
                result = re.search("(?<=import matplotlib.pyplot as )\w+",
                        l, flags=0)
                pylib = result and result.group() or "pyplot"
            elif ('.show()' in l or 'savefig(' in l):
                lines.remove(l)
        lines.append('%s.savefig("%s")\n' %(pylib, out["outfullfn"]))
        text = ''.join(lines)
        args.append(infullfn)
    elif args[0] == "gnuplot":
        size = options.get("size", "900,600")
        if (plot_format in ["pdf", "eps"]):
            # pdf unit is inch while png is pixel, convert them.
            size = ",".join("%d" %(int(i.strip())/100) for i in size.split(","))
        lines = StringIO(text).readlines()
        # Remove the lines with set output/set terminal
        lines = [l for l in lines if (not re.search("^[^#]*set\s+output",
            l, flags=0)) and (not re.search("^[^#]*set\s+term", l, flags=0))]
        lines.insert(0, 'set output "%s"\n' %(out["outfullfn"]))
        terminal = (plot_format == "png") and "pngcairo" or plot_format
        lines.insert(0, 'set terminal %s size %s\n' %(terminal, size))
        text = ''.join(lines)
        args.append(infullfn)
    elif args[0] in ["convert", "magick", "montage"]:
        #magick is the same as convert
        tmp = []
        #print("debug, args: %s" %(args))
        if text:
            args = ["sh", infullfn]
        else:
            #Only have command and not body: call args directly.
            args[-1] = out["outfullfn"]
            text = " ".join(args)
            #args = ["sh", infullfn]
    else:
        args.append(infullfn)

    # write the text as infile.
    with open(infullfn, 'wb') as f:
        f.write(text.encode('utf-8'))

    # 2) generate the output file
    try:
        print(' '.join(args))
        p = Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout, stderr = (p.stdout.read().decode("utf-8"),
                p.stderr.read().decode("utf-8"))
        if stderr and stdout:
            print("[31m%s[1;30m%s[0m" %(stderr, stdout))
    except OSError as err:
        os.chdir(currpath)
        raise PlotError('[1;31m%s[0m' %(err))

    if options.get("annotate", None):
        # We'd like to add annotate on the output.
        c = "convert %s" %(out["outfullfn"])
        for i in StringIO(options["annotate"]).readlines():
            if (i.lstrip()[0] != "#"):
                c += " %s" %(i.strip().rstrip("\\"))
        c += " %s" %(out["outfullfn"])
        print(c)
        os.system(c)

    #print("arg[0]: %s, plot_format: %s, format: %s"
    #        %(args[0], plot_format, app.builder.format))
    if cmd in ["convert", "magick", "montage"]:
        #Get the last word as the original output name

        #print("text: %s" %(text))
        for i in reversed(StringIO(text).readlines()):
            if i and (not (i.lstrip().startswith('#'))):
                conver_outfile = i.split()[-1]
                break
        if (app.builder.format == "latex") and \
                (conver_outfile.split(".")[-1] == "gif"):
            if options.get("latex_show_max_png", 0) and \
                    os.path.splitext(out["outfullfn"])[-1] in [".gif"]:
                i = Image.open(conver_outfile)
                #n = list(ImageSequence.Iterator(i)).size()
                max_num = (i.n_frames > options["latex_show_max_png"]) \
                        and options["latex_show_max_png"] or i.n_frames
                #print("i: %d, max_num: %d"  %(i.n_frames, max_num))
                print("montage %s[0-%d] -coalesce -tile %d %s" 
                        %(conver_outfile, max_num - 1,
                            pow(max_num, 0.5), out["outfullfn"]))
                os.system("montage %s[0-%d] -coalesce -tile %d %s" 
                        %(conver_outfile, max_num - 1,
                            pow(max_num, 0.5), out["outfullfn"]))
                if max_num < i.n_frames:
                    os.system("convert %s -gravity southeast -annotate +0+0 '...' %s"
                            %(out["outfullfn"], out["outfullfn"]))

                os.system("rm %s" %(conver_outfile))
            else:
                print("convert %s[0] %s" 
                        %(conver_outfile, out["outfullfn"]))
                os.system("convert %s[0] %s" 
                        %(conver_outfile, out["outfullfn"]))
                os.system("rm %s" %(conver_outfile))
        else:
            print("mv %s %s" %(conver_outfile, out["outfullfn"]))
            os.system("mv %s %s" %(conver_outfile, out["outfullfn"]))
    elif (args[0] in ["ditaa", "dot", "seqdiag", "blockdiag", "actdiag", \
        "nwdiag"]) and (plot_format in ['pdf']):
        # In fact ditaa don't support pdf, we convert the .svg to .pdf inkscape
        if (args[0] == "dot"):
            print("mv %s %s-%s.svg" %(out["outfullfn"], args[0], hashkey))
            os.system("mv %s %s-%s.svg" %(out["outfullfn"], args[0], hashkey))
        else:
            print("mv %s %s-%s.svg" %(outfname, args[0], hashkey))
            os.system("mv %s %s-%s.svg" %(outfname, args[0], hashkey))

        inkscape = os.system("which inkscape 2> /dev/null")
        if inkscape != 0:
            print('[1;31minkscape does not exist, isntall it at first[0m')
        inkscape = os.popen("inkscape --version | awk  '{print $2}'") 
        #print(int(inkscape.read().split(".")[0]))
        if (int(inkscape.read().split(".")[0], 10) >= 1):
            print("inkscape %s-%s.svg --export-type pdf -o %s"
                    %(args[0], hashkey, out["outfullfn"]))
            os.system("inkscape %s-%s.svg --export-type pdf -o %s"
                    %(args[0], hashkey, out["outfullfn"]))
        else:
            print("inkscape -f %s-%s.svg -A %s"
                    %(args[0], hashkey, out["outfullfn"]))
            os.system("inkscape -f %s-%s.svg -A %s"
                    %(args[0], hashkey, out["outfullfn"]))
    os.chdir(currpath)
    if app.builder.config.plot_log_level > 1:
        print("%s(), out is" %(sys._getframe().f_code.co_name))
        for k,v in out.items() :
            print("    %s: %s" %(k, v))

    return out

def cmd_2_image (app, plot):
    """
    1) 解析plot的内容
    2) 判断是不是已经做过。如果已经做过，直接返回结果，避免重复调用。
    3) 将解析的结果根据options加以处理
    Render plot code into a PNG output file.
    """
    if app.builder.config.plot_log_level > 0:
        print("%s() format: %s, docname: %s, imagedir: %s"
                %(sys._getframe().f_code.co_name,
                    app.builder.format,
                    app.builder.env.docname,
                    app.builder.imagedir))

    args = shlex.split(plot['cmd'])
    text = plot['text']
    options = plot['total_options']
    # Guess the suffix
    plot_format = "png"
    if "convert" in args or "magick" in args or "montage" in args:
        if app.builder.format in ["html"]:
            # We get the suffix of the last word not in the comments
            for i in reversed(StringIO(text).readlines()):
                if i and (not (i.lstrip().startswith('#'))):
                    plot_format = i.split(".")[-1]
                    break
        else:
            # for latex, it's alwyas png.
            plot_format = "png"
    elif "dot" in args:
        #dot
        found = False
        # Guess the plot_format if -TXXX is given
        for param in args:
            if "-T" in param:
                plot_format = param[2:]
                found = True
                break
        if (not found):
            # Set the plot_format to -TXXX
            plot_format = "png"
            args.append("-Tpng")
            plot['cmd'] = ' '.join(args)
        if (plot_format == "svg"):
            plot_format = (app.builder.format in ["latex"]) \
                    and "pdf" or plot_format
    elif options.get("plot_format", None):
        #User definition is higher priority.
        plot_format = options["plot_format"]
    elif options.get("annotate", None):
        # If options include annotate, only support png
        plot_format = "png"
    else:
        #default
        format_map = OUTPUT_DEFAULT_FORMATS.copy()
        format_map.update(app.builder.config.plot_output_format)
        plot_format = format_map.get(app.builder.format, "png")

    options["plot_format"] = plot_format
    hashkey = str(plot['cmd']) + str(options) + str(text)
    hashkey = sha(hashkey.encode('utf-8')).hexdigest()
    outfname = '%s-%s.%s' %(args[0], hashkey, plot_format)
    rel_imgpath = relative_uri(app.builder.env.docname, app.builder.imagedir)
    out = dict(outrelfn = posixpath.join(rel_imgpath, outfname),
        outfullfn = path.join(app.builder.outdir,
            app.builder.imagedir,
            outfname),
        outreference = None)
    if not path.isfile(out["outfullfn"]):
        out = plot_image(app, plot) # Really plot it
    else:
        print("file has already existed: %s" %(outfname))

    if options.get("show_source", False):
        out["outreference"] = posixpath.join(rel_imgpath, infname)

    if app.builder.config.plot_log_level > 1:
        print("%s(), out is" %(sys._getframe().f_code.co_name))
        for k,v in out.items() :
            print("    %s: %s" %(k, v))
    return out

class PlotError(SphinxError):
    category = 'plot error'

class PlotDirective(directives.images.Figure):
    """
    扫描文档时如果找到..plot:: 命令后建议一个空的figure对象，并且将.. plot::
    的内容保存在figure对象上。
    """
    has_content = True
    required_arguments = 0
    option_spec = directives.images.Figure.option_spec.copy()
    option_spec.update(OWN_OPTION_SPEC)

    def plot_param_parser(self, content, options):
        '''
        Given content and return the parsed dictionary:
        {"cmd": xxx, "text": xxx, "option": xxx, "total_options": xxx}
        '''
        tmp = ""
        for line in content:
            #Find the fist verb not starting with '#'
            if (line and (not line.lstrip().startswith('#'))):
                tmp = line.split()[0]
                if not options.get("caption", None):
                    #If no :caption: is given, take the 1st line as caption.
                    tmp_line = line.rstrip()
                    if tmp_line[-1] == "\\":
                        options["caption"] = tmp_line[:-1] + "..."
                    else:
                        options["caption"] = tmp_line
                break
        if (tmp in ["convert", "magick", "montage"]):
            #in case convert and montage: we put the cmd into the text itself
            cmd = tmp
            if len(content[0].split()) > 1:
                #所有的命令在命令行上
                text = '\n'.join(content)
            else:
                #命令行为convert, 所有的命令在内容里
                text = '\n'.join(content[1:])
        else:
            cmd = content[0]
            text = '\n'.join(content[1:])

        total_options = options.copy()
        own_options = dict([(k,v) for k,v in total_options.items() 
                                  if k in OWN_OPTION_SPEC])

        dic = dict(cmd=cmd,text=text,options=own_options,
                directive="plot", total_options=total_options)
        return dic
  
    def run(self):
        '''
        将.. plot:: 的内容和参数保存到figure对象的.plot成员里以备后用。
        '''
        self.arguments = ['']
        params = self.plot_param_parser(self.content, self.options)
        #for k,v in params.items() :
        #    print("PlotDirective.run(), %s: %s" %(k, v))

        # Remove the own options from self-options which will be as figure
        # options.
        for x in params["options"].keys():
            self.options.pop(x)
        # don't parse the centent as legend, it's not legend.
        self.content = None

        #Create a empty image or figure object from self.
        if ("alt" in params["total_options"].keys()):
            #If there is alt parameters then it's inline image
            (node,) = directives.images.Image.run(self)
        else:
            #Figure
            (node,) = directives.images.Figure.run(self)
        if isinstance(node, nodes.system_message):
            return [node]

        #node.plot = dict(cmd=cmd,text=text,options=own_options,
        #        directive="plot", total_options=total_options)
        node.plot = dict(**params)
        #print("PlotDirective.run(), note: %s" %(node))
        return [node]

# http://epydoc.sourceforge.net/docutils/
def doctree_read_callback(app, doctree):
    uris = dict();

    #第一次遍历，生成inline image
    for img in doctree.traverse(nodes.image):
        #For candidate
        if not hasattr(img, 'plot'):
            continue

        print("----------------------------------------------------------------")
        if app.builder.config.plot_log_level > 0:
            print("%s(), img plot cmd: %s, alt: %s"
                    %(sys._getframe().f_code.co_name,
                        (hasattr(img, 'plot')) and img.plot['cmd'] or None,
                        img.get('alt', None)))
        text = img.plot['text']
        options = img.plot['options']
        cmd = img.plot['cmd']
        try:
            #relfn, outfn, relinfile = cmd_2_image(app, img.plot)
            out = cmd_2_image(app, img.plot)
            if options.get("hidden", False):
                #Don't render the image if there is hidden
                nodes.image.pop(img)
                continue
            img['uri'] = out["outrelfn"]
            if img.get('alt', None):
                #For inline 用于类似这样的调用:.. |test1| plot:: convert
                #palms.jpg -grayscale rec601luma out.jpg
                uris[img['alt']] = img['uri']
                if app.builder.config.plot_log_level > 0:
                    print("uris: %s" %(uris))
            if os.path.splitext(out["outfullfn"])[-1] in [".png",".jpg",".gif"]:
                #对于png, jpg, gif 文件，手动获取它的大小
                i = Image.open(out["outfullfn"])
                if img.get("scale", None):
                    img["width"] = "%d" %(i.width * img["scale"] / 100)
                    #print("width: %s" %(img["width"]))
                elif (not img.get("width", None)) and \
                        (not img.get("width", None)):
                    #Mainly for latex, give width if there is not.
                    img["width"] = "%d" %(i.width)
                if app.builder.config.plot_log_level > 1:
                    print("Guess the width: %s." %(img["width"]))
            #img['candidates']={'*': out["outrelfn"]}
            if out["outreference"]:
                reference_node = nodes.reference(refuri=out["outreference"])
                img.replace_self(reference_node)
                reference_node.append(img) 
            #if options.get("show_source", False):
            #    img.insert(0, nodes.literal_block("", "%s\n%s" %(cmd, text)))
        except PlotError as err:
            #app.builder.warn('plot error: ')
            print(err)
            img.replace_self(nodes.literal_block("", "%s\n%s" %(cmd, text)))
            continue
        if app.builder.config.plot_log_level > 0:
            print("%s(), img: %s" %(sys._getframe().f_code.co_name, img))

    #第二次遍历，解析inline image
    for img in doctree.traverse(nodes.image):
        if (not hasattr(img, 'plot')) and img.get('alt', None) and \
                (img['alt'] in uris.keys()):
            #inline image
            img['uri'] = uris[img['alt']]
            #img['candidates'] = {'*': uris[img['alt']]}
            print("------------------------------------------------------------")
            print("inline uri = %s" %(img['uri']))
            if app.builder.config.plot_log_level > 0:
                print("%s(), img plot cmd: %s, alt: %s"
                        %(sys._getframe().f_code.co_name,
                            (hasattr(img, 'plot')) and img.plot['cmd'] or None,
                            img.get('alt', None)))

    for fig in doctree.traverse(nodes.figure):
        if app.builder.config.plot_log_level > 0:
            print("%s(), figure plot: %s"
                    %(sys._getframe().f_code.co_name,
                        (hasattr(img, 'plot')) and img.plot['cmd'] or None))
        if not hasattr(fig, 'plot'):
            continue

        print("================================================================")
        cmd = fig.plot['cmd']
        text = fig.plot['text']
        options = fig.plot['options']

        try:
            #调用cmd_2_image生成图像, 再把图像的地址链接到figure的uri里, 这样
            #就是显示在文档里了
            out = cmd_2_image(app, fig.plot)
            if app.builder.config.plot_log_level > 0:
                print("%s(), out is %s" %(sys._getframe().f_code.co_name, out))

            if options.get("hidden", False):
                #Don't render the image if there is hidden
                nodes.figure.pop(fig)
                continue

            #Caption
            caption_node = nodes.caption("", options.get("caption", cmd))
            fig += caption_node
            fig['ids'] = ["plot"]

            #uri
            for img in fig.traverse(condition=nodes.image):
                img['uri'] = out["outrelfn"]
                if out["outreference"]:
                    reference_node = nodes.reference(refuri=out["outreference"])
                    reference_node += img
                    fig.replace(img, reference_node)
                if os.path.splitext(out["outfullfn"])[-1] in \
                        [".png", ".jpg", ".gif"]:
                    #对于png, jpg, gif 文件，手动获取它的大小
                    i = Image.open(out["outfullfn"])
                    if img.get("scale", None):
                        img["width"] = "%d" %(i.width * img["scale"] / 100)
                        #print("width: %s" %(img["width"]))
                    elif (not img.get("width", None)) and \
                            (not img.get("width", None)):
                        #Mainly for latex, give width if there is not.
                        img["width"] = "%d" %(i.width)
                    if app.builder.config.plot_log_level > 1:
                        print("Guess the width: %s." %(img["width"]))

            #if options.get("show_source", False):
            #    # rendere as a text
            #    fig["align"] = "left"
            #    fig.insert(0, nodes.literal_block("", "%s\n%s" %(cmd, text),
            #               align = "left"))
            #print("rending figure: %s" %(fig))
        except PlotError as err:
            #app.builder.warn('plot error: ')
            print(err)
            fig.replace_self(nodes.literal_block("", "%s\n%s" %(cmd, text)))
            continue
        if app.builder.config.plot_log_level > 0:
            print("%s(), fig: %s" %(sys._getframe().f_code.co_name, fig))

def setup(app):
    #注册2个回调函数
    app.add_directive('plot', PlotDirective)
    app.connect('doctree-read', doctree_read_callback)

    app.add_config_value('plot', 'plot', 'html')
    app.add_config_value('plot_args', [], 'html')
    #plot_log_level, 0: don't print debug info; 1: only print in parameters
    #and out result. 2: debug info
    app.add_config_value('plot_log_level', 0, 'html')
    app.add_config_value('plot_output_format', OUTPUT_DEFAULT_FORMATS, 'html')

#References
###########

#. reStructuredText and Sphinx Reference, https://documatt.com/restructuredtext-reference/element/figure.html

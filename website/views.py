from django.shortcuts import render
from django.contrib import messages
import os
import openai

# Create your views here.
def home(request):
    lang_list = ['abap', 'abnf', 'actionscript', 'ada', 'agda', 'al', 'antlr4', 'apacheconf', 'apex', 'apl', 'applescript', 'aql', 'arduino', 'arff', 'armasm', 'arturo', 'asciidoc', 'asm6502', 'asmatmel', 'aspnet', 'autohotkey', 'autoit', 'avisynth', 'avro-idl', 'awk', 'bash', 'basic', 'batch', 'bbcode', 'bbj', 'bicep', 'birb', 'bison', 'bnf', 'bqn', 'brainfuck', 'brightscript', 'bro', 'bsl', 'c', 'cfscript', 'chaiscript', 'cil', 'cilkc', 'cilkcpp', 'clike', 'clojure', 'cmake', 'cobol', 'coffeescript', 'concurnas', 'cooklang', 'coq', 'cpp', 'crystal', 'csharp', 'cshtml', 'csp', 'css', 'css-extras', 'csv', 'cue', 'cypher', 'd', 'dart', 'dataweave', 'dax', 'dhall', 'diff', 'django', 'dns-zone-file', 'docker', 'dot', 'ebnf', 'editorconfig', 'eiffel', 'ejs', 'elixir', 'elm', 'erb', 'erlang', 'etlua', 'excel-formula', 'factor', 'false', 'firestore-security-rules', 'flow', 'fortran', 'fsharp', 'ftl', 'gap', 'gcode', 'gdscript', 'gedcom', 'gettext', 'gherkin', 'git', 'glsl', 'gml', 'gn', 'go', 'go-module', 'gradle', 'graphql', 'groovy', 'haml', 'handlebars', 'haskell', 'haxe', 'hcl', 'hlsl', 'hoon', 'hpkp', 'hsts', 'http', 'ichigojam', 'icon', 'icu-message-format', 'idris', 'iecst', 'ignore', 'inform7', 'ini', 'io', 'j', 'java', 'javadoc', 'javadoclike', 'javascript', 'javastacktrace', 'jexl', 'jolie', 'jq', 'js-extras', 'js-templates', 'jsdoc', 'json', 'json5', 'jsonp', 'jsstacktrace', 'jsx', 'julia', 'keepalived', 'keyman', 'kotlin', 'kumir', 'kusto', 'latex', 'latte', 'less', 'lilypond', 'linker-script', 'liquid', 'lisp', 'livescript', 'llvm', 'log', 'lolcode', 'lua', 'magma', 'makefile', 'markdown', 'markup', 'markup-templating', 'mata', 'matlab', 'maxscript', 'mel', 'mermaid', 'metafont', 'mizar', 'mongodb', 'monkey', 'moonscript', 'n1ql', 'n4js', 'nand2tetris-hdl', 'naniscript', 'nasm', 'neon', 'nevod', 'nginx', 'nim', 'nix', 'nsis', 'objectivec', 'ocaml', 'odin', 'opencl', 'openqasm', 'oz', 'parigp', 'parser', 'pascal', 'pascaligo', 'pcaxis', 'peoplecode', 'perl', 'php', 'php-extras', 'phpdoc', 'plant-uml', 'plsql', 'powerquery', 'powershell', 'processing', 'prolog', 'promql', 'properties', 'protobuf', 'psl', 'pug', 'puppet', 'pure', 'purebasic', 'purescript', 'python', 'q', 'qml', 'qore', 'qsharp', 'r', 'racket', 'reason', 'regex', 'rego', 'renpy', 'rescript', 'rest', 'rip', 'roboconf', 'robotframework', 'ruby', 'rust', 'sas', 'sass', 'scala', 'scheme', 'scss', 'shell-session', 'smali', 'smalltalk', 'smarty', 'sml', 'solidity', 'solution-file', 'soy', 'sparql', 'splunk-spl', 'sqf', 'sql', 'squirrel', 'stan', 'stata', 'stylus', 'supercollider', 'swift', 'systemd', 't4-cs', 't4-templating', 't4-vb', 'tap', 'tcl', 'textile', 'toml', 'tremor', 'tsx', 'tt2', 'turtle', 'twig', 'typescript', 'typoscript', 'unrealscript', 'uorazor', 'uri', 'v', 'vala', 'vbnet', 'velocity', 'verilog', 'vhdl', 'vim', 'visual-basic', 'warpscript', 'wasm', 'web-idl', 'wgsl', 'wiki', 'wolfram', 'wren', 'xeora', 'xml-doc', 'xojo', 'xquery', 'yaml', 'yang', 'zig']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # Check to make sure language is picked
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to pick a programming language")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        else:
            # OPENAI
            openai.organisation = os.environ.get("OPENAI_ORG")
            openai.api_key = os.environ.get("OPENAI_API_KEY")
            # print("ORG:", openai.organisation)
            # print("API Key:", openai.api_key)
            openai.Model.list()
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f"Respond only with code. Fix this {lang} code: {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                # print(response)
                response = response["choices"][0]["text"].strip()
                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'code': code, 'lang': lang})
            except Exception as e:
                # print(e)
                return render(request, 'home.html', {'lang_list': lang_list, 'response': e, 'lang': lang})
    return render(request, 'home.html', {'lang_list': lang_list})

def suggest(request):
    if request.method == "POST":
        code = request.POST['code']

        # OPENAI
        openai.organisation = os.environ.get("OPENAI_ORG")
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        # print("ORG:", openai.organisation)
        # print("API Key:", openai.api_key)
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = f"Respond only with code. {code}",
                temperature = 0,
                max_tokens = 1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            # print(response)
            response = response["choices"][0]["text"].strip()
            return render(request, 'suggest.html', {'response': response, 'code': code})
        except Exception as e:
            # print(e)
            return render(request, 'suggest.html', {'response': e})
    return render(request, 'suggest.html', {})
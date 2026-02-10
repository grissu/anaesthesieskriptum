# -*- coding: utf-8 -*-

project             = u'Kremser Anästhesieskriptum'
copyright           = u'Sebastian Gabriel | Lizenz: Creative Commons Namensnennung-Share Alike 4.0 International'
author              = u'Sebastian Gabriel (Hg.)'
institution         = u'Medieninhaber: Sebastian Gabriel -- c/o RA Matutis, Fürstenstraße 5, 5400 Hallein'


is_in_development   = True
pdf_page_format     = "a4"

# Show stuff:
show_authors        = True
todo_include_todos  = True
numfig              = True
numfig_secnum_depth = 0
numfig_format       = {
    'figure': 'Fig. %s',
    'table': 'Tab. %s',
    'code-block': 'Listing %s',
    'section': 'Abschnitt %s'
}
latex_show_pagerefs = False
latex_show_urls     = 'no'

suppress_warnings   = [
                        'image.not_readable',
                        'myst.directive_parse',
                        'ref.citation',
                        'ref.ref',
                      ]
keep_warnings       = True
trim_footnote_reference_space = True



# find . -type f -name "*.md" | while read -r file; do
#     echo "#    '$file',"
# done



### BEYOND THIS LINE THERE ARE DRAGONS! ######################################



















































### BEWARE OF THE DRAGONS!

import sys
import os
import re
from sphinx.util import logging
logger = logging.getLogger(__name__)

is_draft = False

exclude_patterns    = [
    '_build/*',
    '_static/*',
    ]


if tags.has('draft'):
    show_status         = "draft"
    tags.add('Entwicklung')
    is_draft            = True
    todo_include_todos  = True
elif tags.has('sprint'):
    show_status         = "sprint"
    tags.add('Entwicklung')
    is_draft            = True
    todo_include_todos  = True
elif tags.has('review'):
    show_status         = "review"
    is_draft            = True
    todo_include_todos  = False
elif tags.has('final'):
    show_status         = "final"
    is_draft            = False
    todo_include_todos  = False
else:
    logger.warning("\033[5m No document status defined!\033[0m (allowed: draft, sprint, review, final).. setting defaults ..")
    show_status         = "final"
    is_draft            = False
    todo_include_todos  = False

if tags.has('letter'):
    pdf_page_format     = "letter"
elif tags.has('a4'):
    pdf_page_format     = "a4"
else:
    pdf_page_format     = "a4"



def tex_sanitize(s):
    """Sanitizes a string so that it can be properly compiled in TeX.
    Escapes the most common TeX special characters: ~^_#%${}
    Removes backslashes.
    """
    s = re.sub('\\\\', '', s)
    s = re.sub(r'([_^$%&#{}])', r'\\\1', s)
    s = re.sub(r'\~', r'\\~{}', s)
    return s



########################################################################
# Version information
########################################################################

# Read git repository information
print("\nUsing git-based descriptive versioning (GitAutoVersion) ...\n")

import git
import GitAutoVersion

repo = git.Repo('..')

# git describe --long --tags --abbrev=7 | sed -e 's/^v//' -e 's/-\([[:digit:]]\+\)-\(g[[:alnum:]]\{7\}\)$/+\1#\2/'


try:
    version = GitAutoVersion.getVersionString(
        repo,
        flag_branch      = "branch",
        flag_development = "DRAFT",
        flag_dirty       = "DIRTY",
        flag_git         = "commit",
        version_prefix   = "v"
        )
except:
    version = "undetermined"

release = version

print("Version is " + version)
print("Release is " + release)

version_latex = tex_sanitize(version)

def setup(app):
    app.add_config_value('releaselevel', '', 'env')



########################################################################
# General configuration
########################################################################

print("----------------------------------------------")
print("General settings     :")
print("----------------------------------------------")
print("Version              : " + version)
print("Release              : " + release)
print("is_draft             : " + str(is_draft))
print("show_status          : " + str(show_status))
print("pdf_page_format      : " + str(pdf_page_format))
print("show_authors         : " + str(show_authors))
print("todo_include_todos   : " + str(todo_include_todos))
print("numfig               : " + str(numfig))
print("----------------------------------------------")
print("Tags                 :")
print("----------------------------------------------")
print(str(tags))

sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-extensions-contrib'))
sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-changeset'))
sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-extensions-contrib'))
sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-frontmatter-expose'))
sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-frontmatter-filter'))
sys.path.append(os.path.abspath('../Submodules/hex15-sphinx-margin'))

extensions                  = [
    'myst_parser',
    'figtable',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_git',
    'sphinx_subfigure',
    'sphinx_design',
    'sphinx_issues',
    'hex15-sphinx-changeset',
    'hex15-sphinx-frontmatter-expose',
#    'hex15-sphinx-frontmatter-filter',
    'hex15-sphinx-margin',
]

myst_enable_extensions      = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# sd_fontawesome_latex        = True

issues_github_path = "CriticalCareClub/Kompendium-alpha"

imgmath_latex               = "dvilualatex"
imgmath_image_format        = "svg"
imgmath_font_size           = 16
imgmath_latex_preamble      = '\\usepackage{unicode-math} \\usepackage{icomma} \\setmathfont{libertinus math} \\usepackage{libertinus}'



# myst_linkify_fuzzy_links = False

myst_substitutions          = {
    'McgPerKg': 'mcg / kg',
    'McgPerKgPerH': 'mcg / kg / h',
    'McgPerKgPerMin': 'mcg / kg / min',
    'MgPerKg': 'mg / kg',
    'MgPerKgPerH': 'mg / kg / h',
    'MgPerMl': 'mg / mL',
    'TxMassVitMKBes': '{ref}`Standardmaßnahmen bei vital bedrohten Patienten <standardmassnahmen-vital>`, Besonderheiten:',
    'TxMassVitMK': '{ref}`Standardmaßnahmen bei vital bedrohten Patienten <standardmassnahmen-vital>`',
    'TxBeiVit': 'Bei vitaler Bedrohung:',
    'IV': 'i. v.',
    'Text-NotReleased': 'Achtung -- Entwicklungsversion! Dieses Dokument ist **nicht freigegeben** und laufenden Änderungen unterworfen. Es enthält ungesicherte Informationen und ist als **unzuverlässig** und **rein informativ** zu betrachten. Die unerlaubte Verbreitung ist untersagt!',
    'Text-InkubatorInhalt': 'Diese Inhalte sind noch im **Inkubator-Stadium** und befinden sich noch nicht auf dem gewünschten fachlichen Niveau, bzw. sind unvollständig und bedürfen einer umfangreichen Überarbeitung. *Nur zur Ansicht oder zu Entwicklungszwecken!*',
    'TxAbcde1': '① — Szeneüberblick und (Selbst-)Schutz',
    'TxAbcde2': '② — Eindruck und HWS-Stabilisierung',
    'TxAbcde3': '③ — Bewusstsein',
    'TxAbcde4': '④ — Hauptbeschwerde',
    'TxAbcdeA': 'Ⓐ — Atemweg',
    'TxAbcdeB': 'Ⓑ — Atmung',
    'TxAbcdeC': 'Ⓒ — Kreislauf und STU',
    'TxAbcdeD': 'Ⓓ — Neurologie',
    'TxAbcdeE': 'Ⓔ — Erweiterte Untersuchung',
    'TxAbcdeAlt': '``…`` — Weiteres',
    'TxAbcdeFazit': '``=`` — Beurteilung',
    'Text-Sampler-S': '🅂 — Symptome und Schmerzen',
    'Text-Sampler-A': '🄰 — Allergien',
    'Text-Sampler-M': '🄼 — Medikation',
    'Text-Sampler-P': '🄿 — Patientengeschichte',
    'Text-Sampler-L': '🄻 — Letze …',
    'Text-Sampler-E': '🄴 — Ereignisse vor Notfalleintritt',
    'Text-Sampler-R': '🅁 — Risikofaktoren',
    'Text-Abcde-1-Short': '① — Szeneüberblick, Schutz',
    'Text-Abcde-2-Short': '② — Eindruck, HWS',
    'Text-Abcde-3-Short': '③ — Bewusstsein',
    'Text-Abcde-4-Short': '④ — Hauptbeschwerde',
    'Text-Abcde-A-Short': 'Ⓐ — Atemweg',
    'Text-Abcde-B-Short': 'Ⓑ — Atmung',
    'Text-Abcde-C-Short': 'Ⓒ — Kreislauf, STU',
    'Text-Abcde-D-Short': 'Ⓓ — Neurologie',
    'Text-Abcde-E-Short': 'Ⓔ — Erweitertet',
    'Text-Abcde-Alt-Short': '``…`` — Weiteres',
    'Text-Abcde-Fazit-Short': '``=`` — Beurteilung',
    'Text-Sampler-S-Short': '🅂 — Symptome',
    'Text-Sampler-A-Short': '🄰 — Allergien',
    'Text-Sampler-M-Short': '🄼 — Medikation',
    'Text-Sampler-P-Short': '🄿 — Patientengeschichte',
    'Text-Sampler-L-Short': '🄻 — Letzte …',
    'Text-Sampler-E-Short': '🄴 — Ereignisse',
    'Text-Sampler-R-Short': '🅁 — Risikofaktoren',
    'version': version,
    'linkpdfa4': '[Das Skriptum als PDF (beidseitiger Druck, A4)](https://anaesthesieskriptum.at/_static/Kremser-Anaesthesieskriptum_v' + version + '_a4.pdf)',
    'linkpdfletter': '[Das Skriptum als PDF (Tablet)](https://anaesthesieskriptum.at/_static/Kremser-Anaesthesieskriptum_v' + version + '_letter.pdf)',
    'Fortschritt': r'''
:::{margin} Fortschritt

☐ gelesen

☐ einmal wiederholt

☐ zweimal wiederholt

☐ gelernt
:::
''',
    'WIP': r'''
:::{attention}
Dieser Abschnitt ist in Arbeit!
:::
    ''',
    'INHALT': r'''
:::{raw} latex
\minitoc
:::
''',
    'Text_wie_kann_ich_beitragen': r'''
:::{admonition} Wie kann ich beitragen?
:class: hint

Das Melden von Fehlern oder Einsendung von Beiträgen kann über
-   unsere E-Mail-Adresse input@anaesthesieskriptum.at geschehen, oder über
-   das Ticketsystem auf unserem [Github™-Repository](https://github.com/grissu/anaesthesieskriptum/issues) (Github™-Konto erforderlich).

    Von der Webseite kann man auch mittels des Github™-Symbols in der rechten oberen Ecke direkt ein Ticket erstellen:

    ![alt text](/Bilder/Screenshot_open-issue-Detail.png)

Bitte beachten Sie {numref}`Hinweise-zur-Einreichung`: "{ref}`Hinweise-zur-Einreichung`".
:::
'''
}

# myst_linkify_fuzzy_links = False

templates_path              = ['../System/templates']
locale_dirs                 = ['../System/locales']
source_suffix               = ['.md', '.rst']
master_doc                  = 'index'
language                    = 'de'
pygments_style              = 'sphinx'

actdiag_html_image_format   = "SVG"
actdiag_latex_image_format  = "pdf"
actdiag_fontpath            = 'Quelltext/_static/lexend/LexendDeca-Regular.ttf'

rst_prolog = """
.. role:: deep

.. role:: cave
"""

md_prolog = """
:::{role} deep
:::

:::{role} cave
:::
"""









########################################################################
# HTML settings
########################################################################

announcement                = "<strong><font color=\"FF0000\">&#128679; ACHTUNG!</font></strong> Dies ist eine <strong><font color=\"FF0000\"> VORABVERSION</font></strong> (v" + version + ") &#9888;"
html_title                  = u"Sebastian Gabriel"
html_short_title            = u'Sebastian Gabriel'
html_logo                   = './Bilder/Logos/AINS-KrAS_v006-solarized.svg'
html_favicon                = './Bilder/Logos/AINS-KrAS_v006-solarized.svg'
html_show_sourcelink        = True
html_theme_path             = ["../System/themes", ]
html_static_path            = ['../System/static']
html_theme                  = "sphinx_book_theme"
html_css_files              = [
                                "pst-definitions.css",
                                "pst-customization.css",
                                "pst-settings-solarized.css",
                                "lexend/lexend.css",
                              ]

html_theme_options          = {
    "announcement"          : announcement,
    "collapse_navigation"   : False,
    "toc_title"             : u"Auf dieser Seite ...",
#    "use_sidenotes": True,
    "repository_provider"   : 'github',
    "repository_url"        : 'https://github.com/grissu/anaesthesieskriptum',
    "repository_branch"     : u"master",
    "use_repository_button" : True,
    "use_download_button"   : False,
    "use_fullscreen_button" : True,
    "use_issues_button"     : True,
#    "navbar_start": ["navbar-logo"],
#    "navbar_center": ["navbar-nav"],
#    "navbar_end": ["navbar-icon-links"],
#    "navbar_persistent": ["search-button"],
#    "navbar_align": "left",
    "primary_sidebar_end"   : ["indices.html"],
    "home_page_in_toc"      : True,
}

















########################################################################
# -- Options for LaTeX output
########################################################################

latex_engine                      = 'lualatex'

latex_additional_files            = [
    'Bilder/Logos/AINS-KrAS_v006.pdf',
    'Bilder/Logos/AINS-KrAS_v006-solarized.pdf',
    'hyphenation.inc',
    "../Submodules/hex15-sphinx-extensions-contrib/lua-ul.sty",
    "../Submodules/hex15-latex-styles/hex15-colors.sty",
    "../Submodules/hex15-latex-styles/hex15-fontsubst-lexend.sty",
    "../Submodules/hex15-latex-styles/hex15-fontsubst-source-serif.sty",
    "../Submodules/hex15-latex-styles/hex15-sphinx.sty",
    "../Submodules/hex15-latex-styles/hex15-theme-ccca.sty",
    "../Submodules/hex15-latex-styles/hex15-theme-klpu.sty",
    "../Submodules/hex15-latex-styles/hex15-theme-ks-alternate.sty",
    "../Submodules/hex15-latex-styles/hex15-theme-ks.sty",
    "../Submodules/hex15-latex-styles/hex15-theme-solarized.sty",
    ]

latex_elements                    = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'releasename': '\\hskip0pt',
    'transition': '\n',
    'fontpkg': r'''
        \setmainfont                                  {Lexend-Light}
        \setsansfont                                  {Lexend-Light}
        \setmonofont                                  {Latin Modern Mono}
    ''',
    'tableofcontents': r'\setcounter{tocdepth}{1}\tableofcontents',
    'preamble': r'''
        \RequirePackage{newunicodechar}
        \usepackage{hex15-sphinx}
        \usepackage{hex15-fontsubst-lexend}
        %\usepackage{hex15-theme-ccca}
        \usepackage{hex15-theme-solarized}
        \usepackage{icomma} % comma as decimal separator


        %\setmainfont                                 {Libertinus Serif}
        %\setsansfont                                 {Libertinus Sans}
        %\setmonofont                                 {Latin Modern Mono}
        %\setmathfont                                 {Libertinus Math}
        %\setfontfamily\FontSansFamily                {Libertinus Sans}
        %\setfontfamily\FontSansNarrowFamily          {Libertinus Sans}
        %\setfontfamily\FontSerifNarrowFamily         {Libertinus Sans}
        %\setfontfamily\FontTtNarrowFamily            {Latin Modern Mono}
        %\setfontfamily\FontDisplay                   {Lexend-Light}
        %\setfontfamily\FontHeaderFamily              {Lexend-Light}
        %\setfontfamily\FontKeyboardFamily            {Libertinus Keyboard}
        %\setfontfamily\FontSansCaptionFamily         {Libertinus Sans}
        %\setfontfamily\FontTable                     {Libertinus Sans}
        \setfontfamily\FontTitleFamily               {Lexend}
        %\setfontfamily\FontTitleDiscrete             {Lexend-Light}
        %\usepackage[ngerman]{hyphenat}

        \usepackage{layout} %
        \usepackage{printlen}
        \include{hyphenation.inc}


        % hook into Sphinx's "heavybox" environment (used for generic admonitions)
        \usepackage{etoolbox}
        \AtBeginEnvironment{sphinxheavybox}{\sffamily\small}

        \renewcommand{\sphinxaccelerator}[1]          {\underline{#1}}
        \renewcommand{\sphinxbfcode}[1]               {\textbf{\sphinxcode{#1}}}
        \renewcommand{\sphinxcode}[1]                 {\texttt{#1}}
        \renewcommand{\sphinxcrossref}[1]             {\emph{#1}}
        \renewcommand{\sphinxemail}[1]                {\texttt{#1}}
        \renewcommand{\sphinxguilabel}[1]             {\emph{#1}}
        \renewcommand{\sphinxkeyboard}[1]             {\sphinxcode{#1}}
        \renewcommand{\sphinxmenuselection}[1]        {\emph{#1}}
        \renewcommand{\sphinxtablecontinued}[1]       {\textsf{#1}}
        \renewcommand{\sphinxtitleref}[1]             {\emph{#1}}
        \renewcommand{\sphinxstyleindexentry}[1]      {#1}
        \renewcommand{\sphinxstyleindexextra}[1]      {(\emph{#1})}
        \renewcommand{\sphinxstyleindexpageref}[1]    {, \pageref{#1}}
        \renewcommand{\sphinxstyleindexpagemain}[1]   {\textbf{#1}}
        \renewcommand{\sphinxstyleindexlettergroup}[1]{{\Large\sffamily#1}\nopagebreak\vspace{1mm}}
        \renewcommand{\sphinxstyletopictitle}[1]      {\textbf{\color{red}#1}\par\medskip}
        \renewcommand{\sphinxstylesidebartitle}[1]    {{\FontHeaderFamily\textbf{#1}}\par\medskip}
        \renewcommand{\sphinxstyleothertitle}[1]      {\textbf{#1}}
        \renewcommand{\sphinxstylesidebarsubtitle}[1] {~\\\textbf{#1} \smallskip}
        \renewcommand{\sphinxstyleemphasis}[1]        {\emph{#1}}
        \renewcommand{\sphinxstyletheadfamily}        {\sffamily\bfseries}
        \renewcommand{\sphinxstyleliteralemphasis}[1] {\emph{\sphinxcode{#1}}}
        \renewcommand{\sphinxstylestrong}[1]          {\textbf{#1}}
        \renewcommand{\sphinxstyleliteralstrong}[1]   {\sphinxbfcode{#1}}
        \renewcommand{\sphinxstyleabbreviation}[1]    {\textsc{#1}}
        \renewcommand{\sphinxstyleliteralintitle}[1]  {\sphinxcode{#1}}
        \renewcommand{\sphinxstylecodecontinued}[1]   {{\footnotesize(#1)}}
        \renewcommand{\sphinxstylecodecontinues}[1]   {{\footnotesize(#1)}}
        \renewcommand{\sphinxstylenotetitle}[1]       {\sphinxdotitlerow{note}{\FontTitleFamily\small\bfseries#1}}

        \renewcommand{\sphinxstylehinttitle}[1]       {\sphinxdotitlerow{hint}      {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyleimportanttitle}[1]  {\sphinxdotitlerow{important} {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyletiptitle}[1]        {\sphinxdotitlerow{tip}       {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstylewarningtitle}[1]    {\sphinxdotitlerow{warning}   {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstylecautiontitle}[1]    {\sphinxdotitlerow{caution}   {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyleattentiontitle}[1]  {\sphinxdotitlerow{attention} {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyledangertitle}[1]     {\sphinxdotitlerow{danger}    {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyleerrortitle}[1]      {\sphinxdotitlerow{error}     {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxstyleseealsotitle}[1]    {\sphinxdotitlerow{seealso}   {\FontTitleFamily\small\bfseries#1}}
        \renewcommand{\sphinxtermref}[1]              {\emph{#1}}

        \renewcommand{\thepart}                     {\arabic{part}}
        \renewcommand{\thechapter}                  {\thepart.\arabic{chapter}}% Prefix chapter with part number
        \usepackage{chngcntr}
        \counterwithin*{chapter}{part}
        \renewenvironment{sphinxlegend}               {\footnotesize\sffamily}{\par}
        \usepackage{tocloft}
        \usepackage{titletoc}
        \setlength\cftchapindent{0em}
        \setlength\cftsecindent{0em}
        \setlength\cftsubsecindent{0em}
        \setlength\cftchapnumwidth{6em}
        \setlength\cftsecnumwidth{6em}
        \setlength\cftsubsecnumwidth{7.5em}
        %\titlecontents{section}
        %    [6em] % left
        %    {} % above code
        %    {\contentsmargin{0pt}\makebox[0pt][r]{\thecontentslabel\enspace}\large} %numbered-entry-format
        %    {\contentsmargin{0pt}\large} % numberless-entry-format
        %    {\quad\thepage} % filler-page-format
        %    [] % below-code
        %\titlecontents{subsection}
        %    [6em] % left
        %    {} % above code
        %    {\contentsmargin{0pt}\makebox[0pt][r]{\thecontentslabel\enspace}\large} %numbered-entry-format
        %    {\contentsmargin{0pt}\large} % numberless-entry-format
        %    {\quad\thepage} % filler-page-format
        %    [] % below-code
        \usepackage{minitoc}
        \dominitoc
        \renewcommand{\mtctitle}{In diesem Kapitel:}

        \newenvironment{dummy}                        {}{}
        \RenewEnviron{sphinxsidebar}                  {\marginpar{\vspace{-0.5cm}\setlist{noitemsep}\FontDisplay\footnotesize\raggedright\BODY}}

        \newcommand{\marginsecnumber}[1]{%
            \makebox[0pt][r]{#1\hspace{0pt}}%
        }




        \hbadness=10000
        \vbadness=10000
        \setlength{\headheight}{13.6pt}
        \setlength{\baselineskip}{20pt}\linespread{1.05}
        \release{v''' + version_latex +
        '''}
    ''',
    'maketitle': r'''
        \MakeCleopatraTitlepage
                                                      {\FontTitleFamily Kremser Anästhesieskriptum} % 1: Short Title
                                                      {2} % 2: TitleScale
                                                      {\FontTitleFamily Facharztprüfung in a Nutshell} % 3: TitleTag
                                                      {\FontTitleFamily{\color{Default-Grey} vormals "Anästhesie Facharztprüfung kompakt" von Anita Aust}} % 4: Subtitle
                                                      {v\Release} % 5: Version
                                                      {\Release} % 6: Release
                                                      {
                                                          \includegraphics[width=11cm]{AINS-KrAS_v006-solarized.pdf}

                                                          \vfill

                                                      } % 7: Picture
                                                      {\FontTitleDiscrete Sebastian Gabriel (HG.)} % 8: Author
                                                      {v\Release} % 9: Date
    ''',
    'figure_align': 'H',
    'geometry': r'''
        \usepackage[
            verbose,
            a4paper,
            asymmetric,
            % reversemp,
            includemp,   % incl. marginpar
            includehead, % incl. header
            includefoot, % incl. footer
            inner  = 30pt,
            outer  = 30pt,
            top    = 6mm,
            bottom =  6mm,
            bindingoffset=45.50787pt,%0.50787+42.67912+2 → Rest=552pt
            marginparsep=15pt,
            marginparwidth = 154pt,
            % marginparpush=0pt,
            footskip = 7mm,
            % % headheight=0.5cm,
            % % headsep=0.5cm,
            %showframe,
            ]
    {geometry}
    ''',
    'printindex': r'\begin{ParWide}\footnotesize\raggedright\printindex\end{ParWide}',
}

if pdf_page_format == 'letter':
    latex_show_pagerefs           = False
    latex_show_urls               = False
    latex_elements['papersize']   = 'letterpaper'
    latex_elements['pointsize']   = '11pt'
    latex_elements['geometry']    = r'''
        \usepackage[
            verbose,
            letterpaper,
            asymmetric,
            % reversemp,
            includemp,   % incl. marginpar
            includehead, % incl. header
            includefoot, % incl. footer
            inner  = 29.5pt,
            outer  = 29.5pt,
            top    = 29.5pt,
            bottom = 29.5pt,
            bindingoffset=0pt,
            marginparsep=15pt,
            marginparwidth = 175pt,
            % marginparpush=0pt,
            footskip = 7mm,
            % % headheight=0.5cm,
            % % headsep=0.5cm,
            %showframe,
            ]
    {geometry}
    '''
    latex_elements['maketitle']   = r'''
        \MakeCleopatraTitlepage
                                                      {\FontTitleFamily Kremser Anästhesieskriptum} % 1: Short Title
                                                      {2} % 2: TitleScale
                                                      {\FontTitleFamily Facharztprüfung in a Nutshell} % 3: TitleTag
                                                      {\FontTitleFamily{\color{Default-Grey} vormals "Anästhesie Facharztprüfung kompakt" von Anita Aust}} % 4: Subtitle
                                                      {v\Release} % 5: Version
                                                      {\Release} % 6: Release
                                                      {
                                                          \includegraphics[width=11cm]{AINS-KrAS_v006-solarized.pdf}

                                                          \vfill

                                                      } % 7: Picture
                                                      {\FontTitleDiscrete Sebastian Gabriel (HG.)} % 8: Author
                                                      {v\Release} % 9: Date
    '''

latex_table_style                 = [
    'booktabs',
    'colorrows',
    ]
latex_toplevel_sectioning         = 'part'
latex_show_urls                   = 'no'
latex_documents                   = [
    (
        master_doc,
        'Kremser-Anaesthesieskriptum_v' + version +'_' + pdf_page_format +'.tex',
        u'KrAS',
        u'Sebastian Gabriel',
        'manual'
    ),
]




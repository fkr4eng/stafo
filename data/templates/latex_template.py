\documentclass[a4paper,twoside,english,ngerman,deutsch,german,sectrefs,envcountsame,envcountchap]{svmono}

\usepackage{xcolor}
\usepackage{listings}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{csquotes}
\usepackage{hyperref}

{% if context.preliminaries %}{% for line in context.preliminaries %}
{{line}}{% endfor %}{% endif %}

\begin{document}

{{context.content}}

\end{document}
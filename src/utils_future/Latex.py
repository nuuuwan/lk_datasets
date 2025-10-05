from utils import Log

log = Log("LatexDoc")


class Latex:

    @staticmethod
    def clean(x):
        x = str(x)
        return (
            x.replace("&", "\\&")
            .replace("%", "\\%")
            .replace("$", "\\$")
            .replace("#", "\\#")
            .replace("lk_", "")
            .replace("_", " ")
            .replace("~", "\\textasciitilde{}")
            .replace("^", "\\textasciicircum{}")
            .replace("'", "''")
            .replace("pmd", "PMD")
        )

    @staticmethod
    def itemize(*items):
        s = "\\begin{itemize}\n"
        for item in items:
            s += f"  \\item {Latex.clean(item)}\n"
        s += "\\end{itemize}\n"
        return s

    @staticmethod
    def link(url):
        return f"\\url{{{url}}}"
